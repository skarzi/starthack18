<template>
  <div class='main-container'>
    <GoogleMap class='google-map'/>
    <div class="google-search-input-container">
      <GoogleSearchInput class="google-search-input"/>
    </div>
  </div>
</template>
<script>
import GoogleMap from '../components/GoogleMap'
import GoogleSearchInput from '../components/GoogleSearchInput'

export default {
  components: {
    GoogleMap: GoogleMap,
    GoogleSearchInput: GoogleSearchInput
  }
}
</script>
<style>
  .main-container {
    height: 100%;
    width: 100%;
    position: relative;
  }
  .google-search-input-container {
    position: absolute;
    background: white;
    top: 75px;
    right: 65%;
    left: 50px;
    z-index: 99;
  }
  .google-search-input {
    width: 85%;
    left: 20px;
  }
</style>
