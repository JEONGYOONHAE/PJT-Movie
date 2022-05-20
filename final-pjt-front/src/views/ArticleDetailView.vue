<template>
  <div class="m-3">
    <h3>{{ article.title }}</h3>
    {{ article.user.username }} | time
    <hr>
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>수정</button>
      </router-link>
      <button @click="deleteArticle(articlePk)">삭제</button>
    </div>
    <div class="articleContent m-3">
      <p>{{ article.content }}</p>
    </div>
    
    <hr>
    <div class="d-flex justify-content-center">
      <button @click="likeArticle(articlePk)">
        추천
        <span :class="{'text-danger': isLike }"><font-awesome-icon icon="fa-solid fa-heart" /></span>
        {{ likeCount }}
        </button>
    </div>
    <hr>
    <comment-list :comments="article.comments"></comment-list>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import CommentList from '@/components/CommentList.vue'

export default {
  name: 'ArticleDetailView',
  components: { CommentList },
  data() {
    return {
      articlePk: this.$route.params.articlePk,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'article', 'isLike']),
    likeCount() {
      return this.article.like_users?.length
    }
  },
  methods: {
    ...mapActions([
      'fetchArticle',
      'likeArticle',
      'deleteArticle',
    ])
  },
  created() {
    this.fetchArticle(this.articlePk)
  }
}
</script>

<style>

</style>