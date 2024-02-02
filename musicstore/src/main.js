import Vue from 'vue'
import App from './App.vue'
import store from './store'
import axios from 'axios'
import VueRouter from 'vue-router'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.prototype.$axios = axios
Vue.config.producFormItemtionTip = false
// 对$router.push()方法进行重写
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err);
};

new Vue({
  el:'#app',
  render: h => h(App),
  beforeCreate(){ 
    Vue.prototype.$bus = this
  },
  store,
  router,
})
