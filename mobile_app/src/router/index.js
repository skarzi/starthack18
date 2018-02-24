import Vue from 'vue'
import Router from 'vue-router'
import Entry from '@/pages/Entry'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Entry',
      component: Entry
    }
  ]
})
