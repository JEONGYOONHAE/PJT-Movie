<template>
  <div class="ps-4">
    <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
      <img class="imgRadius" :src="`https://www.themoviedb.org/t/p/w220_and_h330_face/${ movie.poster_path }`" alt="썸네일">
    </router-link>
    <div class="px-3 pt-3">
      <div @click="movieClick">
        <b>{{ movie.title }}</b>
      </div>
      <div>
        3월 10, 2022
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  methods: {
    movieClick() {
      this.$router.push({ name: 'movie', params: {moviePk: this.movie.pk } })
    }
  }
}
</script>

<style>
.imgRadius {
  border-radius: 20px;
}
</style>