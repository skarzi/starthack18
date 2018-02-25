<template>
  <div class="card-content">
    <div class="top-part">
      <p class="header error">
        Please avoid aggressive acceleration.
      </p>
    </div>
    <v-divider color="darkgray" class="error"></v-divider>
    <div class="bottom-part">
      <p class="regular">
        <img src="../../assets/red-star.png" class="star-icon">
        Mark, you've just accelerated really fast.<br>
        It's unsafe and wasteful.<br>
        Your score was deducted to <strong>4.9</strong>
      </p>
    </div>
  </div>
</template>

<script>
  export default {}
</script>

<style lang="scss">
  .error {
    color: red;
  }

  hr.error {
    background-color: red;
  }
</style>
