<template>
 <div style="text-align: center;" v-if="user">
    <NavBar/>
      <h2> Page Not Found </h2>
      <h4> Please click on the available options. </h4>
    <LogOut /> 
  </div> 
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import LogOut from '@/components/LogOut.vue'

export default {
    name: "NotFound",
    components: {
        NavBar,
        LogOut
  }

}
</script>

<style>

</style>