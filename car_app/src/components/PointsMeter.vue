<template>
  <div class="points-meter">
    <span class="points-value" :style="{left: score/5*100 + '%'}">{{ score.toFixed(2) }}</span>
    <div class="meter-slot">
      <div class="meter-frame" :style="{width: score/5*100 + '%'}">
        <div class="meter-bar"></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    props: ['score']
  }
</script>

<style lang="scss">
  .points-meter {
    width: 400px;
    position: relative;

    .points-value {
      font-size: 34px;
      color: #36b698;
      position: absolute;
      bottom: calc(100% + 10px);
      transform: translateX(-50%);
      text-shadow: 2px 2px #d0d0d0;
      transition: all 0.4s linear;
    }

    .meter-slot {
      height: 30px;
      border-radius: 4px;
      background-color: #E1E1E1;
      border-top: 1px solid #ddd;
      position: relative;
      overflow: hidden;
    }
    .meter-slot:before {
      content: "";
      position: absolute;
      z-index: 1;
      width: 100%;
      top: -10px;
      height: 10px;
      left: 0;
      box-shadow: 0 0 18px rgba(0, 0, 0, 0.6);
    }

    .meter-frame {
      overflow: hidden;
      z-index: 999;
      position: absolute;
      transition: all 0.4s linear;
    }

    .meter-bar {
      height: 30px;
      width: 400px;
      background: linear-gradient(to right, #e97a3b, #ee9c37, #f2bb34, #94bb66, #43b98f, #36b698);
    }
  }
</style>
