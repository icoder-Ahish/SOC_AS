<template>


    <nav class="fixed top-0 z-50 w-full bg-white border-b border-gray-200 dark:bg-gray-800 dark:border-gray-700">
        <div class="px-3 py-3 lg:px-5 lg:pl-3">
          <div class="flex items-center justify-between">
            <div class="flex items-center justify-start">
              <button data-drawer-target="logo-sidebar" data-drawer-toggle="logo-sidebar" aria-controls="logo-sidebar" type="button" class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
                  <span class="sr-only">Open sidebar</span>
                  <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                     <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
                  </svg>
               </button>
              <a href="#" class="flex ml-2 md:mr-24">
                <img src="static/DUGA.png" class="w-11 rounded-full h-11 mr-3" alt="Logo" />
                <span class="self-center text-xl font-semibold sm:text-2xl whitespace-nowrap dark:text-white">DURGA</span>
              </a>
            </div>
             <div class="flex flex-col  items-center">
                <div class="flex  items-center ml-3">
                  <div>
                    <button type="button" @click.prevent="toggleModal" v-if="selectedTools.length > 0" class="flex text-sm text-blue-100 bg-gray-800 p-3  rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" >
                        install                      
                    </button>
                  
                    <!-- <button @click="toggleUserMenu" type="button" class="flex text-sm bg-gray-800 rounded-full focus:ring-4 focus:ring-gray-300 dark:focus:ring-gray-600" aria-expanded="false" data-dropdown-toggle="dropdown-user">
                      <span class="sr-only">Open user menu</span>
                      <img class="w-8 h-8 rounded-full" src="static/admin.jpeg" alt="user photo">
                    </button> -->
                  </div>
                   <!-- <div  v-if="!userMenuVisible" class="z-50 hidden my-4 text-base list-none bg-white divide-y divide-gray-100 rounded shadow dark:bg-gray-700 dark:divide-gray-600" id="dropdown-user">
                    <div class="px-4 py-3" role="none">
                      <p class="text-sm text-gray-900 dark:text-white" role="none">
                        ADMIN
                      </p>
                      <p class="text-sm font-medium text-gray-900 truncate dark:text-gray-300" role="none">
                        admin.ashish@mycompany.com
                      </p>
                    </div>
                    <ul class="py-1" role="none">
                      <li>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Dashboard</a>
                      </li>
                      <li>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Settings</a>
                      </li>
                      <li>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Billing</a>
                      </li>
                      <li>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-600 dark:hover:text-white" role="menuitem">Sign out</a>
                      </li>
                    </ul>
                  </div>  -->
                </div>
              </div> 
          </div>
        </div>
      </nav>
      
      <aside id="logo-sidebar" class="fixed top-0 left-0 z-40 h-screen pt-20 transition-transform -translate-x-full bg-white border-r border-gray-200 sm:translate-x-0 dark:bg-gray-800 dark:border-gray-700" aria-label="Sidebar">
         <div class="h-full px-3 pb-4 overflow-y-auto bg-white dark:bg-gray-800">
            <ul class="space-y-2 font-medium">
               <li>
                  <a href="#HOM" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                     <svg class="w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 22 21">
                        <path d="M16.975 11H10V4.025a1 1 0 0 0-1.066-.998 8.5 8.5 0 1 0 9.039 9.039.999.999 0 0 0-1-1.066h.002Z"/>
                        <path d="M12.5 0c-.157 0-.311.01-.565.027A1 1 0 0 0 11 1.02V10h8.975a1 1 0 0 0 1-.935c.013-.188.028-.374.028-.565A8.51 8.51 0 0 0 12.5 0Z"/>
                     </svg>
                     <span class="ml-3">DURGA Dashboard</span>
                  </a>
               </li>
               <hr>
               <li>
                  <a href="#LI"  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                     <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 18">
                        <path d="M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10Zm10 0h-4.286A1.857 1.857 0 0 0 10 11.857v4.286c0 1.026.831 1.857 1.857 1.857h4.286A1.857 1.857 0 0 0 18 16.143v-4.286A1.857 1.857 0 0 0 16.143 10Z"/>
                     </svg> -->
                     <span class="flex-1 ml-3 whitespace-nowrap">Log Ingestion</span>
                     <!-- <span class="inline-flex px-2 ml-3 text-sm font-medium text-gray-800 bg-gray-100 rounded-full dark:bg-gray-700 dark:text-gray-300">Pro</span> -->
                  </a>
               </li>
               <li>
                  <a href="#LA" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                     <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                        <path d="m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z"/>
                     </svg> -->
                     <span class="flex-1 ml-3 whitespace-nowrap">Log Analysis</span>
                     <!-- <span class="inline-flex w-3 h-3 p-3 ml-3 text-sm font-medium text-blue-800 bg-blue-100 rounded-full dark:bg-blue-900 dark:text-blue-300">3</span> -->
                  </a>
               </li>
               <li>
                  <a href="#BS" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                     <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                        <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                     </svg> -->
                     <span class="flex-1 ml-3 whitespace-nowrap">Backend Storage</span>
                  </a>
               </li>
               <li>
                  <a href="#V" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                     <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 20">
                        <path d="M17 5.923A1 1 0 0 0 16 5h-3V4a4 4 0 1 0-8 0v1H2a1 1 0 0 0-1 .923L.086 17.846A2 2 0 0 0 2.08 20h13.84a2 2 0 0 0 1.994-2.153L17 5.923ZM7 9a1 1 0 0 1-2 0V7h2v2Zm0-5a2 2 0 1 1 4 0v1H7V4Zm6 5a1 1 0 1 1-2 0V7h2v2Z"/>
                     </svg> -->
                     <span class="flex-1 ml-3 whitespace-nowrap">Visualization</span>
                  </a>
               </li>
               <li>
                  <a href="#IE" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                     <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 16">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"/>
                     </svg> -->
                     <span class="flex-1 ml-3 whitespace-nowrap">Intelligent Enrichment</span>
                  </a>
               </li>
               <li>
                <a href="#TDP" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                   <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 16">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"/>
                   </svg> -->
                   <span class="flex-1 ml-3 whitespace-nowrap">Thread Detection And Prevention</span>
                </a>
             </li>
               <li>
                <a href="#CM" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                   <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                      <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                   </svg> -->
                   <span class="flex-1 ml-3 whitespace-nowrap">Case Management</span>
                </a>
             </li>
             <li>
                <a href="#ATO" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                   <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                      <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                   </svg> -->
                   <span class="flex-1 ml-3 whitespace-nowrap">Automate</span>
                </a>
             </li>
             <li>
                <a href="#INV" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                   <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                      <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                   </svg> -->
                   <span class="flex-1 ml-3 whitespace-nowrap">Investigation</span>
                </a>
             </li>
             <li>
                <a href="#HM" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                   <!-- <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                      <path d="M14 2a3.963 3.963 0 0 0-1.4.267 6.439 6.439 0 0 1-1.331 6.638A4 4 0 1 0 14 2Zm1 9h-1.264A6.957 6.957 0 0 1 15 15v2a2.97 2.97 0 0 1-.184 1H19a1 1 0 0 0 1-1v-1a5.006 5.006 0 0 0-5-5ZM6.5 9a4.5 4.5 0 1 0 0-9 4.5 4.5 0 0 0 0 9ZM8 10H5a5.006 5.006 0 0 0-5 5v2a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-2a5.006 5.006 0 0 0-5-5Z"/>
                   </svg> -->
                   <span class="flex-1 ml-3 whitespace-nowrap">Health Monitoring</span>
                </a>
             </li>
             <li>
                <hr>
                <a href="#" @click.prevent="logout" class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
                   <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 16">
                      <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M1 8h11m0 0L8 4m4 4-4 4m4-11h3a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-3"/>
                   </svg>
                   <span class="flex-1 ml-3 whitespace-nowrap">Sign out</span>
                </a>
             </li>
               
            </ul>
         </div>
      </aside>
     
      <div class="p-4 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 ">   
            <div class="rounded bg-gray-50 dark:bg-gray-800">         
            <section class="shadow-inner" id="HOM">
                <h1 class="txt1">Welcome to our DURGA Platform</h1>
                <div class="txt2">Guarding with Open Source: Your Digital Safehouse</div>
            </section> <hr>
        
            <section class="shadow-inner" id="LI">
                <h1 class=""> Log Ingestion</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    <div class="border-2 border-gray-200 border-dashed">
                        <div class="tool"><label for="Fluentd">
                            <input v-model="selectedTools"  type="checkbox" name="Fluentd" id="Fluentd" value="fluentd"> Fluentd  
                                <p class="tool-info">Fluentd simplifies data collection, enabling efficient log aggregation and flexible data routing. It plays a crucial role in log management, helping organizations centralize and analyze logs effectively. <a href="https://docs.fluentd.org/">Read more</a></p>
                                <img class="tool_img" src=" static/fluentdd.png " alt="Fluentd Logo">
                             </label>
                            </div>
                        </div>
                    <div class="border-2 border-gray-200 border-dashed">
                        <div class=""><label for="Filebeat">
                                    <input v-model="selectedTools" type="checkbox" name="Filebeat" id="Filebeat" value="filebeat"> Filebeat 
                                    <p class="tool-info">A lightweight member of the Elastic Stack, Filebeat efficiently ships logs to Elasticsearch. It ensures real-time log analysis and monitoring, enhancing observability and operational insights. <a href="https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-overview.html">Read more</a></p>
                                    <img class="tool_img" src=" static/filebeat.png" alt="Filebeat Logo">
                        </label></div>
                    </div>
                    <div class="border-2 border-gray-200 border-dashed">
                        <div class=""><label for="Rsyslog">
                                        <input v-model="selectedTools" type="checkbox" name="Rsyslog" id="Rsyslog" value="rsyslog"> Rsyslog 
                                        <p class="tool-info">Rsyslog is a reliable open-source logging system. It centralizes log management, simplifying monitoring and troubleshooting of system and application events for organizations. <a href="https://www.rsyslog.com/doc/master/index.html">Read more</a></p>                 
                                        <img class="tool_img" src=" static/rsyslog.png " alt="Rsyslog Logo">
                        </label></div>
                    </div>  
                </div>
            </section> <hr>
        
            <section class="shadow-inner" id="LA">
                <h1 class="">Log Analysis</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                     <div class="tool border-2 border-gray-200 border-dashed"><label for="Graylog">
                        <input v-model="selectedTools"  type="checkbox" name="Graylog" id="Graylog"  value="graylog" > Graylog
                        <p class="tool-info">Graylog, with its user-friendly interface, offers comprehensive log management and analysis. It optimizes log storage, search, and alerting, making it a valuable tool for both security and operations. <a href="https://go2docs.graylog.org/5-1/home.htm">Read more</a></p>
                        <img class="tool_img" src=" static/graylog.png" alt="">
                      </label></div>
                     
                      <div class="border-2 border-gray-200 border-dashed"><label for="Splunk">
                        <input v-model="selectedTools" type="checkbox" name="Splunk" id="Splunk" value="splunk"> Splunk HEC
                        <p class="tool-info">Splunk HEC facilitates HTTP-based log and event data ingestion. It enhances real-time data analysis, offering critical insights for organizations using Splunk for log management and monitoring. <a href="https://docs.splunk.com/Documentation/Splunk/9.1.1/Data/UsetheHTTPEventCollector">Read more</a></p>
                        <img class="tool_img" src=" static/splunk.png" alt="">
                      </label></div>
                   
                      <div class="border-2 border-gray-200 border-dashed"><label for="LogAnalyzer">
                        <input v-model="selectedTools" type="checkbox" name="LogAnalyzer" id="LogAnalyzer" value="logAnalyzer"> LogAnalyzer (formerly known as phpLogCon)
                        <p class="tool-info">LogAnalyzer is a web-based log management tool designed for effective log analysis. It simplifies system issue monitoring and troubleshooting, ensuring robust log management. <a href="https://loganalyzer.adiscon.com/doc/">Read more</a></p>
                        <img class="tool_img" src=" static/loganalyzer.png" alt="">
                      </label></div>
                </div>    
            </section><hr>
            <section class="shadow-inner" id="BS">
                <h1  class="">Backend Storage </h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                    <div class="tool"><label for="WazuhIndexer"> 
                    <input v-model="selectedTools" type="checkbox" name="WazuhIndexer" id="WazuhIndexer" value="wazuhIndexer"> Wazuh Indexer 
                    <p class="tool-info">A vital part of the Wazuh platform, the Wazuh Indexer handles indexing and querying of security data. It forms the cornerstone for effective threat detection and response strategies. <a href="https://documentation.wazuh.com/current/installation-guide/wazuh-indexer/index.html">Read more</a></p> 
                    <img src=" static/wazuhindexer.png" alt="Wazuh Logo"> 
                    </label></div> 
                
                    <div class="tool"><label for="Elasticsearch"> 
                    <input v-model="selectedTools" type="checkbox" name="Elasticsearch" id="Elasticsearch" value="elasticsearch"> Elasticsearch 
                    <p class="tool-info">ElasticSearch, a distributed search and analytics engine, excels in storing and searching large data volumes. Its commonly utilized in ELK (Elasticsearch, Logstash, Kibana) stacks for diverse use cases <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html">Read more</a></p> 
                    <img src=" static/elasticsearch.png " alt="Wazuh Logo"> 
                    </label></div>
                    
                    <div class="tool"><label for="Apache"> 
                    <input v-model="selectedTools" type="checkbox" name="Apache" id="Apache" value="apache_cassandra"> Apache Cassandra 
                    <p class="tool-info">Apache Cassandra is a highly scalable NoSQL database, ideal for managing extensive data volumes. Its focus on high availability and fault tolerance makes it an excellent choice for organizations. <a href="https://cassandra.apache.org/doc/latest/">Read more</a></p> 
                    <img src="static/apache.png" alt="Wazuh Logo"> 
                    </label></div>
                </div> 
            </section><hr>
            <section id="V">
                <h1  class="">Visualization</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
            <section class="shadow-inner" id="IE">
                <h1  class="">Intelligent Enrichment</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
            <section class="shadow-inner" id="TDP">
                <h1  class="">Tread Detection And Prevention</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
            <section class="shadow-inner" id="CM">
                <h1 class="">Case Management</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
            <section class="shadow-inner" id="ATO">
                <h1 class="">Log Automate</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
            <section class="shadow-inner" id="INV">
                <h1 class="">Investigation</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
            <section  class="shadow-inner" id="HM">
                <h1 class="">Health Monitoring</h1>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                    
                </div> 
            </section><hr>
        </div>
        </div>
    </div>

    <!-- Modal -->
<div id="modal" v-show="isModalVisible"  tabindex="-1" class="fixed top-0 left-0 right-0 bottom-0 
  z-50 flex  justify-center  p-4 overflow-x-hidden overflow-y-auto md:inset-0">
    <div class="relative w-[700px] ">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
            <button @click="toggleModal" type="button" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="popup-modal">
                <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                </svg>
                <span class="sr-only">Close modal</span>
            </button>
            <div class="p-6 ">
                <h3 class="mb-5 text-lg font-normal text-black dark:text-gray-400"> You have selected thease tools to install, if you are sure please click to proceed. </h3>
                <div class=" mb-6" v-for="(tools, index) in selectedTools" :key="index">
                    <div class="grid grid-cols-2 md:grid-cols-3 gap-4 shadow-md">
                        <div class="text-gray-500 dark:text-gray-400">
                            {{ tools }}
                        </div>
                        
                      </div>
                  
              </div>
              <button @click.prevent="triggerPipeline"
                      class=" py-2.5 px-4 text-xs font-medium text-center text-blsck bg-black text-white mr-2 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                      Proceed
              </button>
              <button @click="toggleModal" type="button" class="py-2.5 px-4 text-xs font-medium text-center text-blsck bg-red-600 rounded-lg focus:ring-4 focus:ring-primary-200 dark:focus:ring-primary-900 hover:bg-primary-800">
                Cancle
            </button>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default{
    data() {
    return {
      selectedTools: [], 
      isModalVisible: false,
      userMenuVisible: false,
    };
  },
  methods: {
    toggleUserMenu(){
      console.log("Hii");
      this.userMenuVisible = !this.userMenuVisible
    },
    toggleModal() {
            this.isModalVisible = !this.isModalVisible;
    },
    triggerPipeline(){
      const data  = this.selectedTools
      console.log(data);
      axios.post('http://127.0.0.1:8000/api/v2/trigger/', data)
      .then((respons)=>{
         console.log(respons.data)
         this.push
      })
      this.isModalVisible = !this.isModalVisible;
    },
    logout(){
      console.log("logout");
      sessionStorage.removeItem('user_id');
      sessionStorage.removeItem('username');
      window.location.reload()
    },
  }
}

document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);

        if (targetSection) {
            const offsetTop = targetSection.offsetTop;
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Activate sections on scroll
function activateSections() {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top >= 0 && rect.top <= window.innerHeight) {
            if (section.classList) {
                section.classList.add('active');
            }
        } else {
            if (section.classList) {
                section.classList.remove('active');
            }
        }
    });
}


// Display Home section by default
document.addEventListener('DOMContentLoaded', () => {
    const homeSection = document.getElementById('HM');
    homeSection.classList.add('active');
});

document.addEventListener('scroll', activateSections);
</script>

<style scoped> 
/* Style the sections */
section {
    margin-top: 80px;
    padding-top: 100px;
    text-align: center;
    height: 100vh;
}

section h1 {
    font-size: 36px;
    margin-bottom: 20px;
}

/* Add animations */
section {
    opacity: 0;
    transform: translateY(5px);
    transition: opacity 0.6s ease, transform 0.6s ease;
}

section.active {
    opacity: 1;
    transform: translateY(0);
}

.tool_img{
    max-width: 100px;
    max-height: 100px;
    margin-left: 10px;
}
.tool{
    padding: 28px;
}
</style>