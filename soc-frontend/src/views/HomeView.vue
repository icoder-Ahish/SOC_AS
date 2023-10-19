<template>
<leftSidebar/>

<div class="p-4 sm:ml-64">
   <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-20"> 
      <div class="flex items-center justify-center h-48 mb-4 rounded bg-gray-50 dark:bg-gray-800">
               <h1 class=" dark:text-white"> Welcome to the SOC Dashboard </h1>
      </div>  
   </div>
</div>


</template>

<script>
import leftSidebar from '../components/leftSidebar.vue';

export default{
   components:{
      leftSidebar
   }
}
</script>