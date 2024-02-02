<template>
    <!-- 首页主页面  -->
    <div class="globalhome">
        <div class="gmain">
            <div>
                <div class="modules">
                    <div class="module" v-for="(module,index) in modulesList" :key="index" :style="index == 0 ? {marginRight:'16px'} : ''">
                        <router-link :to="{name:module.name,}"><img :src="module.img" alt="modules"></router-link>
                    </div>
                </div>
                <div class="recommend goodsblock">
                    <span class="text">好物推荐</span>
                    <div>
                        <ul class="recmdlist">
                            <li class="recmditem" v-for="(item,index) in recommendData" :key="item.id" :style="(index+1) % 4 == 0 ? {marginRight:'0px'}:''">
                                <router-link :to="{
                                    name:'detail',
                                    params:{
                                        title:item.title,
                                        id:item.id,
                
                                    }}">
                                    <div>
                                    <a class="imgbox"  href="javascript:"><img class="productimg" :src="item.show_picture" alt=""></a>
                                    <div class="content">
                                        <h3>
                                            <span v-show="item.discount" class="tag"><em>{{item.discount}}</em></span>&nbsp;
                                            <a :href="item.href">{{item.title }}</a>
                                        </h3>
                                        <p class="f-thide">￥<em>{{item.price}}</em></p> 
                                    </div>
                                </div>
                                </router-link>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="digital-album" @click="toDataAlbum">
                    <div class="cnt">
                        <div>
                            <span><i></i>数字专辑</span>
                            <p class="f-thide">数字专辑</p> 
                            <a href="">立 即 购 买></a>
                        </div>
                    </div>
                    <div class="album-img">
                        <img class="img-left" src="http://p2.music.126.net/Wz78eriM3xyUnOKT3BRtCA==/109951168771859024.jpg?param=120y120" alt="">
                        <img class="img-m" src="http://p2.music.126.net/OUmlP_yxMvQpVY5zTcLeTg==/109951168761663302.jpg?param=120y120" alt="">
                        <i class="img-right"></i>
                    </div>
                </div>
                <div class="goodsblock">
                    <span class="text">热门商品</span>
                    <div>
                        <ul class="recmdlist">
                            <li class="recmditem" v-for="(item,index) in hotData" :key="item.id" :style="(index+1) % 4 == 0 ? {marginRight:'0px'}:''">
                               <router-link :to="{
                                name:'detail',
                                params:{
                                    title:item.title,
                                    id:item.id,
            
                                }}">
                                    <div>
                                        <a class="imgbox"  href="javascript:''"><img class="productimg" :src="item.show_picture" alt=""></a>
                                        <div class="content">
                                            <h3>
                                                <span v-show="item.discount" class="tag"><em>{{item.discount}}</em></span>&nbsp;
                                                <a :href="item.href">{{item.title }}</a>
                                            </h3>
                                            <p class="f-thide">￥<em>{{item.price}}</em></p> 
                                        </div>
                                    </div>
                               </router-link>
                            </li>
                        </ul>
                    </div>
                </div>
                <div></div>
            </div>
        </div>
        <div class="gtop"></div>
    </div>
</template>

<script>
import {mapState} from 'vuex'
import getRecommendList from '@/api/recommend';
import getHotList from '@/api/hot';
export default {
    name:'GlobalName',
    props:['modulesList'],
    data(){
        return{
            recommendData:'',
            hotData:''
        }
    },
    computed:{
        ...mapState('home',['productionData'])
    },
    methods:{
        toDataAlbum(){
            this.$router.push({name:'album'})
        }
    },
    async created(){
        await getRecommendList().then(res=>{
            this.recommendData = res.data.data
            console.log(this.recommendData);
        }),
        await getHotList().then(response=>{
            this.hotData = response.data.data
            console.log(this.hotData);
        })
    },
}
</script>

<style>
.globalhome{
    padding-bottom: 160px;
    width: 1100px;
    min-height: 750px;
    margin: 0 auto;
    background: #fff;
    }
.gmain{
    width: 100%;
    margin: 0;
}
.modules{
    width: 100%;    
    height: 300px;
    margin-top: 40px;
}
.module{
    float: left;
    width: 542px;
    height: 300px;
}
.recommend{ 
    min-height: 816px;
}
.goodsblock{
    margin-top: 50px;
    width: 100%;
    height: auto;
}
.text{
    font-weight: bold;
    font-size: 24px;
    color: #333;
}
.recmdlist{
    margin-top: 20px;
    overflow: hidden;
    width: 100%;
    height: auto;
}
.recmditem{
    float: left;
    position: relative;
    width: 263px;
    list-style: none;
    height: 382px;
    margin-right: 16px;
}
.imgbox{
    width: 263px;
    display: block;
    position: relative;
    height: 263px;
    background-color: #f9f9f9;
    cursor: pointer;
}
.productimg{
    width: 263px;
    height: 263px;
    display: block;
}
.content{
    margin-top: 10px;
}
.content h3{
    font-size: 14px;
    line-height: 18px;
    font-weight: normal;
    color: #333;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
}
.content p{
    font-size: 16px;
    color: #d33a31;
    border: 0;
    padding-top: 4px;
}
.content h3 a:hover{
    text-decoration: underline;
}
.f-thide{
    word-wrap: normal;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.tag{
    border: 1px solid #d74d45;
    overflow: hidden;
    box-sizing: border-box;
    line-height: 19px;
    padding: 0 3px;
    border-radius: 1px;
    color: #d74d45;
    font-size: 12px;
}
em{
    font-style: normal;
    text-align: left;
    font-size: inherit;
    }
.digital-album{ 
    position: relative;
    width: 100%;
    height: 180px;
    background-color: #f9f9f9;
    cursor: pointer;
    margin-top: 10px;
}
.cnt{
    width: 700px;
    height: 180px;
    margin: 0 20px 0 60px;
}
.cnt div{
    position: relative;
    float: left;
    text-align: left;
}
.cnt span{
    display: block;
    padding-top: 28px;
    font-size: 32px;
    font-weight: bold;
    color: #000000;
}
.cnt a{
    display: block;
    margin-top: 18px;
    font-size: 24px;
    font-weight: bold;
    color: #000000;
    text-decoration: none;
}
.cnt p{
    position: relative;
    margin-top: 9px;
    font-size: 16px;
    color: rgba(0, 0, 0, 0.7);
}
.cnt span i{
    position: relative;
    top: 5px;
    margin-right: 10px;
    display: inline-block;
    width: 32px;
    height: 32px;
    background: url(../../assets/digitalicon.png) no-repeat;
}
.album-img{
    top: 30px;
    right: 50px;
    width: 210px;
    height: 120px;
    position: absolute;
}
.img-left{
    position: absolute;
    top: 15px;
    left: 0;
    width: 100px;
    height: 100px;
}
.img-m{
    position: absolute;
    z-index: 99;
    top: 0;
    left: 60px;
    width: 120px;
    height: 120px;
}
.img-right{
    position: absolute;
    top: 0;
    left: 175px;
    width: 35px;
    height: 120px;
    border: none;
    background: url(../../assets/pointlist.png) no-repeat;
    background-position: 0px -73px
}
</style>