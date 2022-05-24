<template>
  <div class="d-flex">
    <router-link :to="{ name: 'movie', params: {moviePk: movie.pk } }">
      <img class="imgRadius" :src="`https://www.themoviedb.org/t/p/w154/${ movie.poster_path }`" alt="썸네일">
    </router-link>
    <div>
      <router-link :to="{ name: 'movie', params: {moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
      <p>{{ movie.release_date }}</p>
      <p>{{ movie.overview }}</p>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'MoiveSearchCard',
  props: {
    movie: Object
  },
}
</script>

<style>

</style>