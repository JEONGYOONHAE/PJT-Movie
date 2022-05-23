<template>
  <div class="home text-center">
    <home-carousel
      :movies="movies"
    ></home-carousel>
    <div class="ms-5">
      <movie-search></movie-search>
      <div>
        <h3># 최신 상영 영화</h3>
        <main-home
          :movies="moviesRelese"
        ></main-home>
      </div>
      <div>
        <h3># 인기순 추천 영화</h3>
        <main-home
          :movies="moviesRank"
        ></main-home>
      </div>
      <div>
        <h3># 활동 많이 한 유저</h3>
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
