<template>
  <div class="dashboard-view">
    <status-bar :status="1"></status-bar>
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
          <v-btn class="action-button cancel-button"
                 @click="cancelReservation">
            Cancel
          </v-btn>
            <v-btn class="action-button scan-button" to="Scan">
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
  import statusBar from '../components/StatusBar.vue'

  export default {
    data () {
      return {
        map: null,
        cars: [],
        chosenCar: undefined
      }
    },
    components: {
      statusBar
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
        icon: 'https://i.imgur.com/jzJxuAI.png'
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
