<template>
  <div class="m-3">
    <h1>{{ profile.username }}님의 프로필</h1>
    <hr>
    <div>
      <a @click.prevent="moveArticle">게시글</a> | 
      <a @click.prevent="moveComment">댓글</a> | 
      <a @click.prevent="moveLike">좋아요 한 영화</a>
    </div>
    {{ profile }} 
    <div v-show="choose === 0">
      <div 
      v-for="article in profileArticles"
      :key="article.pk"
      >
        <div>
          title: {{ article.title }}
        </div>
        <div>
          content: {{ article.content }}
        </div>
        <hr>
      </div>
    </div>
    <div v-show="choose === 1">
      {{ profile.like_articles }}
      <hr>
    </div>
    <div v-show="choose === 2">
      <div 
      v-for="likeMovie in profileLikeMovie"
      :key="likeMovie.pk"
      >
        <div>
          제목 : {{ likeMovie.title }}
        </div>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ProfileView',
  data() {
    return {
      choose: 0
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
    moveArticle() {
      this.choose = 0
    },
    moveComment() {
      this.choose = 1
    },
    moveLike() {
      this.choose = 2
    },
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style>

</style>