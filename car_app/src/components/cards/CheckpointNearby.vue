<template>
  <div class="card-content">
    <div class="top-part">
      <p class="header">
        Checkpoint Nearby!
      </p>
    </div>
    <v-divider color="darkgray"></v-divider>
    <div class="bottom-part">
      <p class="regular">
        <img src="../../assets/star.png" class="star-icon">
        Fuel the car at near Gas Station and boost your score.<br>We pay for it!
      </p>
      <v-btn class="do-it-button" @click="emitProgressEvent">
        Let's do it!
      </v-btn>
    </div>
  </div>
</template>

<script>
  export default {
    methods: {
      emitProgressEvent () {
        this.$emit('progress')
      }
    }
  }
</script>

<style lang="scss">
  .do-it-button {
    margin-top: 15px;
    font-size: 24px;
    color: #000;
    background-color: #fff;
    border: 2px solid #000;
    width: 600px;
    box-shadow: none !important;
    text-transform: none;
    height: 42px;
  }
</style>
