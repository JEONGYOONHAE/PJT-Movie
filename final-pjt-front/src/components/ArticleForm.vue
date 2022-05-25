<template>
  <form @submit.prevent="onSubmit">
    <div class="text-end"><button>{{ action }}</button></div>
    <div>
      <div class="py-1">
        <input class="articleInput" v-model="formArticle.title" placeholder="제목을 입력해 주세요." type="text" id="title">
      </div>
    </div>
    <div>
      <div class="py-1">
        <textarea 
          v-model="formArticle.content" 
          type="text" 
          cols="30" rows="10"
          id="content" name="content" 
          class="articleInput"
          placeholder="내용을 입력해 주세요."
        ></textarea>
      </div>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ArticleForm',
  props: {
    article: Object,
    action: String,
  },
  data() {
    return {
      formArticle: {
        title: this.article.title,
        content: this.article.content,
      }
    }
  },
  methods: {
    ...mapActions(['createArticle', 'updateArticle']),
    onSubmit() {
      if (this.action === 'create') {
        this.createArticle(this.formArticle)
      } else if (this.action === 'update') {
        alert(this.article.pk)
        const payload = {
          pk: this.article.pk,
          ...this.formArticle,
        }
        this.updateArticle(payload)
      }
    }
  }
}
</script>

<style>
.articleInput {
  width: 80%;
}
</style>