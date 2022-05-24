<template>
  <div>
    <!-- 평점을 등록한 적이 없는 경우 등록 -->
    <span v-if="!isReview">create</span>

    <!-- 평점을 등록했던 경우 수정, 삭제-->
    <span v-if="isReview">
      <span v-if="!isEditing">
        <button @click="editReview">edit</button> |
        <button @click="delteReview">delete</button>
      </span>
      <span v-if="isEditing">
        <button @click="updateReview">Update</button> |
        <button @click="cancleReview">Cancle</button>
      </span>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewItem',
  data() {
    return {

    }
  },
  methods:{
    ...mapActions(['updateReview']),
    editReview,
    delteReview,
    cancleReview
  }

}
</script>

<style>

</style>