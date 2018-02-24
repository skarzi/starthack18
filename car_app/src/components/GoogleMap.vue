<template>
  <div id="map" style="height: 400px; width: 100%">
  </div>
</template>
<script>
import { mapGetters, mapMutations } from 'vuex'

export default {
  name: 'GoogleMap',
  data () {
    return {
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
      createMarkers: 'createMarkers'
    })
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
