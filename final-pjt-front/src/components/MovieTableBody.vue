<template>
  <tr>
    <th scope="row">{{ movie.pk }}</th>
    <td>
      <router-link :to="{ name: 'movie', params: {moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
    </td>
    <td>평점</td>
    <td>관심</td>
  </tr>
</template>

<script>
export default {
  name: 'MovieTableBody',
  props: {
    movie: Object,
  },
  computed: {

  },
}
</script>

<style>

</style>