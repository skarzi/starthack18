<template>
  <div class="dashboard-view">
    <div class="location-input">
      <vue-google-autocomplete
        id="autocomplete"
        classname="form-control"
        placeholder="Hi Mark, where to?"
        v-on:placechanged="handleDestination"
        country="ch"
      >
      </vue-google-autocomplete>
      <div class="fast-forward-button" v-if="destination">
        <v-icon x-large>fast_forward</v-icon>
      </div>
    </div>
    <div id="map-container">
    </div>
    <div class="driving-panel" :class="{visible: !!destination}">
      <points-meter :score="3.5"></points-meter>
      <div class="notifications-panel">
        <div class="panel-header" @click="togglePanel"></div>
        <div class="panel-content" :class="{open: panelOpen}"></div>
      </div>
    </div>
  </div>
</template>

<script>
  import VueGoogleAutocomplete from 'vue-google-autocomplete'
  import PointsMeter from '../components/PointsMeter.vue'

  export default {
    components: {
      VueGoogleAutocomplete,
      PointsMeter
    },
    data () {
      return {
        map: null,
        destination: undefined,
        panelOpen: false,
        carPosition: {
          lat: 47.432421,
          lng: 9.374877
        }
      }
    },
    mounted () {
      this.map = new GMaps({
        div: '#map-container',
        lat: this.carPosition.lat,
        lng: this.carPosition.lng,
        zoom: 16,
        disableDefaultUI: true
      })
      this.map.addMarker({
        lat: this.carPosition.lat,
        lng: this.carPosition.lng,
        icon: 'https://i.imgur.com/jzJxuAI.png'
      })
    },
    methods: {
      togglePanel () {
        this.panelOpen = !this.panelOpen
      },
      handleDestination (address, place, id) {
        document.getElementById('autocomplete').value = 'Heading to ' + place.formatted_address
        this.destination = place
        this.map.addMarker({
          lat: place.geometry.location.lat(),
          lng: place.geometry.location.lng(),
          icon: 'https://i.imgur.com/PcUFEPo.png'
        })
        this.map.cleanRoute()
        this.map.drawRoute({
          origin: [this.carPosition.lat, this.carPosition.lng],
          destination: [place.geometry.location.lat(), place.geometry.location.lng()],
          travelMode: 'driving',
          strokeColor: '#131540',
          strokeOpacity: 0.6,
          strokeWeight: 6
        })
      }
    }
  }
</script>

<style lang="scss">

  .pac-container {
    left: 30px !important;
    top: 148px !important;
    z-index: 9999 !important;
  }

  .dashboard-view {
    position: relative;
  }

  #map-container {
    width: 100vw;
    height: 100vh;
  }

  .location-input {
    position: absolute;
    z-index: 9999;
    background-color: #fff;
    top: 100px;
    left: 30px;
    font-size: 24px;
    padding: 10px;
    padding-left: 25px;
    width: 500px;
    text-align: left;
    box-shadow: 0 3px 1px -2px rgba(0, 0, 0, .2), 0 2px 2px 0 rgba(0, 0, 0, .14), 0 1px 5px 0 rgba(0, 0, 0, .12);

    input {
      width: 100%;
    }
  }

  .fast-forward-button {
    position: absolute;
    left: 0;
    top: calc(100% + 5px);
    text-shadow: 2px 2px #ccc;
    color: #fff;
  }

  .driving-panel {
    position: absolute;
    width: calc(100% - 60px);
    left: 30px;
    bottom: 0;
    opacity: 0;
    transition: opacity 1s linear;

    &.visible {
      opacity: 1;
    }
  }

  .notifications-panel {
    background-color: #fff;
    box-shadow: 0 -5px 20px 0px rgba(0, 0, 0, .2), 0 2px 2px 0 rgba(0, 0, 0, .14), 0 1px 5px 0 rgba(0, 0, 0, .12);
    margin-top: 40px;

    .panel-header {
      height: 40px;
      position: relative;
      &:after {
        content: ' ';
        display: block;
        position: absolute;
        left: 50%;
        top: 0;
        transform: translate(-50%, -50%);
        width: 60px;
        height: 60px;
        background-image: url('../assets/volvo.png');
        background-size: auto 60px;
        background-position: center 0;
      }
    }

    .panel-content {
      transition: height 0.3s linear;
      height: 0;

      &.open {
        height: 260px;
      }
    }
  }
</style>
