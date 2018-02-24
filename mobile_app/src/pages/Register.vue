<template>
  <div>
    <v-toolbar dark class="main-toolbar">
      <v-icon @click="$router.go(-1)">arrow_back</v-icon>
      <v-toolbar-title class="white--text">Create new account</v-toolbar-title>
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
            <v-text-field label="Repeat password" required
                          type="password"></v-text-field>
          </v-card-text>
        </v-card>
        <v-card color="grey lighten-4" class="card--flex-toolbar mt-4">
          <v-toolbar card prominent>
            <v-toolbar-title><strong>Driver License</strong></v-toolbar-title>
          </v-toolbar>
          <v-divider color="grey"></v-divider>
          <v-card-text class="text-xs-center">
            <v-btn
              class="white--text"
              color="cyan"
            >
              Upload scan or a photo
              <v-icon right dark>cloud_upload</v-icon>
            </v-btn>
          </v-card-text>
        </v-card>
        <v-card color="grey lighten-4" class="card--flex-toolbar mt-4">
          <v-toolbar card prominent>
            <v-toolbar-title><strong>Credit card</strong></v-toolbar-title>
          </v-toolbar>
          <v-divider color="grey"></v-divider>
          <v-card-text>
            <v-text-field label="Card Number" required></v-text-field>
            <v-layout row wrap>
              <v-flex xs6>
                <v-text-field label="Exp. date" required></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field label="CVV" required></v-text-field>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-form>
      <v-divider class="mb-3 mt-4" color="gray"></v-divider>
      <div class="text-xs-right">
        <v-btn
          class="white--text"
          color="cyan"
        >
          Apply
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
