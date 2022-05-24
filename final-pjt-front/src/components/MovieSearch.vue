<template>
  <form 
    class="my-4"
    @submit.prevent="searchSubmit"
  >
    <button>
      <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
    </button>
    <input type="text" placeholder="영화를 검색해주세요." v-model="movieTitle">
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default {
  name: 'MovieSearch',
  data() {
    return {
      movieTitle: '',
    }
  },
  computed: {
    ...mapGetters(['movies', 'movieSearchList']),
  },
  methods: {
    ...mapActions(['movieSearch']),
    searchSubmit() {
      this.movieSearch(this.movieTitle)
      this.movieTitle = ''
      if (_.isEmpty(this.movieSearchList)) {
        alert('검색 결과가 없습니다.')
      } else {
        this.$router.push('movies')
      }
    }
  }
}
</script>

<style>

</style>