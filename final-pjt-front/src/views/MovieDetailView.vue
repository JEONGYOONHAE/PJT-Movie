<template>
<div>
  <div class="movie-card">
  <div class="container">
    <a href="#" class="movie-poster"><img :src="`https://www.themoviedb.org/t/p/w342/${movie.poster_path}`" alt="poster"></a>
    <div class="hero">       
      <div class="details">
        <div class="title1">{{ movie.title }}</div> 
        <div class="my-2">
        <span
          v-for=" genre in genreList"
          :key="genre.id"
          class="tag text-center mx-1">
          {{ genre.name }}
        </span>
        <span class="likes align-self-end mx-2">{{ movieScore }}</span>
        <span class="like align-self-end">
            <button @click="likeMovie(movie.id)">
              <span :class="{'text-danger': isLikeMovie }"><font-awesome-icon icon="fa-solid fa-heart" /></span>
            </button>
          </span>
        <div class="inputscore my-4" v-if="correctMovie">
          <review-item></review-item>
        </div>
        </div>
      </div> <!-- end details -->
    </div> <!-- end hero -->
  
    <div class="description">
      <div class="column2">
        <p>{{ movie.overview }}</p>
      </div> <!-- end column2 -->
    </div> <!-- end description -->
  </div> <!-- end container -->
</div> <!-- end movie-card -->
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import ReviewItem from '@/components/ReviewItem.vue'

export default {
  components: { ReviewItem },
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLikeMovie', 'isReview', 'currentUser']),
    likeCount() {
      return this.movie.like_users?.length
    },
    genreList() {
      return this.movie.genre_ids
    },
    setReview() {
      return this.movie? this.movie.review_id : []
    },
    correctMovie() {
      if (this.movie.id === this.$route.params.moviePk) {
        return true
      } else {
        return false
      }
    },
    movieScore() {
      const sumWithInitial = this.movie.review_id.reduce(
        (accumulator, obj) => accumulator + obj.score,
        0
      );
      let movieScoreAvg = ((this.movie.vote_count*this.movie.vote_average) + sumWithInitial) / (this.movie.review_id.length + this.movie.vote_count)
      return movieScoreAvg.toFixed(2)
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie']),
  },
  created() {
    this.fetchMovie(this.moviePk)
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
*, *:before, *:after {
  box-sizing: border-box;
}

body {
  background: #43423E;
}
.movie-poster{
  position: absolute;
  top : 15%;
  left : 63%;
  z-index: 6;
}
a {
  text-decoration: none;
  color: #5C7FB8;
}

a:hover {
  text-decoration: underline;
}

.movie-card {
  color: #A9A8A3;
  position: relative;
}

.container {
  margin: 0 auto;
  width: 780px;
  height: 700px;
  background: #F0F0ED;
  border-radius: 5px;
  box-shadow: 0px 10px 20px 3px rgba(0, 0, 0, 0.55);
}

.hero {
  height: 342px;  
  margin:0;
  position: relative;
  overflow: hidden;
  z-index:1;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.hero:before {
  content:'';
  width:100%; height:100%;
  position:absolute;
  overflow: hidden;
  top:0; left:0;
  background:red;
  background: url("./image/background2.png");
  z-index:-1;
 
  transform: skewY(-2.2deg);
  transform-origin:0 0;
  
  -webkit-backface-visibility: hidden; 
}

.cover {
  position: absolute;
  top: 160px;
  left: 40px;
  z-index: 2;
}

.details {
  padding: 100px 0 0 80px;
} 
  
.title1 {
  color: white;
  font-size: 44px;
  margin-bottom: 13px;
  position: relative;
  font-family: 'ROKAFSansBold';
}    
  
.likes {
  margin-left: 24px;
  font-size: 20px;
}
  
.likes:before {
  content: url("https://www.lottecinema.co.kr/NLCHS/Content/images/icon/star_14.png");
  position: relative;
  top: 2px;
  padding-right: 7px;
}

.description {
  bottom: 0px;
  height: 200px;
  font-size: 20px;

  color: black;
  font-family: 'ROKAFSlabSerifMedium';
}

.column1 {
  padding-top: 50px;
  width: 220px;
  float: left;
  text-align: center;
}

.tag {
  background: #F0F0ED;
  border-radius: 10px;
  padding: 3px 8px;
  font-size: 20px;
  margin-right: 4px;
  line-height: 35px;
  cursor: pointer;
  color: black;
}

.tag:hover {
  background: #ddd;
}
.inputscore{
  font-size: 20px;
}
.column2 {
  padding-top: 30px;
  margin-left: 40px;
  width: 60%;
  float: left;
  font-size: 25px;
}

fieldset, label { margin: 0; padding: 0; }
</style>