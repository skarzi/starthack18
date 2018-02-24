<template>
  <div class="background">
    <div class="form-container">
      <div class="auth-input auth-input--login">
        <input type="text" name="username" placeholder="Username">
      </div>
      <div class="auth-input auth-input--password">
        <input type="password" name="password" placeholder="Password">
      </div>
    </div>
    <div class="buttons-container">
        <router-link to="">
          <v-btn large class="auth-button auth-button--register">Register</v-btn>
        </router-link>
        <router-link to="Dashboard">
          <v-btn large class="auth-button auth-button--signin">Sign In</v-btn>
        </router-link>
    </div>
    <p class="text-xs-right password-remind">
      <a href="#">Forgot password?</a>
    </p>
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
    background-image: url('../assets/backgroundd.png');
    background-size: 100% auto;
    background-color: #151E3F;
    background-position: center 160px;
    padding-top: 420px;
    padding-left: 25px;
    padding-right: 25px;
  }

  .buttons-container {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
    a {
      display: block;
      width: calc(50% - 5px);
    }
  }

  .auth-button {
    font-size: 13px;
    text-transform: none;
    height: 30px;
    border-radius: 0;
    margin: 0;
    width: 100%;

    &--register {
      background-color: #263773;
      color: #fff
    }
    &--signin {
      background-color: #fff;
      color: #263773;
    }
  }

  .auth-input {
    border-bottom: 1px solid #aaa;
    padding-left: 30px;
    height: 40px;
    background-size: auto 20px;
    background-position: 0 center;

    &--login {
      background-image: url('../assets/user.png');
    }
    &--password {
      background-image: url('../assets/lock.png');
      background-position-x: 2px;
    }

    input {
      color: #fff;
      width: 100%;
      font-size: 13px;
      margin-top: 12px;
    }
  }

  .volvo-logo {
    width: 100%;
    margin-top: 50px;
    margin-bottom: 150px;
  }

  .password-remind {
    margin-top: 15px;
    font-size: 12px;
    color: #fff;
    text-decoration: underline;
  }

</style>
