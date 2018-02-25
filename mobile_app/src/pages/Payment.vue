<template>
  <div class="dashboard-view">
    <status-bar :status="3"></status-bar>
    <div class="leaderboard-content">
      <div class="leaderboard-name">
        <p>Payment details</p>
        <v-divider color="lightgray"></v-divider>
        <p class="month">March, 2018</p>
      </div>

      <div class="leaderboard-list">
        <v-layout class="highscore" row wrap>
          <v-flex xs8 offset-xs1 class="name">Distance</v-flex>
          <v-flex xs2 class="score">10 km</v-flex>
        </v-layout>
        <v-layout class="highscore" row wrap>
          <v-flex xs8 offset-xs1 class="name">Cost per km</v-flex>
          <v-flex xs2 class="score">1 CHF</v-flex>
        </v-layout>
        <v-layout class="highscore" row wrap>
          <v-flex xs8 offset-xs1 class="name">Discount</v-flex>
          <v-flex xs2 class="score">-10%</v-flex>
        </v-layout>
        <v-layout class="highscore mt-3" row wrap>
          <v-flex xs8 offset-xs1 class="name">Cost</v-flex>
          <v-flex xs2 class="score">9 CHF</v-flex>
        </v-layout>
      </div>
      <p class="congratulations">
      </p>
      <v-btn class="finish-button" @click="finish">
        Lock the car and pay
      </v-btn>
    </div>
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
    methods: {
      finish () {
        store.commit('cancelReservation')
        this.$router.push({name: 'Dashboard'})
      }
    }
  }
</script>

<style lang="scss">

  .dashboard-view {
    position: relative;
    height: 100vh;
    background-color: #151E3F;
  }

  .leaderboard-content {
    padding: 0 20px;
    color: #fff;
  }

  .leaderboard-name {
    margin-top: 40px;
    padding: 0 80px;
    font-size: 16px;

    .month {
      font-size: 0.8em;
      margin-top: 7px;
    }
  }

  .leaderboard-list {
    margin-top: 30px;
    text-align: left;

    .highscore {
      height: 30px;
      font-size: 18px;
    }

    .score {
      text-align: right;
    }
  }

  .congratulations {
    font-size: 18px;
    margin-top: 70px;
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
    margin: 130px 20px 20px;
    box-shadow: none;
    border-radius: 0;
    width: calc(100% - 40px);
  }


</style>
