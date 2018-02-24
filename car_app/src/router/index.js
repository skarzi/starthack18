import Vue from 'vue'
import Router from 'vue-router'
import Entry from '../pages/Entry'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Entry',
      component: Entry
    }
  ]
})

export default router
