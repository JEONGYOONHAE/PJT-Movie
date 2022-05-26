<template>
  <div class="m-3 mrb">
    <h1 class="h1_title">영화 랭킹</h1>
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
        v-for="(movie, index) in moviesRank"
        :key="movie.pk"
        :index="index+1"
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
      'moviesRank'
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
@font-face {
    font-family: 'ROKAFSansBold', 'ROKAFSansMedium', 'ROKAFSlabSerifMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts2201-3@1.0/ROKAFSansBold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.h1_title {
  margin-top: 0.7em;
  margin-left: 0.7em;
  font-family: 'ROKAFSansBold';
}
</style>