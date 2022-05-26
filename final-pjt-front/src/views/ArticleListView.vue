<template>
  <div class="m-3 ">
    <h1>Mark 게시판</h1>
    <router-link 
      :to="{ name: 'articlesNew' }"
      class="newArticle"
      >
      <font-awesome-icon icon="fa-solid fa-pencil" />
      글쓰기
    </router-link>
    <table class="table text-center">
      <thead>
        <tr>
          <th scope="col">번호</th>
          <th scope="col">제목</th>
          <th scope="col">글쓴이</th>
          <th scope="col">작성일</th>
          <th scope="col">추천</th>
        </tr>
      </thead>
      <tbody>
      <article-table-body
        v-for="article in articles"
        :key="article.pk"
        :article="article"
      ></article-table-body>
      </tbody>
    </table>
    <div class="bottom_pagination d-flex justify-content-center">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#">Previous</a></li>
        <li class="page-item active"><a class="page-link" href="#">1</a></li>
        <li class="page-item"><a class="page-link" href="#">2</a></li>
        <li class="page-item"><a class="page-link" href="#">3</a></li>
        <li class="page-item"><a class="page-link" href="#">Next</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import ArticleTableBody from '@/components/ArticleTableBody.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ArticleListView',
  components: { ArticleTableBody },
  computed: {
    ...mapGetters(['articles'])
  },
  methods: {
    ...mapActions(['fetchArticles'])
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>
.newArticle {
  position: relative;
  left: 90%;
}
.bottom_pagination {
  width: 100%;
}
</style>