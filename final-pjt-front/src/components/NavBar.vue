<template>
  <div>
    <nav class="d-flex justify-content-between navbar navbar-expand navbar-light bg-light">
      <div class="d-flex align-items-center">
        <router-link :to="{ name: 'home' }">
          <img class="logo" alt="Vue logo" src="../assets/logo.png">
        </router-link>
        <ul class="navbar-nav">
          <li class="m-3">
            <router-link :to="{ name: 'home' }">Home</router-link>
          </li>
          <li class="m-3">
            <router-link :to="{ name: 'movieRank' }">영화랭킹</router-link>
          </li>
          <li class="m-3">
            <router-link :to="{ name: 'movieRecommend' }">영화추천</router-link>
          </li>
          <li class="m-3">
            <router-link :to="{ name: 'articles' }">게시판</router-link>
          </li>
        </ul>
      </div>
      <ul class="navbar-nav">
        <li v-if="isAdmin" class="m-3">
          <a href="http://127.0.0.1:8000/admin/">관리자 페이지</a>
        </li>
        <li v-if="!isLoggedIn" class="m-3">
          <router-link :to="{ name: 'login' }">로그인</router-link>
        </li>
        <li v-if="!isLoggedIn" class="m-3">
          <router-link :to="{ name: 'signup' }">회원가입</router-link>
        </li>
        <li v-if="isLoggedIn" class="m-3">
          <router-link :to="{ name: 'profile', params: { username } }">{{ username }}</router-link>
        </li>
        <li v-if="isLoggedIn" class="m-3">
          <router-link :to="{ name: 'logout' }">로그아웃</router-link>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser', 'isAdmin']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
  },
}
</script>

<style>
.logo {
  width: 30px;
}

nav ul li a {
  font-weight: bold;
  color: #2c3e50;
}

nav ul li a.router-link-exact-active {
  color: #42b983;
}
</style>