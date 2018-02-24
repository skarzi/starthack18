<template>
  <div class="map-container">
    <GoogleMap/>
  </div>
</template>
<script>
import GoogleMap from '../components/GoogleMap'

export default {
  components: {
    GoogleMap: GoogleMap
  }
}
</script>
<style>
  .map-container {
    height: 100%;
    witdth: 100%;
  }
</style>
