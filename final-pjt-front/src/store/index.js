import Vue from 'vue'
import Vuex from 'vuex'

import movies from './modules/movies'
import articles from './modules/articles'
import accounts from './modules/accounts'

import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  modules: {
    movies,
    articles,
    accounts,
  }
})
