// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'

import axios from 'axios'
import Vuetify from 'vuetify'
import qs from 'qs'
import 'vuetify/dist/vuetify.min.css' // Ensure you are using css-loader

axios.defaults.baseURL = 'http://130.82.238.4'
axios.defaults.paramsSerializer = function (params) {
  return qs.stringify(params, {indices: false})
}

Vue.use(Vuetify)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
