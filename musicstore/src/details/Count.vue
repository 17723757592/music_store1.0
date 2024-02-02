<template>
    <!-- 对商品计数加减操作功能模块 -->
    <div class="count-box">
        <div class="u-number">
            <a class="u-btn" href="javascript:" @click="jian(id)"><i :style="{backgroundPositionX:'-38px',backgroundPositionY:'-534px'}"></i></a>
            <span class="tot"><input type="text" v-model="put" @blur="changeNumber({id,put})"></span>
            <a class="u-btn" href="javascript:" @click="JIA(id)"><i :style="{backgroundPositionX:'0px',backgroundPositionY:'-534px'}"></i></a>
        </div>
    </div>
</template>

<script>
import {mapActions,mapMutations,mapGetters} from 'vuex';

export default {
    name:'CountNumber',
    props:['id'],
    data(){
        return{
            put:'',
            // countNumber:''
        }
    },
    methods: {
        ...mapActions('cart', ['jian','changeNumber']),
        ...mapMutations('cart',['JIA',]),
    },
    computed:{
        countNumber:{
            get(){
                return this.getShoppingCartNumber(this.id).number || 1
            },
            set(val){
                this.put = val
            }
        },
        ...mapGetters('cart', ['getShoppingCartNumber'])
    },
    watch:{ 
        countNumber:{
            immediate:true,
            deep:true,
            handler(val){
                this.put = val
            }
        },
        put:{
            deep:true,
            handler(newVal){
                // sessionStorage.setItem('number',newVal)
                this.countNumber = newVal
            }
        }
    },

}
</script>

<style lang="less">
.count-box{
    overflow: hidden;
    .u-number{
        float: left;
        width: 132px;
        height: 30px;
        border: 1px solid #e5e5e5;
        border-left: none;
        .u-btn{
            float: left;
            width: 34px;
            height: 30px;
            border-left: 1px solid #e5e5e5;
            i{
                position: relative;
                left: 3px;
                top: 1px;
                display: block;
                width: 100%;
                height: 100%;
                overflow: hidden;
                background: url(../assets/icon.png) no-repeat
            }
        }
        .tot{
            float: left;
            width: 59px;
            height: 30px;
            border-left: 1px solid #e5e5e5;
            input{
                width: 100%;
                margin: 0;
                padding: 0;
                border: none;
                font-size: 14px;
                height: 30px;
                line-height: 30px;
                text-align: center;
            }
        }
    }
}
</style>