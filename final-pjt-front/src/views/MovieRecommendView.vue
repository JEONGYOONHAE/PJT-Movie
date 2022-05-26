<template>
  <div class="">
    <h1 class="h1_title">영화 추천</h1>
    <div class="d-flex justify-content-center fs-5" style="font-family:ROKAFSansBold">
      <div>
        <input class="form-check-input mt-2" type="radio" name="genre" id="comedy" value="코미디" checked>
        <label for="comedy">코미디</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="horror" value="공포" v-model="movieGenre">
        <label for="horror">공포</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="romance" value="로맨스" v-model="movieGenre">
        <label for="romance">로맨스</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="SF" value="SF" v-model="movieGenre">
        <label for="SF">SF</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="ani" value="애니메이션" v-model="movieGenre">
        <label for="ani">애니메이션</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="fantage" value="판타지" v-model="movieGenre">
        <label for="fantage">판타지</label>
        <button @click="moviePick" class="btn btn-secondary ms-3">Pick</button>
      </div>
    </div>
    <hr>
    <div class="div_container d-flex justify-content-center text-white" v-if="isRandomMovie">
      <div class="dd ">
        <div class="d-flex mdv_container border ">
          <div class="mdv_poster  border-black">
            <img :src="`https://www.themoviedb.org/t/p/w342/${randomMovie.poster_path}`" alt="poster">
          </div>
          <div class="mdv_content d-flex align-items-center row ">
            <div class="background-black">
              <div class="mdv_column1 ">
                <div class="mdv_title mx-5 my-3 fs-1" style="font-family:ROKAFSansBold">{{ randomMovie.title }}</div>  
                <div class="mdv_genre mx-5 my-3">
                  <span
                    v-for=" genre in genreList"
                    :key="genre.id"
                    class="mdv_genretag text-black mx-2">
                    {{ genre.name }}
                  </span>
                  <span class="fs-5">{{ randomMovie.release_date }}</span> 
                </div>
                <div class="mdv_score mx-5">
              </div>
              <div class="mdv_column2">
                <div class="mdv_descriptions fs-4 mx-5" style="font-family:ROKAFSansMedium">{{ randomMovie.overview }}</div>
                <div class="fs-4 mx-5 rout_tag text-center d-flex align-items-center justify-content-center">
                  <router-link style=text-decoration:none; :to="{ name: 'movie', params: {moviePk: randomMovie.pk } }">
                    Read More ..
                  </router-link>
                </div>
              </div>
              </div>
            </div>
        </div>
      </div>
      </div>
  </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import _ from 'lodash'

export default {
  name: 'MovieRecommendView',
  data() {
    return {
      movieGenre: '',
      randomMovie: {}
    }
  },
  computed: {
    ...mapGetters(['movies']),
    isRandomMovie() {
      return !_.isEmpty(this.randomMovie)
    }
  },
  methods: {
    moviePick() {
      this.randomMovie = _.sample(_.filter(this.movies, (movie) => { 
        return !_.isEmpty(_.filter(movie.genre_ids, ['name', this.movieGenre]))
      }))
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
.h1_title {
  margin-top: 0.7em;
  margin-left: 0.7em;
  font-family: 'ROKAFSansBold';
}
.div_container {
  position: relative;
  padding: 0px 30px;  
}
.mdv_container {
  box-shadow: 0px 20px 30px 3px rgba(0, 0, 0, 0.55);

}
.dd {
width: 70%;
height: 60%;
border-color:black;
  
}
.mdv_content {
  background: url("./image/background.png");
}

.mdv_genretag {
  background: white;
  border-radius: 10px;
  padding: 3px 8px;
  font-size: 20px;
  margin-right: 4px;
  line-height: 35px;
  cursor: pointer;
}

.mdv_genretag:hover {
  background: #ddd;
}

h1 {
  font-size: 100px;
}

.rout_tag {
  width:30%;
  height:50px;
  color: #77B6E2;
  text-decoration:none;
  font-family: 'Montserrat', sans-serif;
  border:2px solid #77B6E2;
  padding:10px 10px 10px 40px;
  font-size:12px;
  background-size:12px 12px;
  background-repeat:no-repeat;
  background-position: 7% 50%;
  border-radius:5px;
  -webkit-transition-property: all;
  transition-property: all;
  -webkit-transition-duration: .5s;
  transition-duration: .5s;
  padding:0 0 0 40px;
  margin:30px 0 0 0;
  text-decoration : none;
}
.rout_tag:hover { 
  color: #000000;
  background-color: #77B6E2;
  background-image:url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/343086/rFQ5dHA.png);
  background-size:12px 12px;
  background-repeat:no-repeat;
  background-position: 10% 50%;
  cursor: pointer;
  -webkit-transition-property: all;
  transition-property: all;
  -webkit-transition-duration: .5s;
  transition-duration: .5s;
  text-decoration : none;
}
        
</style>