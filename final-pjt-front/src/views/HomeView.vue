<template>
  <div class="home text-center mrb" >
    <home-carousel
      :movies="movies"
    ></home-carousel>
    <div class="ms-4">
      <movie-search></movie-search>
      <div class="d-flex row justify-content-center">
        <div class="home_title">
          <h3 style="font-family:ROKAFSansBold">최신 상영 영화</h3>
        </div>
        <main-home
          :movies="moviesRelese"
        ></main-home>
      </div>
      <div>
        <h3 class="my-4" style="font-family:ROKAFSansBold">인기순 추천 영화</h3>
        <main-home
          :movies="moviesRank"
        ></main-home>
      </div>
      <div>
        <h3 style="font-family:ROKAFSansBold">활동 많이 한 유저</h3>
        <user-active></user-active>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MainHome from '@/components/MainHome.vue'
import UserActive from '@/components/UserActive.vue'
import MovieSearch from '@/components/MovieSearch.vue'
import HomeCarousel from '@/components/HomeCarousel.vue'

import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'HomeView',
  components: {
    MainHome,
    UserActive,
    MovieSearch,
    HomeCarousel,
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
  .home_title{
    color : #254b67;
    height : 70px;
  }
</style>
