<template>
  <tr>
    <th scope="row">{{ index }}</th>
    <td>
      <router-link :to="{ name: 'movie', params: {moviePk: movie.pk } }">
        {{ movie.title }}
      </router-link>
    </td>
    <td>{{ movie.vote_average }}</td>
    <td>{{ movie.like_users.length }}</td>
  </tr>
</template>

<script>

export default {
  name: 'MovieTableBody',
  props: {
    movie: Object,
    index: Number,
  },
  
}
</script>

<style>

</style>