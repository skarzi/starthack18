<template>
  <div class="background"></div>
</template>

<script>
  export default {
    mounted () {
      const ws = new WebSocket('ws://130.82.238.4:8000/carsws/1/')
      ws.onmessage = (event) => {
        this.$router.push({name: 'Dashboard'})
      }
    }
  }
</script>

<style lang="scss">
  .background {
    width: 100vw;
    height: 100vh;
    background-image: url('../assets/background.png');
    background-size: cover;
    background-position: center center;
  }
</style>
