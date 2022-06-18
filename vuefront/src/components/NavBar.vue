<template>
    <nav>
        <router-link to="/home">首页</router-link>
        <router-link to="/host">主播</router-link>
        <router-link to="/guest">观众</router-link>
    </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped>
.active {
    color: rgb(9, 195, 228);
}
nav {
  padding: 5px;
}

nav a {
  padding-right: 20px;
  font-weight: bold;
  font-size: larger;
  color: #2c3e50;
}

</style>
