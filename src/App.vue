<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Hey, I'm learning Vue JS"/>
    <Sagor msg="Hey, I'm learning Vue JS"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import Sagor from './components/Sagor.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    Sagor
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
