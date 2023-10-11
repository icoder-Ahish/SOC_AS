<template>
  <div class="btnclass">
    <button @click="triggerPipeline" class="bg-slate-500 mt-10 btn rounded-2xl p-4 ">Trigger Pipeline</button>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  methods:{
    triggerPipeline(){
      const data = {
        "tool" : "filebit"
      }
      axios.post('http://127.0.0.1:8000/api/v2/trigger/', data)
    }
  }
}
</script>

<style>
.btnclass{

  position: relative;
  left: 50%;
  right: 50%;

}
</style>