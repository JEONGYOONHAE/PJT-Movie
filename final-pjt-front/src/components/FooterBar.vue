<template>
  <footer class="text-center">
    <div class="py-5">
      <p>
        <span class="text-dark font-weight-bold">공지사항</span> | 
        <span class="text-dark font-weight-bold">이용약관</span> | 
        <span class="text-dark font-weight-bold">개인정보처리방침</span>
      </p>
      <div class="footer-container">
        <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-facebook" /></a>
        <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-google-plus" /></a>
        <a href="#" class="social a"><font-awesome-icon icon="fa-brands fa-github" /></a>
      </div>
      <p class="m-0">고객센터  02-3429-5100  |  평일 상담시간  09:00 ~ 18:00</p>
      <p class="m-0">본 컨텐츠의 저작권은 저작권자 또는 제공처에 있으며, 이를 무단 이용하는 경우 저작권법 등에 따라 법적 책임을 질 수 있습니다. </p>
      <span>© 2020 Copyright: </span>
      <span>MY<span style="writing-mode:tb-rl">:D</span></span>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterBar',
}
</script>

<style>
footer {
  font-family: 'Montserrat', sans-serif;
  background-color: rgba(240, 240, 240, 0.473);
  color: rgb(194, 194, 194);
}
.footer-container {
  margin: 20px 0;
}

.footer-container a {
  border-radius: 50%;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  margin: 0 5px;
  height: 40px;
  width: 40px;
}

.footer-container a svg {
  height: 2rem;
}
</style>