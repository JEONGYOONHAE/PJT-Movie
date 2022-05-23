<template>
  <div class="m-3">
    <h1>영화 추천</h1>
    <div class="d-flex justify-content-center">
      <form @submit.prevent="onSubmit">
        <input class="form-check-input mt-2" type="radio" name="genre" id="comedy" valeu="comedy" checked>
        <label for="comedy">코미디</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="horror" valeu="horror">
        <label for="comedy">공포</label>
        <input class="form-check-input mt-2 ms-3" type="radio" name="genre" id="romance" valeu="romance">
        <label for="comedy">로맨스</label>
        <button class="btn btn-secondary ms-3">Pick</button>
      </form>
    </div>
    <hr>
    <div class="d-flex">
      <img class="imgRadius" src="https://via.placeholder.com/300x400" alt="...">
      <div class="ms-3">
        <p>title: xxxxx</p>
        <p>overview: xxxxxxxx</p>
        <p>자세히 보러가기...</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieRecommendView'
}
</script>

<style>

</style>