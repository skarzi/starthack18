<template>
  <div class="background">
    <img class="volvo-logo" src="../assets/volvo.png">
    <div class="buttons-container">
      <div>
        <router-link to="Register">
          <v-btn large class="auth-button">Register</v-btn>
        </router-link>
      </div>
      <div>
        <v-btn large class="auth-button">Sign In</v-btn>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style lang="scss">
  a {
    text-decoration: none;
    color: inherit;
  }
  .background {
    height: 100vh;
    background-image: url('../assets/background.png');
    background-size: cover;
  }

  .volvo-logo {
    width: 100%;
    margin-top: 50px;
    margin-bottom: 150px;
  }

  .auth-button {
    background-color: #fff;
    width: 250px;
    margin-top: 25px;
  }
</style>
