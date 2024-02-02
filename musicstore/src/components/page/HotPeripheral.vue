<template>
    <div class="g-main">
        <div class="ma">
            <div class="m-banner">
                <img src="http://p4.music.126.net/MSO6qHFIWx4GRdx2oJfgLA==/19143596951529139.jpg" alt="">
            </div>
            <div class="m-production">
                <ul class="list">
                    <!-- 用了Global中商品展示的样式 -->
                    <li class="recmditem" v-for="(item,index) in productionData.hotgoods" :key="item.data_id" :style="(index+1) % 4 == 0 ? {marginRight:'0px'}:''">
                       <router-link :to="{
                        name:'detail',
                        params:{
                            title:item.contend,
                            id:item.data_id,
                        }
                       }">
                            <div>
                                <a class="imgbox"  :href="item.href"><img class="productimg" :src="item.img" alt=""></a>
                                <div class="content">
                                    <h3>
                                        <span class="tag"><em>{{item.discount}}</em></span>&nbsp;
                                        <a :href="item.href">{{item.contend }}</a>
                                    </h3>
                                    <p class="f-thide">￥<em>{{item.money}}</em></p> 
                                </div>
                            </div>
                       </router-link>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'vuex';
export default {
    name:'HotPeripheral',
    computed:{
        ...mapState('home',['productionData'])
    },
}
</script>

<style lang="less">
     @import './main.less';
</style>