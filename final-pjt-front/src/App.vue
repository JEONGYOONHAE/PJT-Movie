<template>
  <div id="app">
    <nav-bar v-if="isLoggedIn"></nav-bar>
    <div class="base-body">
      <router-view/>
    </div>
    <footer-bar v-if="isLoggedIn" class="sticky-bottom"></footer-bar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import NavBar from '@/components/NavBar.vue'
import FooterBar from '@/components/FooterBar.vue'

export default {
  name: 'App',
  components: { NavBar, FooterBar },
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.base-body {
  display: relative;
  max-width: 100vw;
  min-height: calc(100vh - 190px);
}
</style>
