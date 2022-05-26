<template>
<!-- <div>
  <b-card
    overlay
    img-src="https://picsum.photos/900/250/?image=3"
    img-alt="Card Image"
    text-variant="white"

    sub-title="Subtitle"
  >
    <b>Welcom.</b>
    <b>Millions of movies, TV shows and people to discover. Explore now.</b>
    <b-card-text>
      <p>please enter a title of movie</p>
    </b-card-text>
  </b-card>
</div>-->
<div></div>
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