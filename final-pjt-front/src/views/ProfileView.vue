<template>
  <div class="d-flex justify-content-center">
    <div class="article-center mt-2">
      <div class="d-flex">
        <div class="profileimgbox d-flex justify-content-center align-items-center">
          <img class="profileimg" alt="profileimg" src="@/assets/profile.png">
        </div>
        <div class="ps-5 ms-5">
          <div>
            <b style="font-size: 25px">{{ profile.username }}</b>
            <button class="like-btn ms-5">프로필 편집</button>
          </div>
          <div class="social-container">
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-facebook-f" /></a>
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-google-plus-g" /></a>
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-linkedin-in" /></a>
          </div>
          <div>
            <span class="profiletext">
              내 게시물 {{ profile.articles.length }}
            </span>
            <span class="ms-5 profiletext">
              좋아요 게시물 {{ profile.like_articles.length }}
            </span>
            <span class="ms-5 profiletext">
              좋아요 영화 {{ profile.like_movies.length }}
            </span>
          </div>
        </div>
      </div>
      <hr>
      <b-tabs content-class="mt-3">
        <b-tab title="Article" active>
          <b-table striped hover :items="items1"></b-table>
        </b-tab>
        <b-tab title="LikeArticle">
          <b-table striped hover :items="items2"></b-table>
        </b-tab>
        <b-tab title="LikeMovie">
          <b-table striped hover :items="items3"></b-table>
        </b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  data() {
    return {
      items1: [],
      items2: [],
      items3: []
    }
  },
  computed: {
    ...mapGetters(['profile']),
    profileArticles() {
      return this.profile.articles
    },
    profileLikeMovie() {
      return this.profile.like_movies
    }
  },
  methods: {
    ...mapActions(['fetchProfile']),
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    let article1 = this.profile.articles
    article1.filter(obj => {
      delete obj.pk
      return obj
    })
    this.items1 = article1
    let article2 = this.profile.like_articles
    article2.filter(obj => {
      delete obj.pk
      return obj
    })
    this.items2 = article2
    let article3 = this.profile.like_movies
    article3.filter(obj => {
      delete obj.pk
      return obj
    })
    this.items3 = article3
  },
}
</script>

<style>
.profileimgbox {
  height: 200px;
  width: 200px;
}

.profileimg {
  height: 150px;
  width: 150px;
}

.profiletext {
  font-size: 15px;
  font-weight: bold;
}

.profile-content{
  width: 720px;
}
</style>