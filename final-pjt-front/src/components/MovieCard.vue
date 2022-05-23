<template>
  <div class="ps-4">
    <img class="imgRadius" :src="`https://www.themoviedb.org/t/p/w220_and_h330_face/${ movie.poster_path }`" alt="썸네일">
    <div class="px-3 pt-3">
      <b>{{ movie.title }}</b>
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
}
</script>

<style>
.imgRadius {
  border-radius: 20px;
}
</style>