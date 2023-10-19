<template>
    <leftSidebar></leftSidebar>
    <div class="p-4 sm:ml-64">
        <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-20" >   
           <div class="flex items-center justify-center h-auto mb-4 m-10 rounded bg-gray-50 dark:bg-gray-800">
                  
                    <iframe
                    width="1000"
                    height="1000"
                    :src="embedUrl"
                    frameborder="0"
                    allowfullscreen class="m-5"
                ></iframe>
           </div>   
        </div>
     </div>
  
    </template>
    

     
    
    <script>
    import leftSidebar from './leftSidebar.vue'


    export default {
    components:{
      leftSidebar,
    },
      computed: {
        embedUrl() {
          return `https://documentation.wazuh.com/current/user-manual/ruleset/index.html`;
        },
      },
    };
    </script>
    
     
    
    <style scoped>
    .youtube-player {
      text-align: center;
    }
    </style>