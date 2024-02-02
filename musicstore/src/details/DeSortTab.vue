<template>
    <!-- 面包屑导航模块 -->
    <div class="mbread">
        <div class="block">
            <span  @click="$router.push({name:'home'})"><a href='javascript:'>首页</a></span>
            <span v-if="bread != null" class="pointer" @click="$router.push({name:'sort', params:{bread:bread}})" :style="{cursor:'pointer'}"><li></li>{{bread}}</span>   
            <span class="pointer"><li></li>{{titleR}}</span>  
            <div class="share" :style="{cursor:'pointer',}">分享</div>
        </div>
    </div>
</template>
    
<script>
export default {
    name:'DeSort',
    props:['titleR', 'bread']
}
</script>

<style scoped>
.share{
    margin-top: 11px;
    background: url(../assets/share.png) no-repeat 0 2px;
    font-size: 16px;
    text-indent: 27px;
    float: right;
    color: #666;
}
</style>