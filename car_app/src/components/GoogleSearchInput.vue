<template>
  <vuetify-google-autocomplete
    id="map-auto"
    :load-google-api="false"
    name="destination"
    :label="'Hi ' + user.name + '. Where to?'"
    single-line
    prepend-icon="search"
    clearable
    color="magenta"
    v-model="target.formatted_address"
    v-on:placechanged="getPlaceData"
  ></vuetify-google-autocomplete>
</template>
<script>
import { mapGetters, mapMutations } from 'vuex'

const TARGET_ICON = ''

export default {

  name: 'GoogleSearchInput',
  data () {
    return {
      user: { 'name': 'Mark' }
    }
  },
  computed: {
    ...mapGetters({
      target: 'getTarget'
    })
  },
  methods: {
    ...mapMutations({
      updateTargetLocation: 'updateTargetLocation'
    }),
    getPlaceData (address, place) {
      this.updateTargetLocation({
        formatted_address: place.formatted_address,
        lat: place.geometry.location.lat,
        lng: place.geometry.location.lng,
        icon: TARGET_ICON
      })
    }
  }
}
</script>
<style>
</style>
