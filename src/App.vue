<template>
  <div id="app">
    <Sagor msg="Hey, I'm learning Vue JS"/>
    <h2>{{msg}}</h2>
    <Todos v-bind:todos="todos"/>
    <TodoItem />
  </div>
</template>

<script>
import Sagor from './components/Sagor.vue';
import Todos from './components/Todos';
import TodoItem from './components/TodoItem';

export default {
  name: 'App',
  components: {
    Sagor,
    Todos,
    TodoItem
  },
  data(){
    return {
      msg: "I am freelancer...",
      todos: [
        {
          id:1,
          title: 'learning vue js',
          is_learn: false
        },
        {
          id:2,
          title: 'learning react js',
          is_learn: true
        },
        {
          id:2,
          title: 'learning angular js',
          is_learn: true
        },
      ]
    }
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
