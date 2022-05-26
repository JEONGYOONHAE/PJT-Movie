import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faMagnifyingGlass, faPencil, faHeart } from '@fortawesome/free-solid-svg-icons'
import { faFacebookF, faGooglePlusG, faLinkedinIn, faGithub, faFacebook, faGooglePlus } from '@fortawesome/free-brands-svg-icons'

library.add(faMagnifyingGlass, faPencil, faHeart, faFacebookF, faGooglePlusG, faLinkedinIn, faGithub, faFacebook, faGooglePlus)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(BootstrapVue)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
