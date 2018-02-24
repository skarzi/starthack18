import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    reservedCar: undefined
  },
  mutations: {
    reserveCar (state, car) {
      state.reservedCar = car
    },

    cancelReservation (state) {
      state.reservedCar = undefined
    }
  }
})
