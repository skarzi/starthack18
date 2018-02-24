// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

Vue.config.productionTip = false
Vue.config.GOOGLE_MAPS_API_KEY = 'AIzaSyAQ_7Z1Qln1f9D70cyDKEPG4_t31kUOdrQ '

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
