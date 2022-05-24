<template>
  <div>
    {{ movie }}
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
          <span>{{ movie.vote_average }}</span>
        </div>
        <div>
          평점주기
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

export default {
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLikeMovie']),
    likeCount() {
      return this.movie.like_users?.length
    },
    genreList() {
      return this.movie.genre_ids
    }
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie'])
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