from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
import requests

class TriggerViewSet(viewsets.ViewSet):
    def create(self, request):
        if request.method == 'POST':
            data = request.data
            
            print(data)
            
            project_id = "121"
            gitlab_token = "DXnzFzayXA8Xbv6_kNSv"

            base_url = f'https://gitlab.os3.com/api/v4/'
            headers = {"PRIVATE-TOKEN": gitlab_token}

            if data:
              print(f'Triggering bracnh: wazuh-s100')  
              trigger_branch(base_url, project_id, headers, "wazuh-s100")  # Vm creations

            for branch in data:
              print(f'Triggering branch: {branch}')  
              trigger_branch(base_url, project_id, headers, branch)    #  tool installations
        
            return Response ({"message": "pipeline trigger"})
        else:
            return Response ({"message": "pipeline not trigger"})

    def get_latest_pipeline_statuses_and_artifacts(request):
        print("API Trigger")
        # Replace these variables with your actual GitLab project ID and private token
        project_id = "121"
        private_token = "DXnzFzayXA8Xbv6_kNSv"
        base_url = "https://gitlab.os3.com/api/v4/"
        headers = {"PRIVATE-TOKEN": private_token}
        pipeline_count = 2

        # Get the statuses of the latest pipelines
        latest_pipeline_statuses = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_count)

        # Get the artifacts for each of the latest pipelines
        all_artifacts = []
        for pipeline_status in latest_pipeline_statuses:
            pipeline_id = pipeline_status["id"]
            artifacts = get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id)
            all_artifacts.append({"status": pipeline_status["status"], "artifacts": artifacts})

        return JsonResponse({"pipelines": all_artifacts})  

def trigger_branch(base_url, project_id, headers, branch_name):
        data = {
            "ref": branch_name
            }
        response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=data, verify=False)
        print(response.status_code)
        if response.status_code == 201:
            return Response({'message': 'Pipeline triggered successfully.'})
        else:
            return Response({'message': 'Failed to trigger the pipeline.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_latest_pipeline_statuses(base_url, project_id, headers, count=2):
    print("Function 2 trigger")
    response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)

    if response.status_code != 200:
        raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")

    pipelines = response.json()
    if not pipelines:
        return []

    latest_pipelines = pipelines[:count]
    latest_statuses = []

    for pipeline in latest_pipelines:
        latest_status = pipeline['status']
        latest_statuses.append({"id": pipeline['id'], "status": latest_status})

    return latest_statuses

def get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id):
    print("Function 3 trigger")
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}/jobs", headers=headers, verify=False)

    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline jobs: {response.status_code}, {response.json()}")

    jobs = response.json()
    artifacts = []

    for job in jobs:
        response = requests.get(base_url + f"projects/{project_id}/jobs/{job['id']}/artifacts", headers=headers, verify=False)
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
                # Modify the following to fetch the required artifacts
                required_artifacts = ['ip.txt', 'elastic_creds.txt']
                for artifact_name in required_artifacts:
                    if artifact_name in zip_file.namelist():
                        content = zip_file.read(artifact_name).decode('utf-8')
                        artifacts.append({"filename": artifact_name, "content": content})

    return artifacts
