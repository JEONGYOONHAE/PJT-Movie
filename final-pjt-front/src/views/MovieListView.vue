<template>
  <div >
    <h1 class="h1_title" style="font-family:ROKAFSansBold"><font-awesome-icon icon="fa-solid fa-magnifying-glass" /> 검색 결과 입니다.</h1>
    <div class="d-flex mt-5 mx-5">
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
.h1_title {
  margin-top: 40px; 
  margin-left: 40px;
  font-family: 'ROKAFSansBold';
}
</style>