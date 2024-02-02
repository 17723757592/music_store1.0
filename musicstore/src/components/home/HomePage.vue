<template>
<!-- 首页面主要展示区域 -->
    <div>
        <ImageShow></ImageShow>
        <SortTab></SortTab>
        <GlobalName :modulesList="modulesList"></GlobalName>
    </div>
</template>

<script>
import ImageShow from './ImageShow.vue'
import SortTab from './SortTab.vue'
import GlobalName from './Global.vue'
export default {
    name:'HomePage',
    data(){
        return{
            // 耳机、银魂周边
            modulesList:[
                {href:'javascript:',img:'http://p4.music.126.net/kQqf40w-NFhLXIksQPgSwg==/109951164207184328.jpg',name:'earphone'},
                {href:'javascript:',img:'http://p4.music.126.net/QtFPuBnRPFatpnGsyNJYhw==/109951163973446450.jpg',name:'hotperipheral' }
        ]
        }
    },
    components: {
        ImageShow,
        SortTab,
        GlobalName,
    }
}
</script>

<style>

</style>