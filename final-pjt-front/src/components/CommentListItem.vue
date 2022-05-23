<template>
  <li class="list-style-none">
    <div>{{ comment.user.username }}</div>
    <span v-if="!isEditing">{{ payload.content }}</span>
    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <span class="mx-3">
        <button @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancle</button>
      </span>
    </span>
    <span 
      class="mx-3"
      v-if="currentUser.username === comment.user.username && !isEditing"
    >
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
    <hr>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      }
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  }
}
</script>

<style>
.list-style-none{
  list-style-type: none;
}
</style>