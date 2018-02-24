import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

function _getCurrentLocation () {
  var location = {
    'lat': 47.4244818,
    'lng': 9.376717299999996,
    'id': '0',
    'formatted_address': 'Your Location'
  }
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      location = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
        'id': '0',
        'formatted_address': 'Your Location'
      }
    }, function () {
      alert('GEO LOCATION ERROR')
    })
  }
  return location
}

export default new Vuex.Store({
  state: {
    _cars: [],
    _map: undefined,
    _source: _getCurrentLocation(),
    _target: undefined
  },
  getters: {
    getMap (state) {
      return state._map
    },
    getSource (state) {
      return state._source
    },
    getTarget (state) {
      return state._target
    }
  },
  mutations: {
    setMap (state, newMap) {
      state._map = newMap
    },
    createMarkers (state) {
      var markers = []
      markers.push({
        lat: state._source.lat,
        lng: state._source.lng,
        title: state._source.formatted_address,
        icon: state._source.icon
      })
      if (state._target) {
        markers.push({
          lat: state._target.lat,
          lng: state._target.lng,
          title: state.formatted_address,
          icon: state._target.icon
        })
      }
      for (var i = 0; i < state._cars.length; i += 1) {
        var car = state._cars[i]
        markers.push({
          lat: car.lat,
          lng: car.lng,
          icon: car.icon,
          title: car.model,
          click: function (e) {
            alert('Hello World!')
          }
        })
      }
      state._map.addMarkers(markers)
    },
    clearMarkers (state) {
      state._map.removeMarkers()
    },
    updateMarkers (state, newMarkers) {
      state._markers = newMarkers
    },
    updateTargetLocation (state, newLocation) {
      state._target = newLocation
    }
  }
})
