<template>
    <!-- 商品详情页 -->
    <div class="g-bg g-footer">
        <DeSort :titleR="titleR" :bread="bread" ></DeSort>
        <DeBody :titleR="titleR" :id="id" :goods="goods"></DeBody>
    </div>
</template>

<script>
// import mixin from '../mixin.js';
// import axios from "axios"
import DeSort from './DeSortTab.vue'
import DeBody from './DeBody.vue'

import { getProductList } from '@/api/product'

export default {
    name:"DetailName",
    props:['titleR','id', 'bread'],
    // mixins:[mixin],
    components:{DeSort,DeBody},
    data() {
        return {
           goods: {}
        }
    },
    methods:{
        addItem(){
            getProductList().then(response => {
                const goods = response.data.goods && Array.isArray(response.data.goods) ? response.data.goods.filter(row => this.id === row.id) : []
                this.goods = goods.length > 0 ? goods[0] : {}
            }).catch(error => {
                console.log(error);
            })
        },
    },
    created(){
        this.addItem()
    },
    mounted(){
        console.log(this.goods);
    }
}
</script>

<style>
</style>