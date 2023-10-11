# from django.contrib import admin
# from django.urls import path,include
# from soc_app.views import TriggerViewSet
# from rest_framework import routers
# # from . import views


# router = routers.DefaultRouter()
# # router.register(r'users', UserAuthViewSet, basename="register")

# router.register(r'trigger', TriggerViewSet, basename='trigger')

# urlpatterns = [   
#     path("", include(router.urls))   
    
# # 

from django.urls import path
from .views import TriggerViewSet

urlpatterns = [
    path('trigger/', TriggerViewSet.as_view({'post': 'create'}), name='trigger-create'),
    path('get_latest_pipeline_statuses_and_artifacts/', TriggerViewSet.as_view({'get': 'get_latest_pipeline_statuses_and_artifacts'}), name='latest-pipeline-status'),
    # Add other URL patterns for your viewset actions as needed
]