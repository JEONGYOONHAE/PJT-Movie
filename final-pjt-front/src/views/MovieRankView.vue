<template>
  <div class="m-3">
    <h1>영화 랭킹</h1>
    {{ movies }}
    <table class="table text-center">
      <thead>
        <tr>
          <th scope="col">순위</th>
          <th scope="col">제목</th>
          <th scope="col">평점</th>
          <th scope="col">추천</th>
        </tr>
      </thead>
      <tbody>
      <movie-table-body
        v-for="movie in movies"
        :key="movie.pk"
        :movie="movie"
      ></movie-table-body>
      </tbody>
    </table>
  </div>
</template>

<script>
import MovieTableBody from '@/components/MovieTableBody.vue'
import { mapGetters , mapActions } from 'vuex'
export default {
  name: 'MovieRankView',
  components: { MovieTableBody },
  computed: {
    ...mapGetters ([
      'movies'
    ])
  },
  methods: {
    ...mapActions ([
      'fetchMovies'
    ])
  },
  created() {
    this.fetchMovies()
  }
}
</script>

<style>

</style>