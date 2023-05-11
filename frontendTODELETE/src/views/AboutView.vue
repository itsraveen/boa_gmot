<template>
  <div style="text-align: center;" v-if="user">
    <NavBar/>
      <h1> About Page </h1>
      <h2> Welcome to CPP! </h2>
      <p> CPP is an app to track your crypto portfolio. </p>
    <LogOut /> <br>
  </div> 
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import LogOut from '@/components/LogOut.vue'
import { getAuth, onAuthStateChanged } from '@firebase/auth';

export default {
  name : "AboutView",

  components: {
    NavBar,
    LogOut
  },
   
  data() {
    return {
      user: false,
      }
      },

    mounted() {
      const auth = getAuth();
      onAuthStateChanged(auth, (user) => {
      if (user) {
        this.user = user;
      }
      })
  },
}
</script>

<style>

</style>