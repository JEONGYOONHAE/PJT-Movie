<template>
  <div class="d-flex justify-content-center ">
    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
      <ol class="carousel-indicators">
        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block carousel-img" :src="randomImg[0]" alt="First slide">
        </div>
        <div class="carousel-item">
          <img class="d-block carousel-img" :src="randomImg[1]" alt="Second slide">
        </div>
        <div class="carousel-item">
          <img class="d-block carousel-img" :src="randomImg[2]" alt="Third slide">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
      </a>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'HomeCarousel',
  props: {
    movies: Array,
  },
  computed: {
    randomImg() {
      let randomMovie = _.sampleSize(this.movies, 3)
      randomMovie = randomMovie.map( obj => {
        return 'https://www.themoviedb.org/t/p/w780' + obj.backdrop_path
      })
      return randomMovie
    },
  },
  methods: {
    
  }
}
</script>

<style>

</style>