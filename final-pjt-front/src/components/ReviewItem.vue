<template>
  <div>
    <!-- 평점을 등록한 적이 없는 경우 등록 -->
    <div v-if="!isReview">
      <form @submit.prevent="onSubmit">
        <div>
          <input type="range" id="score" name="score" min="0" max="10" v-model="payload.score">
          <label for="score">{{ payload.score }}</label>
        </div>
        <div>
          <input type="submit" value="평점등록">
        </div>
      </form>
    </div>
    
    <!-- 평점을 등록했던 경우 수정, 삭제 -->
    <div v-if="isReview">
      <span v-if="!isEditing">
        <div>내 평점 : {{ payload.score }}</div>
      </span>
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
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewItem',
  data() {
    return {
      isEditing: false,
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'isReview', 'movie', 'payload']),
  },
  methods:{
    ...mapActions(['fetchMovie', 'createReview', 'updateReview', 'deleteReview', 'fetchReview']),
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
        score: this.payload.score
      })
    },
  },
  created() {
    this.fetchReview()
  }
}
</script>

<style>

</style>