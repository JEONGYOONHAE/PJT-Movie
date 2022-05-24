<template>
  <div class="m-3">
    <h1>영화 추천</h1>
    <div class="d-flex justify-content-center">
      <div>
        <input class="form-check-input mt-2" type="radio" name="genre" id="comedy" value="코미디" checked>
        <label for="comedy">코미디</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="horror" value="공포" v-model="movieGenre">
        <label for="horror">공포</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="romance" value="로맨스" v-model="movieGenre">
        <label for="romance">로맨스</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="SF" value="SF" v-model="movieGenre">
        <label for="SF">SF</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="ani" value="애니메이션" v-model="movieGenre">
        <label for="ani">애니메이션</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="fantage" value="판타지" v-model="movieGenre">
        <label for="fantage">판타지</label>
        <button @click="moviePick" class="btn btn-secondary ms-3">Pick</button>
      </div>
    </div>
    <hr>
    <div class="d-flex" v-if="isRandomMovie">
      <img class="imgRadius" :src="`https://www.themoviedb.org/t/p/w342${randomMovie.poster_path}`" alt="...">
      <div class="ms-3">
        <p>title: {{ randomMovie.title }}</p>
        <p>overview: {{ randomMovie.overview }}</p>
        <router-link :to="{ name: 'movie', params: {moviePk: randomMovie.pk } }">
        자세히 보러가기...
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'MovieRecommendView',
  data() {
    return {
      movieGenre: '',
      randomMovie: {}
    }
  },
  computed: {
    ...mapGetters(['movies']),
    isRandomMovie() {
      return !_.isEmpty(this.randomMovie)
    }
  },
  methods: {
    moviePick() {
      this.randomMovie = _.sample(_.filter(this.movies, (movie) => { 
        return !_.isEmpty(_.filter(movie.genre_ids, ['name', this.movieGenre]))
      }))
    }
  }

}
</script>

<style>

</style>