<template>
  <div class="m-3">
    <h1>게시글 수정</h1>
    <hr>
    <article-form :article="article" action="update"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ArticleEditView',
  components: { ArticleForm },
  computed: {
    ...mapGetters(['article', 'isArticle'])
  },
  methods: {
    ...mapActions(['fetchArticle'])
  },
  created() {
    this.fetchArticle(this.$route.params.articlePk)
  }
}
</script>

<style>

</style>