<template>
    <!-- 购物车操作页面 -->
    <div>
        <div class="goods-list">
            <div class="list-head">
                <div class="col check"><input type="checkbox" v-model="allCheck">全选</div>
                <div class="col img"> &nbsp;</div>
                <div class="col name">商品名称</div>
                <div class="col price">单价</div>
                <div class="col num">数量</div>
                <div class="col total">小计</div>
                <div class="col action">操作</div>
            </div>
            <div class="list-body">
                <div class="list-item" v-for="item in shoppingCart" :key="item.id">
                    <div class="item-box">
                        <div class="item-tabel">
                            <div class="item-row" :style="{clear:'both'}">
                                <div class="col check"><input type="checkbox" :checked="item.check" @click="changeCheck(item.id)">&nbsp;&nbsp;</div>
                                <div class="col img">
                                    <a href="javascript:">
                                        <img :src= item.img alt="" :style="{width:'80px',height:'80px'}"></a></div>
                                <div class="col name">
                                    <h3><a href="javacsript:">{{ item.title }}</a></h3>
                                </div>
                                <div class="col price">{{ item.price }}</div>
                                <div class="col num">
                                    <CountNumber :id="item.id"></CountNumber>
                                </div>
                                <div class="col total">{{item.price * item.number}}</div>
                                <div class="col action" @click="deleteShoppingCart(item.id)"><button>x</button></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="to-pay" v-if="shoppingCart.length > 0">
                <div class="section-left">
                    <router-link :to="{name:'home'}">
                        <a class="back-shopping" href="javascript:">继续购物
                    </a></router-link>
                    <span class="total-item">已选择
                        <i>{{ checkedNumber }}</i>件
                    </span>
                </div>
                <span class="total-price">合计：
                    <em>{{getTotalPrice}}</em>元
                    <a class="pay-money" href="javascript:" @click="toOrder">去结算</a>
                </span>
            </div>
            <div v-else>
                <h2>您还没有选择商品快去看看吧</h2>
            </div>
        </div>
        <div class="recommend-box">
            <div class="recommend goodsblock">
            <span class="text">好物推荐</span>
            <div>
                <ul class="recmdlist">
                    <li class="recmditem" v-for="(item,index) in productionData.recommend" :key="item.data_id" :style="(index+1) % 4 == 0 ? {marginRight:'0px'}:''">
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
                                        <span v-show="item.discount" class="tag"><em>{{item.discount}}</em></span>&nbsp;
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
    </div>
</template>

<script>
import CountNumber from '../details/Count.vue'
import {mapState, mapMutations, mapGetters, mapActions} from 'vuex'
export default {
    name:'BusName',
    components:{CountNumber},
    computed:{
        ...mapState('home',['productionData']),
        ...mapState('cart',['shoppingCart']),
        ...mapGetters('cart',['getTotalPrice','checkedNumber']),
        allCheck:{
            get(){
                return this.$store.state.cart.shoppingCart.length === this.checkedNumber && this.$store.state.cart.shoppingCart.length > 0
            },
            set(value){
                this.changeAllCheck(value)
            }
           
        }
    },
    methods:{
        ...mapMutations('cart',['changeCheck','deleteShoppingCart']),
        ...mapActions('cart',['changeAllCheck']),
        toOrder(){
            if (this.checkedNumber > 0) {
                this.$store.dispatch('user/check').then(res => {
                    if (res) {
                        this.$router.push({name:'order'})
                    } else {
                        this.helpLogin()
                    }
                })
            } else {
                this.$message.warning('请选择需要结算的商品')
            }
        },

        helpLogin(){
            this.$confirm('你还没有登录，请登录吧', '登录提示', { type: 'warning' }).then(() => {
                this.$store.dispatch('user/login', true)
            }).catch(() => {
                return 0
            })
        },
    },
    mounted(){
        // console.log('start')
        // Promise.resolve().then(() => {
        //     console.log('promise1')
        //     setTimeout(() => {
        //         console.log('timer2')
        //     }, 0)
        // })

        // setTimeout(() => {
        //     console.log('timer1')
        //     Promise.resolve().then(() => {
        //         console.log('promise2')
        //     })
        // }, 0)
        // console.log('end')

    }
}
</script>

<style lang="less" scoped>
.col{
    float: left;
}
.check{
        width: 110px;
        text-align: left;
        input{
            position: relative;
            display: inline-block;
            width: 18px;
            height: 18px;
            line-height: 18px;
            margin-left: 24px;
            font-size: 20px;
            vertical-align: middle;
            top: -1px;
            cursor: pointer;
            margin-right: 15px;
        }
        }
.img{
    width: 120px;
}
.name{
    width: 380px;
    text-align: left;
}
.price{
    width: 130px;
}
.num{
    width: 133px;
    // margin-top:5px;
}
.total{
    width: 100px;
}
.action{
    width: 80px;
}
.goods-list{
    width: 1100px;
    margin:0 auto;
    .list-head{
        line-height: 70px;
        color: #424242; 
        overflow: hidden;
    }
    .list-body{
        .list-item{
            .item-box{
                padding: 15px 26px 15px 0;
                border-top: 1px solid #e0e0e0;
                .item-tabel{
                    .item-row{
                        // overflow: hidden;
                        height: 85px;
                        position: relative;
                        // display: table-cell;
                        // vertical-align: middle;
                        .img{
                            width: 80px;
                            height: 80px;
                            padding-right: 40px;
                            overflow: hidden;
                        }
                        .name{
                            width: 380px;
                            text-align: left;
                            h3{
                                margin-top: 8px;
                                margin-bottom: 8px;
                                font-size: 18px;
                                font-weight: 400;
                                text-overflow: ellipsis;
                                white-space: nowrap;
                                overflow: hidden;
                                width: 380px;
                                margin: 0;
                            }
                        }
                        // .price{
                        //     width: 130px;
                        // }
                        .num{
                            margin-top: -3px;
                        }
                        .total{
                            color:  #d33a31;
                            font-size: 16px;
                        }
                        .action{
                           button{
                            border-radius: 50%;  
                            color:black;
                            background-color: #fff;
                            font-size: 16px;
                            }
                        }
                    }
                }
            }
        }
    }
    .to-pay{
        height: 50px;
        text-align: right;
        background-color: #fff;
        overflow: hidden;
        margin: 20px 0;
        transition: background .3s ease,top .3s ease;
        position: relative;
        .section-left{
            float: left;
            text-align: right;
            .back-shopping{
                line-height: 50px;
                margin-left: 32px;
                color: #757575;
                text-decoration: none;
            }
            .total-item{
                margin-left: 16px;
                padding-left: 16px;
                border-left: 1px solid #eee;
                color: #757575;
                i{
                    color:  #d33a31;
                    font-style: normal;
                }
            }
        }
        .total-price{
            padding-left: 13px;
            line-height: 50px;
            color:#d33a31;
            em{
                font-style: normal;
                font-size: 30px;
            }
            .pay-money{
                width: 200px;
                height: 50px;
                display: inline-block;
                line-height: 50px;
                text-align: center;
                font-size: 18px;
                margin-left: 50px;
                vertical-align: top;
                background: #d33a31;
                border-color: #d33a31;
                color: #fff;
            }
        }
    }
}
.recommend-box{
    width: 1100px;
    margin: 0 auto;
    padding-bottom: 160px;
}
</style>