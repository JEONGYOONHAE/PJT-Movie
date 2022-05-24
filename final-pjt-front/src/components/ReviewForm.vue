<template>
  <form @submit.prevent="onSubmit">
    <div>
      <input type="range" id="volume" name="volume" min="0" max="10" v-model="star">
      <label for="volume">{{ star }}</label>
    </div>
    <div>
      <input type="submit" value="평점등록">
    </div>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name : 'ReviewForm',
  data(){
    return {
      star : 0
    }
  },
  computed: {
    ...mapGetters(['movie']),
  },
  methods:{
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({ 
        moviePk: this.movie.id,
        score: this.star
      })
      this.star = 0
    },
  }
}
</script>

<style>

</style>