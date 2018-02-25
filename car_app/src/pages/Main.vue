<template>
  <div class='main-container'>
    <GoogleMap class='google-map'/>
    <div class="google-search-input-container">
      <GoogleSearchInput class="google-search-input"/>
    </div>
    <div class="bottom-components">
      <p :style="'color: ' +  color + ';'">{{rank / 10}}</p>
      <v-progress-linear v-model="rank" height="20" :color="color"
                         buffer-value="50"
      ></v-progress-linear>
      <div class="info-window">
      </div>
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
  },
  data () {
    return {
      rank: 1.2,
      color: 'primary'
    }
  },
  methods: {
    updateRank (points) {
      this.rank += points
    }
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
  .bottom-components {
    position: absolute;
    bottom: 75px;
    right: 65%;
    left: 50px;
    z-index: 100;
  }
</style>
