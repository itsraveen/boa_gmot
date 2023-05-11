import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'

//import WelcomeCpp from './components/WelcomeCpp.vue' //import component
//import AddCoin from './components/AddCoin.vue'
//import ProfitDisplay from './components/ProfitDisplay.vue'

//const app = createApp(App)
//app.component('WelcomeCpp', WelcomeCpp) //register
//app.component('AddCoin', AddCoin) 
//app.component('ProfitDisplay', ProfitDisplay) 
//app.use(router).mount('#app')

createApp(App).use(router).mount('#app')
