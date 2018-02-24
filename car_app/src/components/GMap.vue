<template>
  <div class="hello">
      <g-autocomplete/>
      <hr>
      <gmap-map
        :center="this.currentLatLng"
        :zoom="7"
        map-type-id="terrain"
        class="map"
        style="width: 100%; height: 500px"
    >
    <gmap-marker v-for="(m, index) in markers" :position="m.position"
                   :clickable="true" :draggable="false"
                   @click="onMarkerClick(m, index)" :icon="m.icon"
                   :key="'marker_' + index">
    </gmap-marker>
    </gmap-map>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

import GAutocomplete from './GAutocomplete'

export default {
  name: 'GMap',
  data () {
    return {
      msg: 'Welcome to Your Vue.js PWA'
    }
  },
  components: {
    GAutocomplete: GAutocomplete
  },
  methods: {
    onMarkerClick () {
      alert('hehe')
    }
  },
  computed: {
    ...mapGetters({
      selectedPlace: 'getSelectedPlace',
      markers: 'getMarkers'
    }),
    currentLatLng () {
      return {
        lat: this.selectedPlace['lat'],
        lng: this.selectedPlace['lng']
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #35495E;
}

map {
}
</style>
