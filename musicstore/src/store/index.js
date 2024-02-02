import Vue from 'vue';
import Vuex from 'vuex';
import home from './modules/home.js';
import user from './modules/user.js'
import cart from './modules/cart.js'

Vue.use(Vuex)

export default new Vuex.Store({
    modules:{
        home,
        user,
        cart
    }
})