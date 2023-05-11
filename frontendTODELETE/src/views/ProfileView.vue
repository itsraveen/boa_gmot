<template>
  <div style="text-align: center;" v-if="user">
    <NavBar/>
    <div> <h3><strong> Profile page </strong></h3></div>
    <div v-if="user">
      <div> <img src="@/assets/logo.png" style="width:75px;height=75px;border-radius:30%;border:2px solid #333;">
      </div>
    <div> 
      <p> 
      Name: <strong> {{user.displayName}} </strong><br>
      Email: <strong>{{user.email}}</strong><br>
      Uid: <strong>{{user.uid}}</strong><br>
      Provider: <strong>{{user.providerData[0].providerId}}</strong>
      </p>
      </div>
  </div>
  <Logout/>
  </div>
</template>

<script>
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import NavBar from '../components/NavBar.vue'
import Logout from '../components/LogOut.vue'

export default {
  name : "ProfileView",
  components: {
    NavBar,
    Logout,
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
        console.log(user)
        })
    }
    
}
</script>

<style>

</style>