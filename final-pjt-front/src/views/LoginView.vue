<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>
    <div class="wholeBox d-flex justify-content-center align-items-center">
      <div class="loginbox text-center">
        <img class="imgRadius mb-3" src="https://via.placeholder.com/80x60" alt="썸네일">
        <h1>로그인</h1>
        <form @submit.prevent="login(credentials)">
          <div class="py-1">
            <input v-model="credentials.username" type="text" id="username" placeholder="아이디" required />
          </div>
          <div>
            <input v-model="credentials.password" type="password" id="password" placeholder="비밀번호" required />
          </div>

          <p class="py-3">아이디/패스워드를 잊으셨나요?</p>
          <router-link :to="{ name: 'signup' }">계정 만들기</router-link>
          <button class="ms-5 btn btn-primary">로그인</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LoginView',
  components: {
      AccountErrorList,
    },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>
.wholeBox {
  width: 100%;
  height: 100%;
  margin-top: 100px;
}

.loginbox {
  width: 368px;
  height: 416px;
  padding: 48px 40px 36px;
  border: 1px solid;
  background-color: rgb(228, 228, 228);
  border-radius: 10px;
}
</style>