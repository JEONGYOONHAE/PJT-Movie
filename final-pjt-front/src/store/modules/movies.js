import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    movies: [],
    movie: {},
    moviesRank: [],
    moviesRelese: [],
    movieSearchList: [],
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    moviesRank: state => state.moviesRank,
    moviesRelese: state => state.moviesRelese,
    isLikeMovie: (state, getters) => {
      if (_.findIndex(state.movie.like_users, ['username', getters.currentUser.username]) === -1) {
        return false
      }
      return true
    },
    movieSearchList: state => state.movieSearchList
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIESRANK: (state, moviesRank) => state.moviesRank = moviesRank,
    SET_MOVIESRELESE: (state, moviesRelese) => state.moviesRelese = moviesRelese,
    SET_MOVIESEARCH: (state, movieSearchList) => state.movieSearchList = movieSearchList,
  },
  actions: {
    fetchMovies({ commit, state }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
      })
        .then(res => {
          commit('SET_MOVIES', res.data )
          commit('SET_MOVIESRANK', _.sortBy(state.movies, 'vote_average').reverse())
          commit('SET_MOVIESRELESE', _.sortBy(state.movies, 'release_date').reverse())
        })
        .catch(err => console.error(err.response)) 
    },
    fetchMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({ name: 'NotFound404' })
          }
        })
    },
    likeMovie({ commit, getters }, moviePk) {
      axios({
        url: drf.movies.likeMoive(moviePk),
        method: 'post',
        headers: getters.authHeader
      })
        .then(res => commit('SET_MOVIE', res.data))
        .catch(err => console.error(err.response))
    },
    movieSearch({ commit, getters }, movieTitle) {
      commit('SET_MOVIESEARCH', _.filter(getters.movies, (movie) => {
        return movie.title.includes(movieTitle)
      }))
    }
  },
}