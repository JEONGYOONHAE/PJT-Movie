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
    payload: {},
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    moviesRank: state => state.moviesRank,
    moviesRelese: state => state.moviesRelese,
    isLikeMovie: (state, getters) => {
      return !!state.movie.like_users.find(obj => obj.username === getters.currentUser.username)
    },
    movieSearchList: state => state.movieSearchList,
    isReview: (state, getters) => {
      return !!state.movie.review_id.find(obj => obj.user.username === getters.currentUser.username)
    },
    payload: state => state.payload,
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIESRANK: (state, moviesRank) => state.moviesRank = moviesRank,
    SET_MOVIESRELESE: (state, moviesRelese) => state.moviesRelese = moviesRelese,
    SET_MOVIESEARCH: (state, movieSearchList) => state.movieSearchList = movieSearchList,
    SET_MOVIE_REVIEWS: (state, review_id) => state.movie.review_id = review_id,
    SET_PAYLOAD: (state, payload) => state.payload = payload,
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
    },
    createReview({ commit, getters, dispatch }, { moviePk, score }) {
      // const score1 = { score }
      // console.log(score)
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'post',
        data: {score : Number(score)},
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          dispatch('fetchReview')
        })
        .catch(err => console.error(err.response))
    },
    updateReview({ commit, getters, dispatch }, { moviePk, reviewPk, score }) {
      const newScore = { score }
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'put',
        data: newScore,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          dispatch('fetchReview')
        })
        .catch(err => console.error(err.response))
    },
    deleteReview({ commit, getters, dispatch }, { moviePk, reviewPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'delete',
          headers: getters.authHeader
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
            dispatch('fetchReview')
          })
          .catch(err => console.error(err.response))
      }
    },
    fetchReview({ commit, getters }) {
      if (getters.isReview) {
        const getReview = getters.movie.review_id.find(obj => obj.user.username === getters.currentUser.username)
        let 파스타먹고싶다 = {
          moviePk: getReview.movie_id,
          reviewPk: getReview.pk,
          score: getReview.score
        }
        commit('SET_PAYLOAD', 파스타먹고싶다)
      } else {
        let 파스타먹고싶다222 = {
          score: 0
        }
        commit('SET_PAYLOAD', 파스타먹고싶다222)
      }
    }
  },

}