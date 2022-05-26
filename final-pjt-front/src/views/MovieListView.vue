<template>
  <div >
    <h1 class="text-center" style="font-family:ROKAFSansBold"><font-awesome-icon icon="fa-solid fa-magnifying-glass" /> 검색 결과 __개 입니다.</h1>
    <div class="d-flex justify-content-center mt-5">
      <moive-search-card
        v-for="movie in movieSearchList"
        :key="movie.pk"
        :movie="movie"
      ></moive-search-card>
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
@font-face {
    font-family: 'ROKAFSansBold', 'ROKAFSansMedium', 'ROKAFSlabSerifMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts2201-3@1.0/ROKAFSansBold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
</style>