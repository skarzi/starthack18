import Vue from 'vue'
import Router from 'vue-router'
import GoogleMap from '../components/GoogleMap'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'GoogleMap',
      component: GoogleMap
    }
  ]
})

export default router
