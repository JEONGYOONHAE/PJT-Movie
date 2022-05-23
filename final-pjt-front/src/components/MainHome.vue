<template>
  <div class="d-flex hello">
    <div 
      class="py-3"
      v-for="movie in movies"
      :key="movie.pk"  
    >
      <movie-card :movie="movie"></movie-card>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'MainHome',
  components: { MovieCard },
  props: {
    movies: Object,
  }
}
</script>

<style >

</style>
