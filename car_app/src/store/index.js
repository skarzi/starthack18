import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

var USER_ICON = 'https://i.imgur.com/jzJxuAI.png'

function _isValidPlace (place) {
  return (
    'geometry' in place && 'formatted_address' in place
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
    })
  }
  return location
}

function _getMarkers (userLocation) {
  // TODO: fetch car markers from IP.
  var markers = []
  if (userLocation) {
    markers.push({
      position: {lat: userLocation.lat, lng: userLocation.lng},
      type: 'user',
      icon: USER_ICON
    })
  }
  return markers
}

function _findMarkerIndexByType (markers, type) {
  for (var i = 0; i < markers.length; i += 1) {
    if (markers[i]['type'] === type) {
      return i
    }
  }
  return -1
}

export default new Vuex.Store({
  state: {
    _selectedPlace: _getCurrentLocation(),
    _markers: _getMarkers(_getCurrentLocation())
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
        var markerIndex = _findMarkerIndexByType(
          state._markers,
          'user'
        )
        if (markerIndex >= 0) {
          state._markers.splice(markerIndex, 1)
        }
        state._selectedPlace = {
          lat: place.geometry.location.lat(),
          lng: place.geometry.location.lng(),
          formatted_address: place.formatted_address,
          id: place.id
        }
        state._markers.push({
          position: {
            lat: place.geometry.location.lat(),
            lng: place.geometry.location.lng()
          },
          type: 'user',
          icon: USER_ICON
        })
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
        state._selectedPlace = _getCurrentLocation(false, null)
      }
      return state._selectedPlace
    }
  }
})
