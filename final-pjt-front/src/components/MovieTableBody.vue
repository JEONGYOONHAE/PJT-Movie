<template>
<div>
    <div class="mt_card-view">
      <div class="mt_card-header">
        <div class="rank_num">{{ index }}</div>
        <router-link :to="{ name: 'movie', params: { moviePk: movie.pk } }">
          <img :src="`https://www.themoviedb.org/t/p/w300/${ movie.poster_path }`" style="withd:100%" alt="썸네일">
        </router-link>
      </div> 
      <div class="mt_card-movie-content">
        <div class="mt_card-movie-content-head">
            <h3 class="mt_card-movie-title">{{ movie.title }}</h3>
          <div class="d-flex align-items-end">
            <div class="mt_ratings "><span>{{ movie.vote_average }}</span>/10</div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- <tr>
    <th scope="row">{{ index }}</th>
    <td>
      <router-link :to="{ name: 'movie', params: {moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
    </td>
    <td>{{ movie.vote_average }}</td>
    <td>{{ movie.like_users.length }}</td>
  </tr> -->
</template>

<script>

export default {
  name: 'MovieTableBody',
  props: {
    movie: Object,
    index: Number,
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
.rank_num{
  font-family: 'ROKAFSansBold';
  font-size: 50px;
  position:float;
}
.mt_card-view {
    background: #ffffff;
    box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 315px;
    margin: 2em;
    border-radius: 10px;
    display: inline-block;
}
 
.mt_card-header {
    padding: 0;
    margin: 0;

    width: 100%;
    display: block;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
}
.mt_card-header-icon {
    position: relative;
}
 
.mt_eader-icon {
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
 
.mt_eader-icon:hover {
    background: rgba(0, 0, 0, 0.15);
    font-size: 74px;
    text-shadow: 0px 0px 20px #6abcea, 0px 5px 30px #6ABCEA;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    opacity: 1;
}
.mt_card-view:hover {
    -webkit-transform: scale(1.03);
    transform: scale(1.03);
    box-shadow: 0px 10px 25px rgba(84, 176, 184, 0.605);
}
 
.mt_card-movie-content {
    padding: 30px 18px 24px 18px;
    margin: 0;
}
 
.mt_card-movie-content-head,
.mt_card-movie-info {
    display: table;
    width: 100%;
}
 
.mt_card-movie-title {
    font-size: 22px;
    margin: 0;
    display: table-cell;
    font-weight:bold;
}
 
.mt_ratings {
  width: 50px;
  height: 15px;
  background-size: contain;
  display: table-cell;
  text-align: right;
  position: relative;
  margin-top: 5px;
  font-weight: 600;

}
 
.mt_ratings span {
  color: #2196F3;
  font-size:20px;
}
 
.mt_card-movie-info {
  margin-top: 1em;
}
</style>