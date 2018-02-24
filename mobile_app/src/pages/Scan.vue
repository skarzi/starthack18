<template>
  <div class="dashboard-view">
    <status-bar :status="1"></status-bar>
    <qrcode-reader @decode="onDecode"></qrcode-reader>
  </div>
</template>

<script>
  import axios from 'axios'
  import store from '../store'
  import statusBar from '../components/StatusBar.vue'
  import { QrcodeReader } from 'vue-qrcode-reader'

  export default {
    components: {
      statusBar, QrcodeReader
    },
    methods: {
      onDecode (content) {
        console.log(content)
        if (content === store.state.reservedCar.id.toString()) {
          axios.put(`/cars/unlock/${content}/1/`).then(resp => {
            console.log(resp)
            this.$router.push({name: 'Driving'})
          })
        }
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

  .qrcode-reader {
    height: calc(100vh - 112px);
  }



</style>
