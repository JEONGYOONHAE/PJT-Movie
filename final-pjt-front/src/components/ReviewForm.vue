<template>
  <div></div>
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