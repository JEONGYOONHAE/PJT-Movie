<template>
  <div class="d-flex justify-content-center">
    <div class="article-center">
      <div class="empty-space"></div>
      <h3>{{ article.title }}</h3>
      <b>{{ article.user.username }}</b> | {{ createdArticle }}
      <hr>
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button class="comment-btn">수정</button>
        </router-link>
        <button class="comment-btn" @click="deleteArticle(articlePk)">삭제</button>
      </div>
      <div class="articleContent py-5">
        {{ article.content }}
      </div>
      <hr>
      <div class="d-flex justify-content-center">
        <button class="like-btn" @click="likeArticle(articlePk)">
          추천
          <span :class="{'text-danger': isLike }"><font-awesome-icon icon="fa-solid fa-heart" /></span>
          {{ likeCount }}
        </button>
      </div>
      <hr>
      <b>댓글</b> <span class="comment-cnt">총 <span style="color:#42b983">{{ article.comments.length }}</span> 개</span>
      <hr>
      <comment-list :comments="article.comments"></comment-list>
    </div>
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
    },
    createdArticle() {
      let today = new Date()
      let nowYear = today.getFullYear(); // 년도
      let nowMonth = today.getMonth() + 1;  // 월
      let nowDate = today.getDate();  // 일
      let nowhours = today.getHours(); // 시
      let nowminutes = today.getMinutes();  // 분
      // let nowseconds = today.getSeconds();  // 초

      let articleday = this.article.created_at
      let articleYear = articleday.slice(0, 4)
      let articleMonth = articleday.slice(5, 7)
      let articleDate = articleday.slice(8, 10)
      let articlehours = articleday.slice(11, 13)
      let articleminutes = articleday.slice(14, 16)
      // let articleseconds = articleday.slice(17, 19)

      let _date
      if (nowYear > articleYear) {_date = `${nowYear-articleYear}년 전`}
      else if (nowMonth > articleMonth) {_date = `${nowMonth - articleMonth}달 전`}
      else if (nowDate > articleDate) {_date = `${nowDate - articleDate}일 전`}
      else if (nowhours > articlehours) {_date = `${nowhours - articlehours}시간 전`}
      else if (nowminutes > articleminutes) {_date = `${nowminutes - articleminutes}분 전`}
      else {_date = '방금 전'}

      return _date
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
.articleContent {
  white-space: pre-wrap;
}

.empty-space {
  min-height: 10vh;
}

.comment-cnt {
  font-size: 6px;
  color: rgba(168, 168, 168, 0.788);
}

.article-center{
  max-width: 720px;
}

.like-btn {
  margin-left: 6px;
  border: 1px solid;
  border-radius: 5px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.25), 
      0 2px 2px rgba(0,0,0,0.22);
}
</style>