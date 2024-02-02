<template>
    <!-- 分类页面包屑导航栏 -->
    <div class="mbread">
        <div class="block">
            <span @click="$router.push({name:'home'})"><a href="javascript:">首页</a></span>
            <span class="pointer"><li></li>{{ bread }}</span>
        </div>
    </div>
</template>

<script>
export default {
    name:'SortTop',
    props:['bread'],
}
</script>

<style>
.mbread{
    min-height: 30px;
    margin-bottom: 15px;
    border-bottom: 1px solid #333;
}.block{
    padding: 30px 0 19px 0;
    text-align: left;
    font-size: 18px;
    font-weight: 600;
}
.pointer{
    font-size: 16px;
    color: #999;
}
.pointer li{
    position: relative;
    top: 7px;
    display: inline-block;
    width: 16px;
    height: 26px;
    margin: 0 4px 0 8px;
    background: url(../assets/ar.png) no-repeat left center;
}
</style>