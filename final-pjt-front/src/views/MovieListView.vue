<template>
  <div>
    <h1>검색한 영화 목록</h1>
    {{ movies }}
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieListView',
  computed: {
    ...mapGetters(['movies'])
  },
  methods: {
    ...mapActions(['fetchMovies'])
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style>

</style>