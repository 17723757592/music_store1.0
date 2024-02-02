<template>
  <div id="app">  
    <BannerName></BannerName>
    <router-view :key="$route.fullPath"><HomePage></HomePage></router-view>
    <BottomName></BottomName>
  </div>
</template>

<script>
// import readMe from './api/readMe'
import BannerName from './components/Banner.vue'
import HomePage from './components/home/HomePage.vue'
import BottomName from './components/Bottom'

import {mapState } from 'vuex'

export default {
  name: 'App',
  data(){
    return{
    }
  },
  computed:{
    ...mapState('cart', ['shoppingCart'])
  },
  components: {
    BannerName,
    HomePage,
    BottomName
  },
  watch:{
    shoppingCart:{
      immediate:true,
      deep:true,
      handler(val){
        sessionStorage.setItem('shoppingCart', JSON.stringify(val))
      }
    }
  },
}
</script>

<style>
li{
    list-style: none;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
body, html, h1, h2, h3, h4, h5, h6, ul, ol, li, dl, dt, dd, header, menu, section, p, input, td, th, section{
  padding: 0;
  margin: 0;
}
a{
  cursor: pointer;
  text-decoration: none;
  color: #333;
  padding: 0;
  margin: 0;
}
</style>
