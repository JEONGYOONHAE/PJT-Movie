<template>
  <li class="list-style-none">
    <div><b>{{ comment.user.username }}</b> | {{ createdComment }}</div>
    <span v-if="!isEditing">{{ payload.content }}</span>
    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <span class="mx-3">
        <button class="comment-btn" @click="onUpdate">Update</button> |
        <button class="comment-btn" @click="switchIsEditing">Cancle</button>
      </span>
    </span>
    <span 
      class="mx-3"
      v-if="currentUser.username === comment.user.username && !isEditing"
    >
      <button class="comment-btn" @click="switchIsEditing">Edit</button>
      <button class="comment-btn" @click="deleteComment(payload)">Delete</button>
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
    createdComment() {
      let today = new Date()
      let nowYear = today.getFullYear(); // 년도
      let nowMonth = today.getMonth() + 1;  // 월
      let nowDate = today.getDate();  // 일
      let nowhours = today.getHours(); // 시
      let nowminutes = today.getMinutes();  // 분
      // let nowseconds = today.getSeconds();  // 초

      let articleday = this.comment.created_at
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
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
  }
}
</script>

<style>
.list-style-none{
  list-style-type: none;
}

.comment-btn {
  margin-left: 6px;
  border: 0px;
  border-radius: 10px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.25), 
      0 2px 2px rgba(0,0,0,0.22);
}
</style>