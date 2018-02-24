<template>
  <gmap-autocomplete :value="currentCity"
    @place_changed="setPlace">
  </gmap-autocomplete>
</template>
<script>
import {mapMutations, mapGetters} from 'vuex'

export default {
  name: 'GAutocomplete',
  computed: {
    ...mapGetters({
      selectedPlace: 'getSelectedPlace'
    }),
    currentCity () {
      return this.selectedPlace['formatted_address']
    }
  },
  methods: {
    ...mapMutations([
      'updatePlace'
    ]),
    setPlace (place) {
      console.log(place)
      this.updatePlace(place)
    }
  }
}
</script>
<style>
</style>
