<template>
    <!-- 标签分类板块-->
    <div class="filters">
        <div class="n-filter">
            <div class="g-wrap">
                <div class="g-inner" v-if="productionData[identify].brand">
                    <div class="tags">
                        <span class="title">品牌:</span>
                        <ul>
                            <li v-for="(brand,index) in productionData[identify].brand" :key="index" @click="keyBrand(brand,index)">
                                <a :class="index == currentBra ? 'active' : ''">{{brand}}</a></li>
                        </ul>
                        <span class="more">更多<i></i></span>
                    </div>
                    <div class="tags" v-if="productionData[identify].sort.length > 0">
                        <span class="title">分类:</span>
                        <ul>
                            <li v-for="(sort,index) in productionData[identify].sort" :key="index" @click="keySort(sort,index)">
                                <a :class="index == currentSor ? 'active' : ''">{{sort}}</a></li>
                        </ul>
                    </div>
                    <div class="tags" :style="{borderBottom:'none'}">
                        <span class="title">价格:</span>
                        <ul>
                            <li v-for="(price,index) in productionData[identify].price" :key="index" @click="keyPri(index)">
                                <a :class="index == currentPri ? 'active' : ''">{{price}}</a></li>
                            <li>
                                <span class="txt lf">自定义</span>
                                <span>
                                    <input class="butstyle" v-model="bottomPrice" type="text" placeholder="bottom price">
                                </span>
                                <span>--</span>
                                <span>
                                    <input class="butstyle" v-model="topPrice" type="text" placeholder="   top price">
                                </span>
                            </li>
                            <li><span class="btn-sure" @click="getKeyPri" :style="(topPrice!='' && bottomPrice!='') ? {backgroundColor:'#000'} : ''">确定</span></li>
                        </ul> 
                     </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {mapState} from 'vuex';
export default {
    name:'FiltersName',
    props:['bread'],
    data(){
        return{
            currentBra:-1,
            currentSor:-1,
            currentPri:-1,
            bottomPrice:'',
            topPrice:'',
            identify:'',
        }
    },
    created(){
        this.identify = this.bread == 'IP周边' ?  'IPper' : 'DigitalVideo'
    },
    computed:{
        ...mapState('home',['productionData'])
        
    },
    methods:{
        keyBrand(brand,index){
            this.currentBra == index ?  this.currentBra = -1 : this.currentBra = index 
            this.$bus.$emit('getKeyBra',brand)
        },
        keySort(sort,index){
            this.currentSor == index ? this.currentSor = -1 : this.currentSor = index 
            this.$bus.$emit("getKeySor",sort)
        },
        // keyPri(price,index){
        //     this.currentPri == index ? this.currentSor = -1 : this.currentSor = index 
        //     this.$bus.$emit("getKeyPri",price)
        // },
        getKeyPri(){
            this.$bus.$emit("getKeyPri",[this.bottomPrice,this.topPrice])
        },
        keyPri(index){
            console.log(index);
            // this.currentPri == index ? this.currentPri = -1 : this.currentPri = index 
            console.log(this.topPrice);
            if(index){
                console.log(1);
                index == 1 ? (this.topPrice = 2000 ,this.bottomPrice = 800) : (this.topPrice = 5000 , this.bottomPrice = 2000)
                this.getKeyPri() 
                this.currentPri == index ? (this.currentPri = -1, this.bottomPrice = '', this.topPrice = '') : this.currentPri = index 
                return 0
            }
            this.topPrice = 800 ,this.bottomPrice = 1
            console.log(2);
            this.getKeyPri()
            this.currentPri == index ? (this.currentPri = -1, this.bottomPrice = '', this.topPrice = '') : this.currentPri = index 
        }
    },
}
    
</script>

<style scoped>
.active{
    color:#fff;
    background-color:#000;
}
.tags ul li {
    float: left;
    line-height: 44px;
    padding: 0 4px;
    color: #333;
}
.tags ul li a{
    padding: 3px 15px;
}
.n-filter{
    width: 100%;
    margin: 20px auto 0 auto;
}
.title{
    float: left;
    width: 80px;
    line-height: 44px;
    color: #999;
    font-weight: 600;
}
.g-wrap{
    width: 1098px;
    margin: 0 auto;
    border: 1px solid rgba(0, 0, 0, 0.1);
    font-size: 14px;
    text-align: center;
}
.tags{
    overflow: hidden;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1)
}
.tags ul{
    width: 938px;
    float: left;
}
.more{
    float: left;
    width: 60px;
    padding-right: 20px;    
    height: 24px;
    margin-top: 10px;
    cursor: pointer;
}
.more i{
    float: right;
    width: 14px;
    height: 7px;
    margin-top: 6px;
    background-position: -24px -0px;
    background: url(../assets/ar2.png)no-repeat;
}
.lf{
    float: left;
}
.butstyle{
    width: 80px;
    height: 20px;
    font-size: 14px;
    border: 1px solid rgba(0, 0, 0, 0.15);
    border-color: #e5e5e5\0;
}
.btn-sure{
    background-color: #ccc;
    color: #fff;
    cursor: pointer;
    padding: 3px 13px;
    font-weight: 600;
    }
</style>