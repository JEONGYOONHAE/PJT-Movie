<template>
<div>
  <div class="card-view">
    <div class="card-header">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
        <img  :src="`https://www.themoviedb.org/t/p/w300/${ movie.poster_path }`" style="withd:100%" alt="썸네일">
      </router-link>
    </div>

    <div class="card-movie-content">
      <div class="card-movie-content-head">
          <h3 class="card-movie-title">{{ movie.title }}</h3>
      </div>
      <div class="ratings"><span>{{ movie.vote_average }}</span>/10</div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  methods: {
    movieClick() {
      this.$router.push({ name: 'movie', params: {moviePk: this.movie.pk } })
    }
  }
}
</script>

<style>
.imgRadius {
  border-radius: 20px;
}
.card-view {
    background: #ffffff;
    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 315px;
    margin: 2em;
    border-radius: 10px;
    display: inline-block;
}
 
.card-header {
    padding: 0;
    margin: 0;

    width: 100%;
    display: block;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}
.card-header-icon {
    position: relative;
}
 
.header-icon {
    width: 100%;
    height: 367px;
    line-height: 367px;
    text-align: center;
    vertical-align: middle;
    margin: 0 auto;
    color: #ffffff;
    font-size: 54px;
    text-shadow: 0px 0px 20px #6abcea, 0px 5px 20px #6ABCEA;
    opacity: .85;
}
 
.header-icon:hover {
    background: rgba(0, 0, 0, 0.15);
    font-size: 74px;
    text-shadow: 0px 0px 20px #6abcea, 0px 5px 30px #6ABCEA;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    opacity: 1;
}
.card-view:hover {
    -webkit-transform: scale(1.03);
    transform: scale(1.03);
    box-shadow: 0px 10px 25px rgba(84, 176, 184, 0.605);
}
 
.card-movie-content {
    padding: 30px 18px 24px 18px;
    margin: 0;
}
 
.card-movie-content-head,
.card-movie-info {
    display: table;
    width: 100%;
}
 
.card-movie-title {
    font-size: 22px;
    margin: 0;
    display: table-cell;
}
 
.ratings {
    width: 50px;
    height: 15px;
    background-size: contain;
    display: table-cell;
    text-align: right;
    position: relative;
    margin-top: 5px;
    font-weight: 600;
}
 
.ratings span {
    color: #2196F3;
}
 
.card-movie-info {
    margin-top: 1em;
}
</style>