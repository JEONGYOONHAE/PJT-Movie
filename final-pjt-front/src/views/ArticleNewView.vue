<template>
  <div class="m-3">
    <h1>μ κΈ μμ±</h1>
    <hr>
      <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'

export default {
  name: 'ArticleNewView',
  components: { ArticleForm },
  data() {
    return {
      article: {
        pk: null,
        title: '',
        content: '',
      }
    }
  },
}
</script>

<style>

</style>