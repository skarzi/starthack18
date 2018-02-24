<template>
  <div id="map" style="height: 400px; width: 100%">
  </div>
</template>
<script>
import { mapGetters, mapMutations } from 'vuex'
import axios from 'axios'

export default {
  name: 'GoogleMap',
  data () {
    return {
      cars: []
    }
  },
  computed: {
    ...mapGetters({
      map: 'getMap',
      source: 'getSource'
    })
  },
  methods: {
    ...mapMutations({
      setMap: 'setMap',
      setCars: 'setCars',
      createMarkers: 'createMarkers'
    }),
    getCars: function () {
      axios.get('/cars/').then(res => {
        var data = res.data
        var cars = []
        for (let car of data) {
          var latlng = data.location.split(',').map(x => parseFloat(x))
          cars.push({
            'lat': latlng[0],
            'lng': latlng[1],
            'state': car['state'],
            'model': car['model'],
            'icon': car['icon']
          })
        }
        return cars
      })
    }
  },
  mounted: function () {
    this.setMap(new GMaps({
      div: '#map',
      lat: this.source['lat'],
      lng: this.source['lng']
    }))
    this.createMarkers()
  }
}
</script>
<style>
</style>
