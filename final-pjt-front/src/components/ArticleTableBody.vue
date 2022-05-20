<template>
  <tr>
    <th scope="row">{{ article.pk }}</th>
    <td>
      <router-link :to="{ name: 'article', params: {articlePk: article.pk } }">
        {{ article.title }}
      </router-link>
    </td>
    <td>
      <router-link :to="{ name: 'profile', params: { username } }">
        {{ article.user.username }}
      </router-link>
    </td>
    <td>작성일</td>
    <td>{{ likeCount }}</td>
  </tr>
</template>

<script>
export default {
  name: 'ArticleTableBody',
  props: {
    article: Object,
  },
  computed: {
    username() {
      return this.article.user.username
    },
    likeCount() {
      return this.article.like_count
    }
  }
}
</script>

<style>

</style>