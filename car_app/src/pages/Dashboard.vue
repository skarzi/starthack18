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
      <div class="fast-forward-button" v-if="destination" @click="progress">
        <v-icon x-large>fast_forward</v-icon>
      </div>
    </div>
    <div id="map-container">
    </div>
    <div class="driving-panel" :class="{visible: !!destination}">
      <points-meter :score="score"></points-meter>
      <div class="notifications-panel">
        <div class="panel-header" @click="togglePanel"></div>
        <div class="panel-content" :class="{open: panelOpen}">
          <div class="close-panel-button" @click="togglePanel">
            <img src="../assets/close.png">
          </div>
          <hello v-if="demoProgress===0"></hello>
          <checkpoint-nearby v-if="demoProgress===1"
                             @progress="progress"></checkpoint-nearby>
          <on-checkpoint v-if="demoProgress===2"></on-checkpoint>
          <payment-confirmed v-if="demoProgress===3"></payment-confirmed>
          <magical-encounter v-if="demoProgress===4"></magical-encounter>
          <aggressive-accelerating
            v-if="demoProgress===5"></aggressive-accelerating>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import VueGoogleAutocomplete from 'vue-google-autocomplete'
  import PointsMeter from '../components/PointsMeter.vue'

  import Hello from '../components/cards/Hello.vue'
  import CheckpointNearby from '../components/cards/CheckpointNearby.vue'
  import OnCheckpoint from '../components/cards/OnCheckpoint.vue'
  import PaymentConfirmed from '../components/cards/PaymentConfirmed.vue'
  import MagicalEncounter from '../components/cards/MagicalEncounter.vue'
  import AggressiveAccelerating from '../components/cards/AggressiveAccelerating.vue'

  export default {
    components: {
      VueGoogleAutocomplete,
      PointsMeter,
      Hello,
      CheckpointNearby,
      OnCheckpoint,
      PaymentConfirmed,
      MagicalEncounter,
      AggressiveAccelerating
    },
    data () {
      return {
        map: null,
        destination: undefined,
        panelOpen: false,
        carPosition: {
          lat: 47.432421,
          lng: 9.374877
        },
        demoProgress: 0,
        score: 4,
        points: []
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
    watch: {
      demoProgress (value) {
        if (value === 3) {
          this.score = 4.9
        } else if (value === 4) {
          this.score = 4.95
        } else if (value === 5) {
          this.score = 4.9
        }
      }
    },
    methods: {
      togglePanel () {
        this.panelOpen = !this.panelOpen
      },
      handleDestination (address, place, id) {
        document.getElementById('autocomplete').value = 'Heading to ' + place.formatted_address
        this.destination = place
        this.map.getRoutes({
          origin: [this.carPosition.lat, this.carPosition.lng],
          destination: [place.geometry.location.lat(), place.geometry.location.lng()],
          travelMode: 'driving',
          provideRouteAlternatives: false,
          callback: (data) => {
            console.log(data)
            this.points = data[0].legs[0].steps.map(step => {
              return {
                lat: step.end_point.lat(),
                lng: step.end_point.lng()
              }
            })
            console.log(this.points)
          }
        })
        this.reloadMap()
        setTimeout(() => {
          this.panelOpen = true
        }, 1200)
      },
      progress () {
        this.demoProgress += 1
        if (this.demoProgress <= 5) {
          this.panelOpen = true
        }
        this.carPosition = this.points.shift()
        this.reloadMap()
      },
      reloadMap () {
        this.map.removeMarkers()
        this.map.cleanRoute()
        this.map.addMarker({
          lat: this.carPosition.lat,
          lng: this.carPosition.lng,
          icon: 'https://i.imgur.com/jzJxuAI.png'
        })
        this.map.setCenter({
          lat: this.carPosition.lat,
          lng: this.carPosition.lng
        })
        this.map.addMarker({
          lat: this.destination.geometry.location.lat(),
          lng: this.destination.geometry.location.lng(),
          icon: 'https://i.imgur.com/PcUFEPo.png'
        })
        this.map.drawRoute({
          origin: [this.carPosition.lat, this.carPosition.lng],
          destination: [this.destination.geometry.location.lat(), this.destination.geometry.location.lng()],
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

  @font-face {
    font-family: "Bodoni";
    src: url("../assets/Bodoni.ttf");
  }

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
      position: relative;
      overflow: hidden;

      &.open {
        height: 240px;
      }

      .close-panel-button {
        position: absolute;
        top: 0;
        left: 20px;
      }

      p.header {
        font-family: 'Bodoni', serif;
        font-size: 24px;
      }

      p.regular {
        font-size: 24px;

      }

      .card-content {
        padding-top: 20px;
      }

      hr.divider {
        width: 500px;
        margin: 20px auto;
      }

      .star-icon {
        height: 30px;
        vertical-align: -8px;
      }
    }
  }
</style>
