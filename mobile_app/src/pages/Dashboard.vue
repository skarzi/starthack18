<template>
  <div class="dashboard-view">
    <v-toolbar dark class="dashboard-toolbar" extended>
      <div class="dashboard-background">
      </div>
      <v-layout row wrap class="status-bar">
        <v-flex xs4 class="active">
          Search
        </v-flex>
        <v-flex xs4>
          Drive
        </v-flex>
        <v-flex xs4>
          Finish
        </v-flex>
        <div class="status-indicator"></div>
      </v-layout>
    </v-toolbar>
    <div id="map-container">

    </div>
    <v-slide-y-reverse-transition>
      <div class="selected-car" v-if="chosenCar || reservedCar">
        <img :src="chosenCar.icon + '?w=100'">
        <p class="car-name">{{ chosenCar.model }}</p>
        <p class="car-capacity">
          <v-icon size="10px">person</v-icon>
          Max. 5
        </p>
        <v-divider color="lightgray"></v-divider>
        <div class="credit-card-info">
          <p v-if="!reservedCar">
            <img src="../assets/mastercard.png"> ⋯ 7638
          </p>
          <p v-else>
            The car will be reserved for 10 minutes.
          </p>
        </div>
        <v-btn class="action-button confirm-button" @click="reserveCar"
               v-if="!reservedCar">
          Confirm
        </v-btn>
        <div class="action-buttons" v-else>
          <v-btn class="action-button cancel-button" @click="cancelReservation">
            Cancel
          </v-btn>
          <v-btn class="action-button scan-button">
            Scan QR Code
          </v-btn>
        </div>
      </div>
    </v-slide-y-reverse-transition>
  </div>
</template>

<script>
  import axios from 'axios'
  import store from '../store'

  export default {
    data () {
      return {
        map: null,
        cars: [],
        chosenCar: undefined
      }
    },
    computed: {
      reservedCar () {
        return store.state.reservedCar
      }
    },
    mounted () {
      this.map = new GMaps({
        div: '#map-container',
        lat: 47.432421,
        lng: 9.374877,
        zoom: 16,
        disableDefaultUI: true,
        click: e => {
          this.chosenCar = undefined
        }
      })
      this.map.addMarker({
        lat: 47.432421,
        lng: 9.374877,
        icon: 'http://www.myiconfinder.com/uploads/iconsets/32-32-bd14ef53b2e3d822094dbd064b9b206b-compas.png'
      })
      axios.get('/cars/').then(resp => {
        this.cars = resp.data
        this.drawCars()
      })
    },
    methods: {
      drawCars () {
        this.cars.forEach(car => {
          console.log(car)
          this.map.addMarker({
            lat: car.location.split(',')[0],
            lng: car.location.split(',')[1],
            icon: car.icon + '?w=50',
            click: e => {
              if (!this.reservedCar) {
                this.chosenCar = car
              }
            }
          })
        })
      },

      reserveCar () {
        store.commit('reserveCar', this.chosenCar)
      },

      cancelReservation () {
        store.commit('cancelReservation')
      }
    }
  }
</script>

<style lang="scss">

  .dashboard-view {
    position: relative;
  }

  #map-container {
    height: calc(100vh - 112px);
  }

  .dashboard-background {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-size: 100% auto;
    opacity: 0.2;
    background-image: url('../assets/pattern.png');
    margin: 0 !important;
  }

  .dashboard-toolbar {
    position: relative;
    background-color: #151E3F;
    background-image: url('../assets/volvo.png');
    background-size: auto 44px;
    background-position: center 15px;
    z-index: 9999;
    box-shadow: none;
  }

  .status-bar {
    position: absolute;
    height: 40px;
    bottom: 0;
    left: 0;
    right: 0;
    margin: 0 !important;
    text-align: center;
    text-transform: uppercase;
    line-height: 40px;

    .flex {
      color: #666;
    }

    .flex.active {
      color: #fff;
    }

    .status-indicator {
      position: absolute;
      height: 4px;
      background: linear-gradient(to bottom right, gray, lightgray);
      bottom: -2px;
      left: 0;

      &:after {
        content: ' ';
        display: block;
        position: absolute;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background-color: #f1f1f1;
        top: -2px;
        right: -2px;
      }
    }

    .flex.active + .flex + .flex + .status-indicator {
      width: 33%;
    }

    .flex + .flex.active + .flex + .status-indicator {
      width: 66%;
    }

    .flex + .flex + .flex.active + .status-indicator {
      width: 100%;
    }
  }

  .selected-car {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 20px 25px 0;
    text-align: center;
    background-color: #fff;
    box-shadow: 0 2px 4px -1px rgba(0, 0, 0, .2), 0 4px 5px 0 rgba(0, 0, 0, .14), 0 1px 10px 0 rgba(0, 0, 0, .12);

    .car-name {
      margin-top: 15px;
    }

    .car-capacity {
      font-size: 0.7em;
    }

    .credit-card-info {
      margin-top: 10px;
      text-align: left;
      img {
        vertical-align: -3px;
        width: 30px;
      }
    }

    .action-button {
      text-transform: none;
      font-size: 12px;
      margin: 0 0 20px;
      box-shadow: none;
    }

    .confirm-button {
      width: 100%;
    }

    .action-buttons {
      display: flex;
      justify-content: space-between;
    }

    .cancel-button, .scan-button {
      width: calc(50% - 5px);
    }

    .confirm-button, .scan-button {
      color: #fff;
      background-color: #263773;
    }

    .cancel-button {
      border: 2px solid #263773;
      color: #263773;
      background-color: #fff;
    }
  }
</style>
