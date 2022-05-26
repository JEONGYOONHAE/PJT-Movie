<template>
  <div class="row justify-content-center my_card mb-5">
    <div class="col-12 col-md-10 col-lg-8 mt-2">
      <span class="fs-2" style="font-family:ROKAFSansBold">PLEASE ENTER A TITLE</span>
      <form 
        class="card card-sm border-0"
        @submit.prevent="searchSubmit">
        <div class="card-body row no-gutters align-items-center my_card">
          <div class="col-auto">
          </div>
          <div class="col">
            <input style="font-family:ROKAFSansMedium" class="form-control form-control-lg form-control-borderless" type="text" placeholder="영화를 검색해주세요." v-model="movieTitle">
          </div>
          <div class="col-auto my_btn">
            <button style="font-family:ROKAFSansBold" class="btn btn-lg color-white" type="submit">Search</button>
          </div>
        </div>
      </form>
    </div>
  </div>
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
@font-face {
    font-family: 'ROKAFSansBold', 'ROKAFSansMedium', 'ROKAFSlabSerifMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts2201-3@1.0/ROKAFSansBold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.my_btn {
  background-color:#77B6E2;
  color: white;
}
.my_card {
  background-color:#D1ECFB;
  

}
</style>