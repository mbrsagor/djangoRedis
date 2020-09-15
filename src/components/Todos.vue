<template>
    <div>
        <h3>Todos component</h3>
        <ul v-bind:key="todo.id" v-for="todo in todos">
            <li> {{todo.id}} || {{todo.title}}  || {{todo.is_learn}} </li>
        </ul>
    </div>
</template>

<script>
export default {
    name:'Todos',
    props:['todos']
}
</script>

<style scoped>

</style>
