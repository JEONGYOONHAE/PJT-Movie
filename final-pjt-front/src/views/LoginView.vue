<template>
  <div class="user-box">
    <div class="a-container" id="a-container">
      <div class="form-container sign-up-container">
        <form class="a-form" @submit.prevent="signup(signupCredentials)">
          <h1>회원가입</h1>
          <div class="social-container">
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-facebook-f" /></a>
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-google-plus-g" /></a>
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-linkedin-in" /></a>
          </div>
          <span>or use your information for registration</span>
          <input class="a-input" v-model="signupCredentials.username" type="text" id="username" placeholder="아이디" required/>
          <input class="a-input" v-model="signupCredentials.password1" type="password" id="password1" placeholder="비밀번호" required/>
          <input class="a-input" v-model="signupCredentials.password2" type="password" id="password2" placeholder="비밀번호 확인" required/>
          <button class="a-button">Sign Up</button>
        </form>
      </div>
      <div class="form-container sign-in-container">
        <form class="a-form" @submit.prevent="login(loginCredentials)">
          <h1>로그인</h1>
          <div class="social-container">
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-facebook-f" /></a>
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-google-plus-g" /></a>
            <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-linkedin-in" /></a>
          </div>
          <span>or use your account</span>
          <input class="a-input" v-model="loginCredentials.username" type="text" id="username" placeholder="아이디" required />
          <input class="a-input" v-model="loginCredentials.password" type="password" id="password" placeholder="비밀번호" required />
          <a class="a" href="#">아이디/패스워드를 잊으셨나요?</a>
          <button class="a-button">Sign In</button>
        </form>
      </div>
      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-panel overlay-left">
            <h1>로그인 GoGo</h1>
            <p>아이디 있는거 다 알아요 언능언능 로그인해서 페이지를 좀 둘러 봅시다!</p>
            <button class="a-button ghost" id="signIn" @click="removePanel">Sign In</button>
          </div>
          <div class="overlay-panel overlay-right">
            <h1>Hello, 칭구들!</h1>
            <p>아이디가 없으면 아이디를 만들러 가세요 아래 회원가입 버튼을 친히 만들어 드렸습니다!</p>
            <button class="a-button ghost" id="signUp" @click="addPanel">Sign Up</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import AccountErrorList from '@/components/AccountErrorList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LoginView',
  // components: {
  //     AccountErrorList,
  //   },
  data() {
    return {
      loginCredentials: {
        username: '',
        password: '',
      },
      signupCredentials: {
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
    ...mapActions(['login', 'signup']),
    addPanel() {
      const container = document.getElementById('a-container');
      container.classList.add("right-panel-active");
    },
    removePanel() {
      const container = document.getElementById('a-container');
      container.classList.remove("right-panel-active");
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

.user-box {
  background: #f6f5f7;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  font-family: 'Montserrat', sans-serif;
  height: 100vh;
  margin: -20px 0 0px;
}

h1 {
  font-weight: bold;
  margin: 0;
}

p {
  font-size: 14px;
  font-weight: 100;
  line-height: 20px;
  letter-spacing: 0.5px;
  margin: 20px 0 30px;
}

span {
  font-size: 12px;
}

.a {
  color: #333;
  font-size: 14px;
  text-decoration: none;
  margin: 15px 0;
}

.a-button {
  border-radius: 20px;
  border: 1px solid #FF4B2B;
  background-color: #FF4B2B;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.a-button {
  border-radius: 20px;
  border: 1px solid #FF4B2B;
  background-color: #FF4B2B;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: bold;
  padding: 12px 45px;
  letter-spacing: 1px;
  text-transform: uppercase;
  transition: transform 80ms ease-in;
}

.a-button:active {
  transform: scale(0.95);
}

.a-button:focus {
  outline: none;
}

.a-button.ghost {
  background-color: transparent;
  border-color: #FFFFFF;
}

.a-form {
  background-color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 50px;
  height: 100%;
  text-align: center;
}

.a-input {
  background-color: #eee;
  border: none;
  padding: 12px 15px;
  margin: 8px 0;
  width: 100%;
}

.a-container {
  background-color: #fff;
  border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
      0 10px 10px rgba(0,0,0,0.22);
  position: relative;
  overflow: hidden;
  width: 768px;
  max-width: 100%;
  min-height: 480px;
}

.form-container {
  position: absolute;
  top: 0;
  height: 100%;
  transition: all 0.6s ease-in-out;
}

.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}

.a-container.right-panel-active .sign-in-container {
  transform: translateX(100%);
}

.sign-up-container {
  left: 0;
  width: 50%;
  opacity: 0;
  z-index: 1;
}

.a-container.right-panel-active .sign-up-container {
  transform: translateX(100%);
  opacity: 1;
  z-index: 5;
  animation: show 0.6s;
}

@keyframes show {
  0%, 49.99% {
    opacity: 0;
    z-index: 1;
  }
  
  50%, 100% {
    opacity: 1;
    z-index: 5;
  }
}

.overlay-container {
  position: absolute;
  top: 0;
  left: 50%;
  width: 50%;
  height: 100%;
  overflow: hidden;
  transition: transform 0.6s ease-in-out;
  z-index: 100;
}

.a-container.right-panel-active .overlay-container{
  transform: translateX(-100%);
}

.overlay {
  background: #FF416C;
  background: -webkit-linear-gradient(to right, #FF4B2B, #FF416C);
  background: linear-gradient(to right, #FF4B2B, #FF416C);
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 0 0;
  color: #FFFFFF;
  position: relative;
  left: -100%;
  height: 100%;
  width: 200%;
    transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.a-container.right-panel-active .overlay {
    transform: translateX(50%);
}

.overlay-panel {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 40px;
  text-align: center;
  top: 0;
  height: 100%;
  width: 50%;
  transform: translateX(0);
  transition: transform 0.6s ease-in-out;
}

.overlay-left {
  transform: translateX(-20%);
}

.a-container.right-panel-active .overlay-left {
  transform: translateX(0);
}

.overlay-right {
  right: 0;
  transform: translateX(0);
}

.a-container.right-panel-active .overlay-right {
  transform: translateX(20%);
}

.social-container {
  margin: 20px 0;
}

.social-container a {
  border: 1px solid #DDDDDD;
  border-radius: 50%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px;
  height: 40px;
  width: 40px;
}
</style>