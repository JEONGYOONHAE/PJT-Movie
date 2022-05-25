<template>
  <div>
    평점주기
    {{ isReview }}
    <p>{{ payload }}</p>
    <!-- 평점을 등록한 적이 없는 경우 등록 -->
    <span v-if="!isReview">
      <form @submit.prevent="onSubmit">
        <div>
          <input type="range" id="score" name="score" min="0" max="10" v-model="score">
          <label for="score">{{ payload.score }}</label>
        </div>
        <div>
          <input type="submit" value="평점등록">
        </div>
      </form>
    </span>
    
    <!-- 평점을 등록했던 경우 수정, 삭제 -->
    <span v-if="isReview">
      <span v-if="!isEditing">{{ payload.score }}</span>
      <span v-if="isEditing">
        <div>
          <input type="range" id="score" name="score" min="0" max="10" v-model="payload.score">
          <label for="score">{{ payload.score }}</label>
        </div>
        <span>
          <button @click="onUpdate">Update</button> |
          <button @click="switchIsEditing">Cancle</button>
        </span>
      </span>
      <span v-if="!isEditing">
        <button @click="switchIsEditing">수정</button> |
        <button @click="deleteReview(payload)">삭제</button>
      </span>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default {
  name: 'ReviewItem',
  data() {
    return {
      payload: {
        score: 0
      },
      isEditing: false,
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'isReview', 'movie']),
  },
  methods:{
    ...mapActions(['createReview', 'updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      this.isEditing = false
    },
    onSubmit() {
      this.createReview({
        moviePk: this.$route.params.moviePk,
        score: this.score
      })
    },
  },
  created() {
    alert(this.isReview)
    if (this.isReview) {
      console.log(this.movie)
      this.payload = _.filter(this.movie.review_id, obj => {
        return obj.user.username === this.currentUser.username
      })[0]
    }
  }
}
</script>

<style>

</style>