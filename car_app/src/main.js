// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App'
import router from './router'
import store from './store'
import * as VueGoogleMaps from 'vue2-google-maps'

import 'vuetify/dist/vuetify.min.css'

Vue.config.productionTip = false
Vue.config.GOOGLE_MAPS_API_KEY = 'AIzaSyAQ_7Z1Qln1f9D70cyDKEPG4_t31kUOdrQ '
Vue.use(Vuetify)
Vue.use(VueGoogleMaps, {
  load: {
    key: Vue.config.GOOGLE_MAPS_API_KEY,
    libraries: 'places' // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
