<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>
    <div class="wholeBox d-flex justify-content-center align-items-center">
      <div class="loginbox">
        <img class="imgRadius mb-3" src="https://via.placeholder.com/80x60" alt="썸네일">
        <h2>Mark 계정 만들기</h2>
        <form @submit.prevent="signup(credentials)">
          <div>
            <div>
              <label for="username">아이디: </label>
            </div>
            <input v-model="credentials.username" type="text" id="username" placeholder="아이디를 입력해주세요" required/>
          </div>
          <div>
            <div>
              <label for="password1">비밀번호: </label>
            </div>
            <input v-model="credentials.password1" type="password" id="password1" placeholder="비밀번호를 입력해주세요" required/>
          </div>
          <div>
            <div>
              <label for="password2">비밀번호 재확인: </label>
            </div>
            <input v-model="credentials.password2" type="password" id="password2" placeholder="비밀번호 확인" required/>
          </div>
          <div class="mt-3">
            <router-link :to="{ name: 'login' }">대신 로그인하기</router-link>
            <button class="ms-5 btn btn-primary">Signup</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SignupView',
  components: {
      AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>