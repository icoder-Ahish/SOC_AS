<template>
<leftSidebar/>
<div class="p-4 sm:ml-64">
    <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700 mt-20" >   
       <div class="items-center p-4 justify-center h-auto  m-10 rounded bg-gray-50 dark:bg-gray-800">

        <h1 class="items-center text-gray-800 dark:text-white text-xl font-bold"> Choose Your Rules</h1>
        <div class="flex items-center m-4">
            <input id="default-checkbox" v-model="selectedRules" type="checkbox" value="rule-1" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
            <label for="default-checkbox" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                Alert When user created and deleted within 60 min.
            </label>
        </div>
        <div class="flex items-center m-4">
            <input  id="-checkbox" v-model="selectedRules" type="checkbox" value="rule-2" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
            <label for="-checkbox" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                File Changes Detections
            </label>
        </div>
        <div class="flex items-center m-4">
            <input  id="-checkbox" v-model="selectedRules" type="checkbox" value="rule-3" class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
            <label for="-checkbox" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">
                Unauthorised Login Protections
            </label>
        </div>
    
        <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-700">
        <button v-if="selectedRules.length > 0" class="flex  items-center  bg-gray-800 hover:bg-gray-600 dark:bg-gray-900 text-white font-semibold px-4 py-2 rounded-lg ">
            Apply
          </button>
       </div>   
    </div>
 </div>
</template>

<script>
import leftSidebar from './leftSidebar.vue';

export default {
    components:{
      leftSidebar,
    },
    data(){
        return{
            selectedRules: []
        }
    }
}

</script>