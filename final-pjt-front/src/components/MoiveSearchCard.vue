<template>
<div>
  <div class="card-view text-center">
    <div class="card-header">
      <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
        <img  :src="`https://www.themoviedb.org/t/p/w300/${ movie.poster_path }`" alt="썸네일">
      </router-link>
    </div>

    <div class="card-movie-content">
      <div class="card-movie-content-head">
        <h3 class="card-movie-title">{{ movie.title }}</h3>
        <div class="ratings"><span>{{ movie.vote_average }}</span>/10</div>
      </div>
      <div class="card-movie-info">
        <div class="movie-running-time">
            <label>Last update</label>
            <span>   Sun 8 Sept - 10:00PM</span>
        </div>
        <div class="movie-running-time">
            <label>Running time</label>
            <span>   2hr 09min</span>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'MoiveSearchCard',
  props: {
    movie: Object
  },
}
</script>

<style>
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
  box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.08);
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
  font-weight: bold;
}
 
.ratings {
  width: 50px;
  height: 15px;
  background-size: contain;
  display: table-cell;
  position: relative;
  margin-top: 5px;
  font-weight: 600;
  font-size:30px;

}
 
.ratings span {
  color: #2196F3;
  font-size:30px;
}
 
.card-movie-info {
  margin-top: 1em;
  font-size:20px;
  font-weight: bold;
}
.movie-running-time span {
  font-size:15px;
}
</style>