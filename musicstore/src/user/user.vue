<template>
    <!-- 登陆后个人中心页面 -->
    <div class="per-center">
        <SortTop :bread="perNav">
        </SortTop>
        <div class="per-navlist">
            <el-tabs :tab-position="tabPosition" style="height: 160px;" v-model="number"> 
                <el-tab-pane v-for="(item,index) in perNavList" :key="index" label="item.nav" >
                    <div slot="label" @click="changeNav(item.nav,item.name,item.number)">
                        {{item.nav}}
                    </div>
                    <!-- <router-link :to="{name:'perorder'}"></router-link> -->
                </el-tab-pane>
            </el-tabs>
        </div>
        <div class="childbox">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
import SortTop from '../views/SortTop.vue'
export default {
    name:'PersonalCenter',
    props:['bread','confirmAddress'],
    components:{SortTop},
    data(){
      return {
        tabPosition: 'left',
        // 该组件的index是字符型
        number:sessionStorage.getItem("index") || '0',
        perNav:sessionStorage.getItem("report") || this.bread,
        perNavList:[
        {nav:'我的订单',name:'perorder',number:0, },
        {name:'perdiscount',nav:"我的优惠券",number:1},
        {name:'peraddress',nav:"我的收货地址",number:2},
        {name:'customersevice',nav:"在线客服",number:3}]
      };
    },
    methods:{
        changeNav(nav,name,number){
            this.perNav = nav,
            this.$router.push({
                name:name,
            }),
            sessionStorage.setItem("report",nav);
            //将所需要展示的tab标签的index进行记录
            sessionStorage.setItem("index",number);
        },
    },
    beforeRouteLeave(to, from, next){
        sessionStorage.removeItem("report")
        sessionStorage.removeItem("index")
        next()
    },
}
</script>

<style lang="less" scoped>
.childbox{
    float: left;
    min-height: 480px;
}
.per-center{
    width: 1100px;
    margin: 0 auto;
    overflow: hidden;
    background: #fff;
    padding-bottom: 160px;
    .per-navlist{
        float: left;
    }
}
</style>