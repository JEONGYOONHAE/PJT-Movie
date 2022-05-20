<template>
  <form 
    class="my-4"
    @submit.prevent="onSubmit"
  >
    <button>
      <font-awesome-icon icon="fa-solid fa-magnifying-glass" />
    </button>
    <input type="text" placeholder="영화를 검색해주세요." v-model="movieTitle">
  </form>
</template>

<script>
export default {
  name: 'MovieSearch',
  data() {
    return {
      movieTitle: ''
    }
  },
  methods: {
    onSubmit() {},
  }

}
</script>

<style>

</style>