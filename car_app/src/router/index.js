import Vue from 'vue'
import Router from 'vue-router'
import Screensaver from '@/pages/Screensaver'
import Dashboard from '@/pages/Dashboard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Screensaver',
      component: Screensaver
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    }
  ]
})
