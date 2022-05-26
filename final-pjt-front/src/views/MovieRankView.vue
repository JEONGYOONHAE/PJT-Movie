<template>
  <div class="mrb">
    <h1 class="h1_title">영화 랭킹</h1>
    <div class="container d-flex justify-content-between">
      <div class="rank_grid">
        <div class="row row-cols-4">
          <movie-table-body
            v-for="(movie, index) in moviesRank"
            :key="movie.pk"
            :index="index+1"
            :movie="movie"
            class="col"
          ></movie-table-body>
        </div>

      </div>

    </div>
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
  margin-top: 40px;
  margin-left: 40px;
  font-family: 'ROKAFSansBold';
}
.rank_grid{
}
</style>