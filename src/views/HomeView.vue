<script setup>
import HelloWorld from '../components/HelloWorld.vue';
import IconCommunity from '../components/icons/IconCommunity.vue';
import TheWelcome from '../components/TheWelcome.vue'
import WelcomeItem from '../components/WelcomeItem.vue';
import AboutView from './AboutView.vue';
import Chart from './Chart.vue';
</script>

<template>
  <main>
    <Chart/>
    
  </main>
</template>

<script>

export default {
    data() {
        return {};
    },
    components: { HelloWorld, WelcomeItem, IconCommunity, AboutView }
}
</script>