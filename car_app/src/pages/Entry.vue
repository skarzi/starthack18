<template>
  <div class="background" @click="goToMain()">
  </div>
</template>
<script>
import router from '../router'

export default {
  data () {
    return {
    }
  },
  methods: {
    goToMain () {
      router.push('Main')
    }
  }
}
</script>
<style>
.background {
    height: 100vh;
    background-image: url('../assets/background.png');
    background-size: 100% auto;
    background-color: #151E3F;
    background-position: center;
    padding-top: 420px;
    padding-left: 25px;
    padding-right: 25px;
}
</style>
