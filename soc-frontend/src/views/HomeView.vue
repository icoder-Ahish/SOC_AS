<template>
  <div class="header ">
    <h1>DURGA (Defense Utility for Risk Governance and Awareness)</h1>
    <a class="logout" href="#" @click..prevent="logout">Logout</a>
  </div>  
    <form method="post" @submit="validateForm">    
        <div class="container">
            <div class="left-panel">
                <div class="op">Select Options</div>
                <div class="tool-link" @click="handleClick('Thread_Detection');">Thread Detection And Prevention
                </div>
                <div class="tool-link" @click="handleClick('Log_Ingestion');">Log Ingestion
                </div>
                <div class="tool-link" @click="handleClick('Log_Analysis');">Log Analysis
                </div>
                <div class="tool-link" @click="handleClick('Backend_Storage');">Backend
                    Storage</div>
                <div class="tool-link" @click="handleClick('Visulization');">Visualization
                </div>
                <div class="tool-link" @click="handleClick('Intelligence_Enrichment');">
                    Intelligence Enrichment</div>
                <div class="tool-link" @click="handleClick('Case_Management');">Case
                    Management</div>
                <div class="tool-link" @click="handleClick('Automate_Automate');">
                    Automate</div>
                <div class="tool-link" @click="handleClick('Investigation');">Investigation
                </div>
                <div class="tool-link" @click="handleClick('Health_Monitoring');">Health
                    Monitoring</div>
                
                <!-- <div class="install-button-container">
                    <input type="submit" id="submit-button" name="submit" value="Install" style="display: none;" />
                </div> -->
            </div>
            <div class="center-panel" id="center-panel"  >
              <div id="intro">

                  <div class="txt1">Welcome To DURGA Platform</div>
                  <div class="txt2">Guarding with Open Source: Your Digital Safehouse</div>
                 
              </div>
              <div id="checkbox-container"></div>
              <div class="toolist"  v-html="centerPanelContent" ></div>
             
          </div>
          
            <div class="right-panel" id="right-panel" style="display: none;">
                <div class="op">Selected Tools</div>
                <div id="summary-container">

                </div>
                <div class="install-button-container">                  
                    <input type="submit" id="submit-button" name="submit" value="Install" style="display: none;" />
                </div>
            </div>
        </div>
    </form>
</template>

<script>

export default{
  name: 'App',
  data() {
    return {
      centerPanelContent: '', 
      selectedOptions: [],
    };
  }, 

  created(){
    window.addEventListener('beforeunload', () => {
                    localStorage.clear(); // Clear local storage
 });
 
  },                  
  methods:{
    validateForm() {
        console.log("Install button click");
            var checkboxes = document.querySelectorAll('input[type="checkbox"]');
            var checkedCount = 0;
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].checked) {
                  console.log(checkedCount);
                    checkedCount++;
                }
            }
            if (checkedCount === 0) {
                alert("Please select at least one option.");
                return false;
            }
            return true;
    },
    showSubmitButton() {
        // console.log("showButton function is called");
            var submitButton = document.getElementById('submit-button');
            submitButton.style.display = 'block';
        },
    handleClick(toolName){
      this.showToolSettings(toolName);
      this.showSubmitButton();
    },
    showToolSettings(toolName){
    //   console.log("showToolSetting is called");
      document.getElementById('intro').style.display = 'none';

      var rightPanel = document.getElementById('right-panel');
      rightPanel.style.display = 'block';

      if (toolName === 'Log_Analysis') {
        // Define the HTML content you want to display
        const settings = `<h2 class="mt-5 font-bold">Log Analysis Tools</h2>
          <div class="tool"><label for="Graylog">
            <input  type="checkbox" name="Graylog" id="Graylog"  value="Graylog" > Graylog

            <p class="tool-info">Graylog, with its user-friendly interface, offers comprehensive log management and analysis. It optimizes log storage, search, and alerting, making it a valuable tool for both security and operations. <a href="https://go2docs.graylog.org/5-1/home.htm">Read more</a></p>
            <img src=" ../../public/static/graylog.png" alt="">
          </label></div>
          <br>
          <div ><label for="Splunk">
            <input  type="checkbox" name="Splunk" id="Splunk" value="Splunk"> Splunk HEC
            <p class="tool-info">Splunk HEC facilitates HTTP-based log and event data ingestion. It enhances real-time data analysis, offering critical insights for organizations using Splunk for log management and monitoring. <a href="https://docs.splunk.com/Documentation/Splunk/9.1.1/Data/UsetheHTTPEventCollector">Read more</a></p>
            <img src=" ../../public/static/splunk.png" alt="">
          </label></div>
          <br>
          <div ><label for="LogAnalyzer">
            <input  type="checkbox" name="LogAnalyzer" id="LogAnalyzer" value="LogAnalyzer"> LogAnalyzer (formerly known as phpLogCon)
            <p class="tool-info">LogAnalyzer is a web-based log management tool designed for effective log analysis. It simplifies system issue monitoring and troubleshooting, ensuring robust log management. <a href="https://loganalyzer.adiscon.com/doc/">Read more</a></p>
            <img src=" ../../public/static/loganalyzer.png" alt="">
          </label></div>`;
        
       
        this.centerPanelContent = settings;
      }
      else  if (toolName === 'Log_Ingestion') {
                var settings = `<h2 class=" mt-5 font-bold">Log Ingestion Tools</h2>
                    <div class="tool"><label for="Fluentd">
                    <input  type="checkbox" name="Fluentd" id="Fluentd" value="Fluentd"> Fluentd  
                    <p class="tool-info">Fluentd simplifies data collection, enabling efficient log aggregation and flexible data routing. It plays a crucial role in log management, helping organizations centralize and analyze logs effectively. <a href="https://docs.fluentd.org/">Read more</a></p>
                    <img src=" ../../public/static/fluentdd.png " alt="Fluentd Logo">
                    </label></div>
                    <br>
                    <div class=""><label for="Filebeat">
                    <input  type="checkbox" name="Filebeat" id="Filebeat" value="Filebeat"> Filebeat 
                    <p class="tool-info">A lightweight member of the Elastic Stack, Filebeat efficiently ships logs to Elasticsearch. It ensures real-time log analysis and monitoring, enhancing observability and operational insights. <a href="https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-overview.html">Read more</a></p>
                    <img src=" ../../public/static/filebeat.png" alt="Filebeat Logo">
                    </label></div>
                    <br> 
                   
                    <div class=""><label for="Rsyslog">
                    <input  type="checkbox" name="Rsyslog" id="Rsyslog" value="Rsyslog"> Rsyslog 
                    <p class="tool-info">Rsyslog is a reliable open-source logging system. It centralizes log management, simplifying monitoring and troubleshooting of system and application events for organizations. <a href="https://www.rsyslog.com/doc/master/index.html">Read more</a></p>                 
                        <img src=" ../../public/static/rsyslog.png " alt="Rsyslog Logo">
                    </label></div> `;
                
        this.centerPanelContent = settings;
            }
            else if (toolName === 'Thread_Detection') {
                var settings = `<h2 class="mt-5 font-bold">Thread Detection And Prevention Tools</h2> 
                    <div class="tool"><label for="Wazuh"> 
                    <input  type="checkbox" name="Wazuh" id="Wazuh" value="Wazuh"> Wazuh 
                    <p class="tool-info">Wazuh helps monitoring cloud infrastructure at an API level, using integration modules that are able to pull security data from well known cloud providers, such as Amazon AWS, Azure or Google Cloud. In addition, Wazuh provides rules to assess the configuration of your cloud environment, easily spotting weaknesses. <a href="https://documentation.wazuh.com/current/index.html">Read more</a></p> 
                    <img src=" ../../public/static/WAZUH.png" alt="Wazuh Logo"> 
                    </label></div></div> 
                    <br> 
                    <div class="tool"><label for="OSSEC"> 
                    <input  type="checkbox" name="OSSEC" id="OSSEC" value="OSSEC"> OSSEC 
                    <p class="tool-info">OSSEC (Open Source HIDS SECurity) is a free, open-source host-based intrusion detection system (HIDS). It performs log analysis, integrity checking, Windows registry monitoring, rootkit detection, time-based alerting, and active response. <a href="https://documentation.wazuh.com/current/index.html">Read more</a></p> 
                    <img src=" ../../public/static/ossec.png" alt="Wazuh Logo"> 
                    </label></div>
                    <br> 
                    <div class="tool"><label for="MISP"> 
                    <input  type="checkbox" name="MISP" id="MISP" value="MISP"> MISP (Malware Information Sharing Platform) 
                    <p class="tool-info">MISP is an open source software and it is also a large community of MISP users creating, maintaining and operating communities of users or organizations sharing information about threats or cyber security indicators worldwide. <a href="https://documentation.wazuh.com/current/index.html">Read more</a></p> 
                    <img src=" ../../public/static/misp.png" alt="Wazuh Logo"> 
                    </label></div>`;
                    this.centerPanelContent = settings;
            }
            else if (toolName === 'Backend_Storage') {
                var settings = `<h2 class="mt-5 font-bold">Backend Storage Tools</h2> 
                    <div class="tool"><label for="WazuhIndexer"> 
                    <input  type="checkbox" name="WazuhIndexer" id="WazuhIndexer" value="WazuhIndexer"> Wazuh Indexer 
                    <p class="tool-info">A vital part of the Wazuh platform, the Wazuh Indexer handles indexing and querying of security data. It forms the cornerstone for effective threat detection and response strategies. <a href="https://documentation.wazuh.com/current/installation-guide/wazuh-indexer/index.html">Read more</a></p> 
                    <img src=" ../../public/static/wazuhindexer.png" alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="Elasticsearch"> 
                    <input  type="checkbox" name="Elasticsearch" id="Elasticsearch" value="Elasticsearch"> Elasticsearch 
                    <p class="tool-info">ElasticSearch, a distributed search and analytics engine, excels in storing and searching large data volumes. Its commonly utilized in ELK (Elasticsearch, Logstash, Kibana) stacks for diverse use cases <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html">Read more</a></p> 
                    <img src=" ../../public/static/elasticsearch.png " alt="Wazuh Logo"> 
                    </label></div>
                    <br> 
                    <div class="tool"><label for="Apache"> 
                    <input  type="checkbox" name="Apache" id="Apache" value="Apache Cassandra"> Apache Cassandra 
                    <p class="tool-info">Apache Cassandra is a highly scalable NoSQL database, ideal for managing extensive data volumes. Its focus on high availability and fault tolerance makes it an excellent choice for organizations. <a href="https://cassandra.apache.org/doc/latest/">Read more</a></p> 
                    <img src="../../public/static/apache.png" alt="Wazuh Logo"> 
                    </label></div>`;
                    this.centerPanelContent = settings;
            } 
            else if (toolName === 'sulization') {
                var settings = `<h2 class="mt-5 font-bold">Visulization Tools</h2> 
                    <div class="tool"><label for="Grafana"> 
                    <input  type="checkbox" name="Grafana" id="Grafana" value="Grafana"> Grafana 
                    <p class="tool-info">Grafana is an open-source platform known for data visualization and monitoring. It empowers organizations to create interactive dashboards for metrics and log data. <a href="https://grafana.com/docs/">Read more</a></p> 
                    <img src=" ../../public/static/grafana.png" alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="Kibana"> 
                    <input  type="checkbox" name="Kibana" id="Kibana" value="Kibana"> Kibana 
                    <p class="tool-info">Kibana serves as the user interface for Elasticsearch. It simplifies data exploration and visualization through interactive dashboards, making log and metric analysis straightforward. <a href="https://www.elastic.co/guide/en/kibana/current/index.html">Read more</a></p> 
                    <img src="../../public/static/ kibana.png " alt="Wazuh Logo"> 
                    </label></div>
                    <br> 
                    <div class="tool"><label for="Cabot"> 
                    <input  type="checkbox" name="Cabot" id="Cabot" value="Cabot"> Cabot 
                    <p class="tool-info">Cabot is a self-hosted open-source monitoring and alerting system. It keeps a vigilant eye on service and system health, ensuring timely notifications for potential issues. <a href="https://cabotapp.com/qs/quickstart.html">Read more</a></p> 
                    <img src=" ../../public/static/cabot.png " alt="Wazuh Logo"> 
                    </label></div>`;
                  
                    this.centerPanelContent = settings;
            } else if (toolName === 'Intelligence_Enrichment') {
                var settings = `<h2 class="mt-5 font-bold">Intelligence Enrichment Tools</h2> 
                    <div class="tool"><label for="OpenCTI"> 
                    <input  type="checkbox" name="OpenCTI" id="OpenCTI" value="OpenCTI"> OpenCTI 
                    <p class="tool-info">OpenCTI facilitates the collection, analysis, and sharing of cyber threat intelligence. It fosters collaboration among security professionals and organizations, enhancing threat awareness and preparedness. <a href="https://docs.opencti.io/latest/">Read more</a></p> 
                    <img src="../../public/static/opencti.png " alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="MISP"> 
                    <input  type="checkbox" name="MISP" id="MISP" value="MISP"> MISP (Malware Information Sharing Platform) 
                    <p class="tool-info">MISP, an open-source threat intelligence platform, enhances structured threat information sharing among security professionals, aiding in threat detection and mitigation. <a href="https://www.misp-project.org/documentation/">Read more</a></p> 
                    <img src="../../public/static/misp.png " alt="Wazuh Logo"> 
                    </label></div>`;
                    
                 this.centerPanelContent = settings;
            }
            else if (toolName === 'Case_Management') {
                var settings = `<h2 class="mt-5 font-bold">Case Management Tools</h2> 
                    <div class="tool"><label for="TheHIVE"> 
                    <input  type="checkbox" name="TheHIVE" id="TheHIVE" value="TheHIVE"> TheHIVE 
                    <p class="tool-info">TheHIVE streamlines incident response and case management with its open-source platform. It facilitates efficient handling of security incidents and promotes collaboration among analysts. <a href="https://docs.thehive-project.org/">Read more</a></p> 
                    <img src="../../public/static/thehive.png " alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="RTIR"> 
                    <input  type="checkbox" name="RTIR" id="RTIR" value="RTIR"> RTIR (Request Tracker for Incident Response) 
                    <p class="tool-info">RTIR extends Request Tracker for incident response teams. It provides comprehensive tools for managing and tracking security incidents and investigations effectively. <a href="https://docs.bestpractical.com/rtir/4.0.3/index.html">Read more</a></p> 
                    <img src="../../public/static/rtir.png " alt="Wazuh Logo"> 
                    </label></div>`;
                 this.centerPanelContent = settings;
            } else if (toolName === 'Automate_Automate') {
                var settings = `<h2 class="mt-5 font-bold">Automate Tools</h2> 
                    <div class="tool"><label for="Shuffle"> 
                    <input  type="checkbox" name="Shuffle" id="Shuffle" value="Shuffle"> Shuffle 
                    <p class="tool-info">Shuffle is an open-source framework tailored for managing and automating security playbooks. It equips organizations with the means to respond promptly and effectively to security incidents. <a href="https://shuffler.io/docs/about">Read more</a></p> 
                    <img src="../../public/static/shuffle.png " alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="Cortex"> 
                    <input  type="checkbox" name="Cortex" id="Cortex" value="Cortex"> Cortex 
                    <p class="tool-info">Cortex is an open-source observability and security automation platform. It integrates seamlessly with various security tools, automating responses to threats and enhancing security operations. <a href="https://docs.cortex.io/">Read more</a></p> 
                    <img src="../../public/static/cortex.png " alt="Wazuh Logo"> 
                    </label></div>`;
                 this.centerPanelContent = settings;
            } else if (toolName === 'Investigation') {
                var settings = `<h2 class="mt-5 font-bold">Investigation Tools</h2> 
                    <div class="tool"><label for="Velociraptor"> 
                    <input  type="checkbox" name="Velociraptor" id="Velociraptor" value="Velociraptor"> Velociraptor 
                    <p class="tool-info">Velociraptor is an open-source endpoint visibility and digital forensics tool. It empowers security professionals to collect and analyze endpoint data, aiding in threat detection and rapid response <a href="https://docs.velociraptor.app/docs/">Read more</a></p> 
                    <img src="../../public/static/velociraptor.png " alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="OSINT"> 
                    <input  type="checkbox" name="OSINT" id="OSINT" value="OSINT"> OSINT Framework 
                    <p class="tool-info">Open-source intelligence (OSINT) involves gathering and analyzing publicly available information from diverse sources to enhance security and investigative processes. <a href="https://osintframework.com/">Read more</a></p> 
                    <img src="../../public/static/osint.png " alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="ElastAlert"> 
                    <input  type="checkbox" name="ElastAlert" id="ElastAlert" value="ElastAlert"> ElastAlert 
                    <p class="tool-info">ElastAlert, an open-source alerting framework for Elasticsearch, enables organizations to define custom alerting rules and actions based on data in Elasticsearch indices. <a href="https://elastalert.readthedocs.io/en/latest/">Read more</a></p> 
                    <img src="../../public/static/elastalert.png " alt="Wazuh Logo"> 
                    </label></div>`;
                 this.centerPanelContent = settings;
                    }
            else if (toolName === 'Health_Monitoring') {
                var settings = `<h2 class="mt-5 font-bold">Health Monitoring Tools</h2> 
                    <div class="tool"><label for="InfluxDB"> 
                    <input  type="checkbox" name="InfluxDB" id="InfluxDB" value="InfluxDB"> InfluxDB 
                    <p class="tool-info">InfluxDB, an open-source time-series database, is optimized for efficient storage and querying of time-series data. It plays a pivotal role in monitoring and analytics applications. <a href="https://docs.influxdata.com/">Read more</a></p> 
                    <img src="../../public/static/influxdb.png " alt="Wazuh Logo"> 
                    </label></div> 
                    <br> 
                    <div class="tool"><label for="Prometheus"> 
                    <input  type="checkbox" name="Prometheus" id="Prometheus" value="Prometheus"> Prometheus 
                    <p class="tool-info">Prometheus is an open-source monitoring and alerting toolkit, designed to collect, process, and generate alerts based on metrics and predefined rules, aiding organizations in proactive system monitoring and issue detection <a href="https://prometheus.io/docs/prometheus/latest/getting_started/">Read more</a></p> 
                    <img src="../../public/static/prometheouss.png " alt="Wazuh Logo"> 
                    </label></div>`;
                 this.centerPanelContent = settings;
            }
            this.loadCheckboxStates(toolName)

    },
    loadCheckboxStates(toolName) {
                    // Replace this with your logic to load checkbox states from localStorage
                    var checkboxes = document.querySelectorAll('#center-panel input[type="checkbox"]');
                    checkboxes.forEach((checkbox) => {
                        var checkboxState = localStorage.getItem(toolName + '_' + checkbox.id);
                        if (checkboxState === 'true') {
                            this.selectedOptions[checkbox.name] = true;
                            checkbox.checked = true;
                            checkbox.closest('.tool').classList.add('selected');
                        } else {
                            this.selectedOptions[checkbox.name] = false;
                            checkbox.checked = false;
                            checkbox.closest('.tool').classList.remove('selected');
                        }

                        checkbox.addEventListener('change', () => {
                            if (checkbox.checked) {
                                this.selectedOptions[checkbox.name] = true;
                                checkbox.closest('.tool').classList.add('selected');
                            } else {
                                this.selectedOptions[checkbox.name] = false;
                                checkbox.closest('.tool').classList.remove('selected');
                            }
                            localStorage.setItem(toolName + '_' + checkbox.id, checkbox.checked);
                            // Call a method to update the summary when a checkbox is changed
                            this.updateSummary();
                        });
                    });
                },
        updateSummary() {
          console.log("UpdateSummary function call");
          var summaryContainer = document.getElementById('summary-container');
          summaryContainer.innerHTML = '';
                    for (var option in this.selectedOptions) {
                        if (this.selectedOptions.hasOwnProperty(option) && this.selectedOptions[option]) {
                            summaryContainer.innerHTML += '<p>' + option + '</p>';
                        }
            }
        },
        
    logout(){
      console.log("logout");
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      window.location.reload()
    }, 
 
  }
}

</script>
<style scoped>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

h1 {
    text-align: center;
    padding: 20px;
    color: #4285F4;
    background-color: #ffffff;
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
    margin-left: 10px;
    margin-right: 10px;
    border-radius: 15px;
}
h2 {
    color: #4285F4;
    font-size: 25px;
    text-shadow: 2px 2px 2px rgba(109, 109, 109, 0.3);
}
.container {
    display: flex;
    justify-content: space-between;
}

.left-panel {
    margin-left: 10px;
    margin-top: 17px;
    width: 20%;
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 5px 0px 10px rgba(0, 0, 0, 0.2);
    min-height: 80vh;
    /* Added */
    max-height: 80vh;
    /* Added */
    overflow-y: auto;
    /* Added for scrolling */
    position: relative;
    /* Added for positioning */
    display: flex;
    flex-direction: column;
    /* Adjusted to column layout */
}

.center-panel {
    width: 70%;
    background-color: #ffffff;
    padding: 20px;
    margin-left: 20px;
    margin-top: 17px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    margin-right: 20px;
    min-height: 80vh;
    /* Added */
    display: flex;
    flex-direction: column;
    /* Center elements vertically */
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
}
/* .info-container{
    width: 20%;
    display: flex;
    flex-direction: column;
    position: relative;
} */
.right-panel {
    margin-right: 10px;
    width: 20%;
    background-color: #f0f0f0;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 5px 0px 10px rgba(0, 0, 0, 0.2);
    min-height: 80vh;
    /* Added */
    max-height: 80vh;
    /* Added */
    overflow-y: auto;
    /* Added for scrolling */
    position: relative;
    /* Added for positioning */
    display: flex;
    flex-direction: column;
    /* Adjusted to column layout */
}
.tool-link {
    cursor: pointer;
    padding: 10px;
    border: 1px solid #ccc;
    background-color: #fff;
    border-radius: 10px;
    margin-bottom: 10px;
    text-align: center;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.3);
    font-size: 18px;
}

.tool-link:hover {
    background-color: #cbcbcb;
}

.op {
    padding: 10px;
    margin-bottom: 30px;
    text-align: center;
    /* background-color: #4285F4; */
    color: #4285F4;
    /* border-radius: 10px; */
    /* box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.3); */
    position: relative; /* Position relative to allow for pseudo-element */
    font-size: 25px;
    font-weight: bold;
    text-shadow: 2px 2px 2px rgba(109, 109, 109, 0.3);
}

.op::after {
    content: ""; /* Pseudo-element for the underline */
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 2px; /* Adjust this value for the thickness of the line */
    background-color: #4285F4; /* Color of the line */
}



.logout {
    position: absolute;
    top: 5px;
    right: 20px;
    text-decoration: none;
    color: #fff;
    padding: 10px 20px;
    background-color: #4285F4;
    font-size: 18px;
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
    border-radius: 5px;
    border: 1px solid #ccc;

}

label {
    display: block;
    margin-bottom: 10px;
    color: #000000;
    font-weight: bold;
    font-size: 20px;
    padding: 10px;
}

input[type="checkbox"] {
    margin-right: 10px;
    vertical-align: middle;
    height: 18px;
    width: 18px;
    display: none;
}

.logout:hover {
    background-color: #3074ED;
}

.install-button-container {
    margin-top: auto;
    /* Pushes the install button to the bottom */
    width: 90%;
    position: absolute;
    bottom: 0;
    left: 0;
    margin-bottom: 20px;
}

input[type="submit"] {
    padding: 10px;
    background-color: #4285F4;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 18px;
    width: 100%;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.3);
    text-align: center;
    justify-content: space-between;
    margin-left: 20px;
    font-weight: bold;
    
}

input[type="submit"]:hover {
    background-color: #3074ED;
}

.txt1 {
  font-size: 75px;
  color: #bbbaba;
  margin-top: 75px;
  font-weight: bold;
  padding: 5px;
  margin-top: 20%;
  text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.3);
}

.txt2 {
  font-size: 30px;
  color: #575757;
  margin-top: 10px;
  font-weight: bold;
  padding: 5px;
}


#summary-container h2 {
    font-size: 18px;
    font-weight: bold;
    color: #4285F4;
    margin-bottom: 10px;
}

#summary-container p {
    margin: 0;
    font-size: 18px;
    color: #333;
    padding: 5px 0;
    font-weight: bold;
}
.tool{
    /* border: 1px solid black; */
    margin-bottom: 10px;
    padding: 10px  ;
    max-width: 50%;
    max-height: 50%;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.3);
    border-radius: 15px;
    display: flex;
}
img{
    width: 100px;
    height: 100px;
    object-fit: contain;
    margin-top: 2px;
}
.tool-info{
    font-size: 15px;
    color: #575757;
}
.selected {
background-color: #d4d4d4; 
border: 1px solid #333;
}
</style>
