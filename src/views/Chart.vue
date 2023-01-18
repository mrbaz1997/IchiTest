<template class="chart">
  <button type="button" id="get-joke" @click="fetchAPIData">Get Chart</button>
  <div v-if="responseAvailable == true">
    <hr>
    <p>{{ result }}
    </p>
    <hr>
  </div>
</template>

<script>
export default {
  name: "test",
  data() {
    return {
      result: null,
      responseAvailable: false,
      APIKey: "T084SMZSYP1VH2IL",
      function: "FX_DAILY",
      url: "",
    }
  },
  methods: {
  },
  created: function () {
    console.log("Starting connection to WebSocket Server")
    this.result = new WebSocket("wss://marketdata.tradermade.com/feedadv")

    this.result.onmessage = function (event) {
      console.log(event);
    }

    this.result.onopen = function (event) {
      this.result.send("{\"userKey\":\"sioDXZLutTRvXwmoRmaqA\", \"symbol\":\"GBPUSD\"}");
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

  },
}
</script>

<style>
@media (min-width: 1024px) {
  .chart {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
