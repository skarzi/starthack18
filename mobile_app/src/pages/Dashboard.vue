<template>
  <div>
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
  </div>
</template>

<script>
  export default {
    data () {
      return {
        map: null
      }
    },
    mounted () {
      this.map = new GMaps({
        div: '#map-container',
        lat: 47.432421,
        lng: 9.374877,
        zoom: 16,
        disableDefaultUI: true
      })
    }
  }
</script>

<style lang="scss">
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
</style>
