<template>
  <div style="text-align: center;" v-if="user">
    <NavBar/>
    <div> <h3><strong> Home Page </strong></h3></div>
    <WelcomeCpp/>
    <AddCoin @added="change"/>
    <ProfitDisplay :key="refreshComp"/>
    <Logout/>
  </div>
</template>

<script>
import WelcomeCpp from '../components/WelcomeCpp.vue'
import AddCoin from '../components/AddCoin.vue'
import ProfitDisplay from '../components/ProfitDisplay.vue'
import NavBar from '../components/NavBar.vue'
import Logout from '../components/LogOut.vue'
import { getAuth, onAuthStateChanged } from 'firebase/auth';

export default {
  name: 'HomeView',
  components: {
    WelcomeCpp,
    AddCoin,
    ProfitDisplay,
    NavBar,
    Logout,
  },
data() {
  return {
    refreshComp:0,
    user: false,
  }
}, 
methods: {
  change() {
    this.refreshComp += 1
  }
},
   mounted() {
        const auth = getAuth();
        onAuthStateChanged(auth, (user) => {
        if (user) {
            this.user = user;
        }
        })
    }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
