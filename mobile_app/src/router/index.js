import Vue from 'vue'
import Router from 'vue-router'
import Entry from '@/pages/Entry'
import Register from '@/pages/Register'
import Signin from '@/pages/Signin'
import Dashboard from '@/pages/Dashboard'
import Scan from '@/pages/Scan'
import Driving from '@/pages/Driving'
import Leaderboard from '@/pages/Leaderboard'
import Payment from '@/pages/Payment'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Entry',
      component: Entry
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/signin',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/scan',
      name: 'Scan',
      component: Scan
    },
    {
      path: '/driving',
      name: 'Driving',
      component: Driving
    },
    {
      path: '/leaderboard',
      name: 'Leaderboard',
      component: Leaderboard
    },
    {
      path: '/payment',
      name: 'Payment',
      component: Payment
    }
  ]
})
