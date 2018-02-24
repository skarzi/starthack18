<template>
  <div>
    <v-toolbar dark class="main-toolbar">
      <v-icon @click="$router.go(-1)">arrow_back</v-icon>
      <v-toolbar-title class="white--text">Sign in</v-toolbar-title>
    </v-toolbar>

    <div class="body text-xs-left pl-3 pr-3 pb-5">
      <v-form>
        <v-card color="grey lighten-4" class="card--flex-toolbar mt-4">
          <v-toolbar card prominent>
            <v-toolbar-title><strong>Login information</strong>
            </v-toolbar-title>
          </v-toolbar>
          <v-divider color="grey"></v-divider>
          <v-card-text>
            <v-text-field label="Username" required></v-text-field>
            <v-text-field label="Password" required
                          type="password"></v-text-field>
          </v-card-text>
        </v-card>
      </v-form>
      <div class="text-xs-right mt-4">
        <v-btn
          class="white--text"
          color="cyan"
        >
          Sign in
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style lang="scss">
  .main-toolbar {
    background-color: #1C1A44;
  }

  .input-group__details:before {
    background-color: #333;
  }
</style>
