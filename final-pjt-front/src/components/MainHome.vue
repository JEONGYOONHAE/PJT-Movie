<template>
  <div class="hello">
    <div class="d-flex py-3">
      <movie-card></movie-card>
      <movie-card></movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
export default {
  name: 'MainHome',
  components: { MovieCard },
}
</script>

<style >

</style>
