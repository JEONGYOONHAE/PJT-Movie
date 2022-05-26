<template>
  <div class="">
    <form @submit.prevent="onSubmit">
      <textarea name="comment" id="comment" cols="80" rows="4" v-model="content" placeholder="여러분의 소중한 댓글을 입력해 주세요." required>
      </textarea>
      <div>
        <button class="comment-btn">등록</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ 
        articlePk: this.article.pk,
        content: this.content
      })
      this.content = ''
    }
  }
}
</script>

<style>

</style>