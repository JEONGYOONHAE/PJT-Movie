<template>
  <div class="home text-center mrb" >
    <div class="ms-4">
      <movie-search></movie-search>
      <div class="d-flex row justify-content-center">
        <div>
          <h3 class="hv_title mt-5" >최신 상영 영화</h3>
        </div>
        <main-home
          :movies="moviesRelese"
        ></main-home>
      </div>
      <div>
        <h3 class="my-4 hv_title" >인기순 추천 영화</h3>
        <main-home
          :movies="moviesRank"
        ></main-home>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MainHome from '@/components/MainHome.vue'
// import UserActive from '@/components/UserActive.vue'
import MovieSearch from '@/components/MovieSearch.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'HomeView',
  components: {
    MainHome,
    // UserActive,
    MovieSearch,
  },
  computed: {
    ...mapGetters ([
      'movies',
      'moviesRank',
      'moviesRelese',
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
    font-family: 'ROKAFSansBold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts2201-3@1.0/ROKAFSansBold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
  .hv_title{
    color : #254b67;
    font-family:ROKAFSansBold;
    font-size: 40px;
  }
</style>
