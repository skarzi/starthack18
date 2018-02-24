import Vue from 'vue'
import Router from 'vue-router'
import Entry from '@/pages/Entry'
import Register from '@/pages/Register'

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
    }
  ]
})
