import Vue from 'vue'
import Router from 'vue-router'
import Entry from '../pages/Entry'
import Main from '../pages/Main'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Entry',
      component: Entry
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    }
  ]
})

export default router
