import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router'
import ViewUI from 'view-design'
import 'view-design/dist/styles/iview.css';
import axios from 'axios'
import store from './store'
// import ElementUI from 'element-ui'
// import '@/icons'

Vue.use(VueRouter)
Vue.use(ViewUI);
// Vue.use(ElementUI)
Vue.prototype.axios = axios;

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
