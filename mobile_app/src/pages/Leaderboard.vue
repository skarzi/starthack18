<template>
  <div class="dashboard-view">
    <status-bar :status="3"></status-bar>
    <div class="leaderboard-content">
      <div class="leaderboard-name">
        <p>Leaderboard</p>
        <v-divider color="lightgray"></v-divider>
        <p class="month">March, 2018</p>
      </div>

      <div class="leaderboard-list">
        <v-layout class="highscore" row wrap>
          <v-flex xs2 class="icon"></v-flex>
          <v-flex xs8 class="name">Mark</v-flex>
          <v-flex xs2 class="score">4.85</v-flex>
        </v-layout>
        <v-layout class="highscore" row wrap>
          <v-flex xs2 class="icon icon--second"></v-flex>
          <v-flex xs8 class="name">Celia</v-flex>
          <v-flex xs2 class="score">4.60</v-flex>
        </v-layout>
        <v-layout class="highscore" row wrap>
          <v-flex xs2 class="icon icon--third"></v-flex>
          <v-flex xs8 class="name">John</v-flex>
          <v-flex xs2 class="score">4.25</v-flex>
        </v-layout>
      </div>
      <p class="congratulations">
        Congratulations Mark!<br>
        10% off that trip!
      </p>
      <v-btn class="finish-button" to="Payment">
        Next
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
    methods: {}
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

    .icon {
      background-image: url('../assets/diamond.png');
      background-size: auto 16px;
      background-position: 10px 4px;
      &--second {
        opacity: 0.66;
      }
      &--third {
        opacity: 0.33;
      }
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
    margin: 80px 20px 20px;
    box-shadow: none;
    border-radius: 0;
    width: calc(100% - 40px);
  }


</style>
