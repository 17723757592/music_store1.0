<template>
    <!-- 主要信息展示模块 -->
    <div class="g-main">
        <div class="n-detail">
            <div class="f-cb" :style="{minHeight:'530px',overflow:'hidden'}">
                <div class="img-display" :style="{float:'left',}">
                    <div class="pic">
                        <div class="imgbox">
                        <img :src=showImg alt=""></div>
                    </div>
                    <div class="smallnav">
                        <ul>
                            <li v-for="(item,index) in detailnav" :key="index">
                                <img :src="item" alt="" @click="changeShow(item)">
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="n-info">
                    <div class="basic">
                        <h2>{{titleR}}</h2>
                        <p class="price">
                            <span>￥</span>
                            <em>{{ detailData.price}}</em>
                        </p>
                        <div class="standard">
                            <div class="select-box">
                                <div class="detailtext">规格:</div>
                                <ul>
                                    <li v-for="(standard,index) in detail_standard" :key="index" >
                                        <p>{{ standard }}</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="count">
                            <div class="count-box">
                                <p class="detailtext">数量:</p>
                                <!-- <CountNumber></CountNumber> -->
                                <div class="cnt-box">
                                    <div class="u-number">
                                        <a class="u-btn" href="javascript:" @click="jian"><i :style="{backgroundPositionX:'-38px',backgroundPositionY:'-534px'}"></i></a>
                                        <span class="tot"><input type="text" v-model="put">{{ id }}</span>
                                        <a class="u-btn" href="javascript:" @click="JIA"><i :style="{backgroundPositionX:'0px',backgroundPositionY:'-534px'}"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="services">
                        <p class="detailtext">服务:</p>
                        <div class="servecnt">
                            <a class="serveitem" href="javascript:">{{'7天无理由退货' }}</a>
                        </div>
                    </div>
                    <p class="buyit">
                        <a class="buybtn buybtn1" href="javascript:" @click="buyNow">立即购买</a>
                        <a class="buybtn tocar buybtn1" href="javascript:" @click="addProduction">加入购物车</a>
                    </p>
                </div>
            </div>
            <div class="n-contend">
                <div class="n-contend-left">
                    <h2 class="headline">商品详情</h2>
                    <div class="n-describe">
                        <div class="j-flag">
                           <img v-for="(item,index) in detailimg" :key="index" :src="item" alt="">
                           <div>
                                <p v-for="(item,index) in detail_content" :key="index">{{ item }}</p>
                                <p><br></p>
                                <p><span>购买须知</span></p>
                                <p><span>商品购买成功后，会在2个工作日内发货，法定节假日顺延，请在确认商品完好后再签收。</span></p>
                                <p><span>若存在质量问题，请务必在签收后7天内联系客服。</span></p>
                                <p><span>客服账号：向【云音乐客服】账号私信反馈</span></p>
                            </div>
                        </div>
                    </div>
                    <div></div>
                </div>
                <div class="hotrecommned">
                    <h2 class="headline normal">热门商品</h2>
                    <div class="m-product">
                        <ul class="recmdlist">
                            <li class="hotitem" v-for="(item,index) in productionData.recommend" :key="item.data_id" v-show="index < 4" @click="toRecommend(item)">
                                <!-- <router-link :to="{
                                    name:'detail',
                                    params:{
                                        title:item.contend,
                                        id:item.data_id,
                                    }}"> -->
                                    <div>
                                        <a class="picbox"  :href="item.href"><img :src="item.img" alt=""></a>
                                        <div class="content">
                                            <h3>
                                                <span v-show="item.discount" class="tag"><em>{{item.discount}}</em></span>&nbsp;
                                                <a :href="item.href">{{item.contend }}</a>
                                            </h3>
                                            <p class="f-thide">￥<em>{{item.money}}</em></p> 
                                        </div>
                                    </div>
                                <!-- </router-link> -->
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div ref="topbar" class="topbar" v-show="isVisable">
                <div class="barbox">
                    <div class="imgbox"><img :src="detailnav[0]" alt=""></div>
                    <div class="barmsg">
                        <p>{{ titleR }}</p>
                        <span :style="{color:'#d33a31'}">{{detailData.price}}</span>
                    </div>
                    <p class="buyit" :style="{float:'right'}">
                        <a class="buybtn buybtn2" href="javascript:" @click="buyNow">立即购买</a>
                        <a class="buybtn tocar buybtn2" href="javascript:" @click="addProduction">加入购物车</a>
                    </p>
                </div>
            </div>
            <div></div>
        </div>
    </div>
</template>

<script>
import getDetail from '@/api/detail';
// import {nanoid} from 'nanoid'
import {mapState, mapMutations,} from 'vuex';
// import createOrderNumber from '@/utils/create_order_number';
// import mixin from '../mixin.js';
// import CountNumber from './Count.vue'
export default {    
    name:'DeBody',
    props:['titleR','id'],
    // components:{CountNumber},
    // mixins:[mixin],
    data(){
        return{
            isVisable:false,
            number:1,
            put:'',
            countNumber:1,
            showImg:'',
            detailData:'',
            detailnav:'',
            detailimg:'',
            detail_content:'',
            detail_standard:''
        }
    },
    methods:{
        ...mapMutations('cart', ['unshiftShoppingCart']),
        toRecommend(item){
            this.$router.push({name:"detail",params:{
                title:item.contend,
                id:item.data_id,
            }})
        },
        JIA(){
            this.countNumber++
        },
        jian(){
            if(this.countNumber > 1){
                this.countNumber--
            }
        },
        buyNow(){
            console.log(this.detailData.price);
            const goods = {
                    commodity_id:this.detailData.id,
                    brand_id:this.detailData.brand_id,
                    category_id:this.detailData.category_id,
                    title:this.titleR,
                    price:this.detailData.price,
                    img:this.detailnav[0],
                    number:this.countNumber,
                    check:true,
                }
            this.unshiftShoppingCart(goods)
            this.$router.push({name:'bus',})
        },
        addProduction(){
            // 拿到某一商品数量进一步放进购物车
            const goods = {
                    commodity_id:this.detailData.id,
                    brand_id:this.detailData.brand_id,
                    category_id:this.detailData.category_id,
                    title:this.titleR,
                    price:this.detailData.price,
                    img:this.detailnav[0],
                    number:this.countNumber,
                    check:true,
                }
            this.unshiftShoppingCart(goods)
            // store刷新数据丢失，存入浏览器，，写在app组件里
            this.$message({
                showClose: true,
                message: '成功加入购物车',
                type: 'success'
                });
            
        },
        changeShow(item){
            this.showImg = item
        },
        windowScrollListener() {
            var scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
            // console.log(scrollTop);
            if (scrollTop >= 555) {
                this.isVisable = true; 
            }
            if (scrollTop < 555) {
                this.isVisable = false; 
            }
        },
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
    computed:{
        ...mapState('home',['productionData']),   
    //     ...mapGetters('home', ['number'])

    },
    async created(){
        window.addEventListener('scroll', this.windowScrollListener);
        await getDetail(Number(this.id)).then(res=>{
            this.detailData = res.data.data
            console.log(this.detailData);
            let pictures = this.detailData.pictures.split("*")
            let detailnav = pictures[0].replace("[","").replace("]","")
            let detailimg = pictures[1].replace("[","").replace("]","")
            // data = this.recommendData.pictures[0].replace("]","")
            this.detailnav = detailnav.split(",")
            this.detailimg = detailimg.split(",")
            this.showImg = this.detailnav[0]
            this.detail_content =this.detailData.content.split("*")
            this.detail_standard = this.detailData.standard.split("*")
            console.log(this.detail_standard,this.detail_content);
        });
    //     this.goods = this.productionData.goods.find((item) =>{
    //         return item.id == this.id
    // })
        // this.$bus.$on('takeNumber',this.demo)
    },
    mounted(){
        console.log(typeof(this.id));
    },
    destroyed(){
        window.removeEventListener('scroll', this.windowScrollListener);
        // this.$bus.$off('takeNumber')
    }
}
</script>
<style lang="less" scoped>
.detailtext{
    height: 30px;
    line-height: 30px;
    color: #999;
    float: left;
    margin-right: 30px;
    font-size: 12px;
}
.headline{
    height: 30px;
    line-height: 30px;
    padding-bottom: 17px;
    margin-bottom: 20px;
    border-bottom: 1px solid #000;
    font-size: 22px;
}
.buyit{
        overflow: hidden;
        .buybtn1{
            width: 170px;
            height: 50px;
            line-height: 47px;
            margin-top: 30px;
        }
        .buybtn2{
            width: 160px;
            height: 40px;
            line-height: 37px;
            margin-top: 14px;
        }
        .buybtn{
            float: left;
            box-sizing: border-box;
            font-size: 18px;
            border: 2px solid #d33a31;
            color: #d33a31;
            background-color: white;
            text-align: center;
            margin-right: 10px;
        }
        .tocar{
            background-color:#d33a31;
            color: white;
        }
            }
.g-main{
    width: 100%;
    text-align: left;
    margin: 0;
    .n-detail{
        padding-top: 5px;
        min-height: 600px;
        .f-cb{
            .img-display{
            .pic{
                box-sizing: border-box;
                width: 440px;
                position: relative;
                height: 440px;
                .imgbox{
                    position: relative;
                    overflow: hidden;
                    width: 100%;
                    height: 100%;
                    background: #f9f9f9;
                    img{
                        width: 100%;
                        height: 100%;
                    }
                }
            }
            .smallnav{
                        position: relative;
                        z-index: 1;
                        zoom: 1;
                        width: 440px;
                        height: 80px;
                        margin-top: 10px;
                        overflow: hidden;
                        ul{
                            width: 3000px;
                            transition: 0.3s;
                            overflow: hidden;
                            li{
                                box-sizing: border-box;
                                float: left;
                                width: 80px;
                                height: 80px;
                                margin-right: 10px;
                                background: #f9f9f9;
                                img{
                                    width: 100%;
                                    height: 100%;
                                }
                            }
                        }
                    }
            }
            .n-info{
            width: 580px;
            float: right;
            .basic{
                position: relative;
                h2{
                    line-height: 34px;
                    color: #333;
                    font-weight: normal;
                    font-size: 24px;
                }
                .price{
                        margin: 20px 0;
                        font-size: 14px;
                        span{
                            font-size: 30px;
                            margin-right: 3px;
                            color: #d33a31;
                        }
                        em{
                            margin-right: 4px;
                            font-size: 30px;
                            color: #d33a31;
                        }    
                }
                .standard{
                    .select-box{
                        margin: 16px -16px 0 -8px;
                        border: 1px solid #fff;
                        padding: 0 7px;
                        overflow: hidden;
                        ul{
                            overflow: hidden;
                            width: 510px;
                            float: left;
                            margin-bottom: -8px;
                            li{
                                box-sizing: border-box;
                                height: 30px;
                                position: relative;
                                margin-bottom: 10px;
                                line-height: 27px;
                                font-size: 12px;
                                float: left;
                                margin-right: 10px;
                                padding: 0 20px;
                                border: 1px solid #e5e5e5;
                                background: #fff;
                                cursor: pointer;
                            }
                        }
                    }
                }
                .count{
                    .count-box{
                        margin-top: 17px;
                        overflow: hidden;
                        // .u-number{
                        //     float: left;
                        //     width: 132px;
                        //     height: 30px;
                        //     border: 1px solid #e5e5e5;
                        //     border-left: none;
                        //     .u-btn{
                        //         float: left;
                        //         width: 34px;
                        //         height: 30px;
                        //         border-left: 1px solid #e5e5e5;
                        //         i{
                        //             position: relative;
                        //             left: 3px;
                        //             top: 1px;
                        //             display: block;
                        //             width: 100%;
                        //             height: 100%;
                        //             overflow: hidden;
                        //             background: url(../assets/icon.png) no-repeat
                        //         }
                        //     }
                        //     .tot{
                        //         float: left;
                        //         width: 59px;
                        //         height: 30px;
                        //         border-left: 1px solid #e5e5e5;
                        //         input{
                        //             width: 100%;
                        //             margin: 0;
                        //             padding: 0;
                        //             border: none;
                        //             font-size: 14px;
                        //             height: 30px;
                        //             line-height: 30px;
                        //             text-align: center;
                        //         }
                        //     }
                        // }
                    }
                }
            }
            .services{
                    position: relative;
                    margin-top: 17px;
                    .servecnt{
                        cursor: pointer;
                        margin-left: 69px;
                        .serveitem{
                            display: inline-block;
                            position: relative;
                            line-height: 30px;
                            font-size: 12px;
                            margin-right: 28px;
                            color: #666;
                        }
                        .serveitem::before{
                            content: "";
                            position: absolute;
                            top: 13px;
                            left: -8px;
                            width: 3px;
                            height: 3px;
                            border-radius: 100%;
                            background-color: #d33a31;
                        }
                    }
            }
            }
        }
        .n-contend{
            overflow: hidden;
            margin-top: 66px;
            .n-contend-left{
                float: left;
                width: 700px;
                .n-describe{
                    float: left;
                    width: 700px;
                    .j-flag{
                        img{
                            display: block;
                            width: 100%;
                            height: auto;
                        }
                        p{
                            font-size: 14px;
                            line-height: 18px;
                            padding: 5px 0;
                            color: #666;
                        }
                    }
                }
            }
            .hotrecommned{
                float: right;
                width: 340px;
                .normal{
                    font-weight: normal;
                }
                .m-product{
                    .hotitem{
                        float: left;
                        width: 100%;
                        height: 100px;
                        position: relative;
                        padding-right: 16px;
                        margin-bottom: 40px;
                        .picbox{
                            float: left;
                            height: 100px;
                            width: 100px;
                            background-color: #f9f9f9;
                            position: relative;
                            img{
                                display: block;
                                height: 100%;
                                width: 100%;
                            }
                        }
                    }
                }
            }
        }
        .topbar{
            position: fixed;
            left: 0;
            top: 0;
            width: 100%;
            height: 70px;
            background-color: #fff;
            z-index: 999;
            .barbox{
                overflow: hidden;
                position: relative;
                width: 1100px;
                height: 70px;
                margin: 0 auto;
                .imgbox{
                    height: 50px;
                    width: 50px;
                    margin-top: 10px;
                    float: left;
                    background: #f9f9f9;
                    img{
                        display: block;
                        width: 100%;
                        height: 100%;
                    }
                }
                .barmsg{
                    width: 634px;
                    height: 48px;
                    float: left;
                    padding: 11px 0;
                    padding-left: 16px;
                    margin-right: 60px;
                    p{
                        font-size: 16px;
                        height: 26px;
                        line-height: 26px;
                    }
                }
            }

        }
    }
}
</style>