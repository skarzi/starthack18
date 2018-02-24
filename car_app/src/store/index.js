import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

function _isValidPlace (place) {
  return (
    'id' in place && 'lat' in place &&
    'ltg' in place && 'formated_address' in place
  )
}

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
      console.log('GEOLOCATION ERROR!')
    })
  }
  return location
}

export default new Vuex.Store({
  state: {
    _selectedPlace: _getCurrentLocation(),
    _markers: []
  },
  mutations: {
    addMarker (state, marker) {
      state._markers.push(marker)
    },
    removeMarker (state, index) {
      state._markers.splice(index, 1)
    },
    clearMarkers (state) {
      state._markers = []
    },
    updateMarkers (state, newMarkers) {
      state._markers = newMarkers
    },
    updatePlace (state, place) {
      if (_isValidPlace(place)) {
        state._selectedPlace = place
      }
      return state._selectedPlace
    }
  },
  getters: {
    getMarkers: function (state) {
      return state._markers
    },
    getSelectedPlace: function (state) {
      if (state._selectedPlace === undefined) {
        state._selectedPlace = _getCurrentLocation()
      }
      return state._selectedPlace
    }
  }
})
