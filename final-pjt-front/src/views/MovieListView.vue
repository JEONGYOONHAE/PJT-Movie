<template>
  <div>
    {{  movieSearchList }}
    <h1>검색한 영화 목록</h1>
    <div class="d-flex">
      <div>
        <moive-search-card
          v-for="movie in movieSearchList"
          :key="movie.pk"
          :movie="movie"
        ></moive-search-card>
      </div>
    </div>
  </div>
</template>

<script>
import MoiveSearchCard from '@/components/MoiveSearchCard.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieListView',
  components: { MoiveSearchCard },
  computed: {
    ...mapGetters(['movieSearchList'])
  },
}
</script>

<style>

</style>