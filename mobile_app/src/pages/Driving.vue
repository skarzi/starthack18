<template>
  <div class="dashboard-view">
    <status-bar :status="2"></status-bar>
    <img class="car-photo" :src="car.icon + '?w=200'">
    <p class="instructions">
      Now take a look at the monitor screen.<br>
      Drive safe and have fun.
    </p>
    <v-btn class="finish-button" to="Leaderboard">
      Trip finished?
    </v-btn>
  </div>
</template>

<script>
  import store from '../store'
  import statusBar from '../components/StatusBar.vue'

  export default {
    components: {
      statusBar
    },
    computed: {
      car () {
        return store.state.reservedCar
      }
    },
    methods: {}
  }
</script>

<style lang="scss">

  .dashboard-view {
    position: relative;
    height: 100vh;
    background-color: #151E3F;
  }

  .car-photo {
    margin: 140px auto 70px;
  }

  .instructions {
    font-size: 16px;
    text-align: center;
    color: #fff;
  }

  .finish-button {
    color: #263773;
    background-color: #fff;
    text-transform: none;
    font-size: 12px;
    margin: 80px 20px 20px;
    box-shadow: none;
    border-radius: 0;
    width: calc(100% - 40px);
  }


</style>
