<template>
  <div class="bar-container">
    <div class="bar-label" :class="{'color': labelColor}">
    </div>
    <div class="bar-body">
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      labelColor: 'orange'
    }
  }
}
</script>
<style>
</style>
