<template>
  <div>
    <h1>영화 세부항목</h1>
    <div class="d-flex align-items-center movie-detail-bg">
      <img :src="`https://www.themoviedb.org/t/p/w342/${movie.poster_path}`" class="imgRadius" alt="poster">
      <div class="ps-3">
        <h3>{{ movie.title }}{{ movie.release_date }}</h3>
        <div>
          장르 : 
          <span
            v-for=" genre in genreList"
            :key="genre.id"
          >
            {{ genre.name }}
          </span>
        </div>
        <div>
          <button @click="likeMovie(movie.id)">
            추천
            <span :class="{'text-danger': isLikeMovie }"><font-awesome-icon icon="fa-solid fa-heart" /></span>
            {{ likeCount }}
          </button> 평점: 
          <span>{{ movieScore }}</span>
        </div>
        <div v-if="correctMovie">
          <review-item></review-item>
        </div>
        <div>
          <p>개요</p>
          {{ movie.overview }}
        </div>
      </div>
    </div>
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
.movie-detail-bg{
  background-color: blanchedalmond;
  width: 100%;
  height: 600px;
}
</style>