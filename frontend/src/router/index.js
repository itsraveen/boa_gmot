import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import ProfileView from '@/views/ProfileView.vue'
import OnlyProfit from '@/views/OnlyProfit.vue'
import NotFound from '@/views/NotFound.vue'
import Login from '@/components/Login.vue'

const routes = [
    {
      path: '/',
      name: 'Login',
      component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: HomeView
},
  {
      path: '/about',
      name: 'About',
      component: AboutView
  },
  {
      path: '/profile',
      name: 'Profile',
      component: ProfileView
  },
  {
      path: '/profit',
      name: 'Profit Page',
      component: OnlyProfit
  },
  {
      path: '/:catchAll(.*)',
      name: "NotFound",
      component: NotFound
  }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;