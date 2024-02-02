<template>
    <!-- ip周边，数码影音等导航区 -->
    <div>
        <div class="gtab">
            <div class="hometab">
                <ul>
                    <li class="tab" v-for="(tab,index) in tabList" :key="index">
                        <!-- <a :href="tab.href"> -->
                        
                        <router-link :to="{
                            name:tab.name,
                            params:{
                                bread:tab.title
                                }
                            }">
                            <img :src="tab.ico" alt="tab-icos">
                            <span>{{tab.title}}</span>
                        </router-link>
                            
                        <em class="line" v-if="index !== tabList.length-1"></em>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
// import jifen from '../../assets/jifen.png'
import getCategory from '@/api/category';
export default {
    name:'SortTab',
    data(){
        return{
            tabList:'',
        }   
    },
    async created(){
        await getCategory().then(res=>{
            this.tabList = res.data.data
        })
        console.log(this.tabList);
    },
}
</script>

<style>
.gtab{
    width: 100%;
    height: 80px;
    position: relative;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
}
.hometab{
    width: 1100px;
    margin: 0 auto;
}
.hometab ul{
    width: 100%;
    height: 80px;
}
/* .hometab ::after{
    clear: both;
    content: ".";
    display: block;
    height: 0;
    visibility: hidden;
} */
.hometab ul li{
    list-style: none;
} 
.hometab ul li a{
    float: left;
    width: 250px;
    padding: 0 10px;
    height: 80px;
    text-align: center;
    font-size: 0;
}
.line{
    display: inline-block;
    height: 48px;
    width: 1px;
    margin: 16px 0 16px 0;
    background-color: #000000;
    opacity: 0.1;
}
.hometab ul li img{
    display: inline-block;
    width: 48px;
    height: 48px;
    vertical-align: top;
    padding-top: 16px;
    border: 0;
}
.tab{
    float: left;
    width: 275px;
    height: 80px
}
.tab span{
    display: inline-block;
    max-width: 190px;
    height: 80px;
    padding-left: 12px;
    line-height: 80px;
    font-size: 14px;
    font-weight: bold;
    color: #333333;
}
</style>