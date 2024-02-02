<template>
    <!-- 顶部登录搜索区 -->
    <div>
        <div class="nav">
            <div class="m-nav">
                <div class="m-nav-left" @click="$router.push({name:'home'})">
                    <a href="javascript:"></a>
                </div>
                <div class="m-nav-m">
                    <div>
                        <div class="inputbox">
                            <input class="input" type="text" v-model="keyWords" placeholder="输入你想搜索的商品" @keyup.enter="getKeyDatas(keyWords)">
                        </div>
                    </div>
                </div>
                <el-badge :value="shoppingCart.length" class="item-number" :hidden="Boolean(!shoppingCart.length)">
                    <div class="m-nav-bus">
                        <a href="">
                            <router-link :to="{name:'bus'}"></router-link>  
                        </a>
                    </div>
                </el-badge>
                <!-- <div class="m-nav-bus">
                    <a href="">
                        <router-link :to="{name:'bus'}"></router-link>
                    </a>
                </div> -->
                <div class="m-nav-lo">
                    <div class="m-nav-select">
                        <div v-if="getLogin">
                            <div>
                                <el-avatar icon="el-icon-user-solid">
                                </el-avatar>
                                <ul class="methods">
                                        <li class="personal-center" @click="$router.push({name:'personalcenter',params:{bread:'我的订单'}})">
                                            <a href="javascript:"><em class="phone-ico">
                                            </em>我的订单<span></span></a>
                                        </li>
                                        <li class="unlogin" @click="logout">
                                            <a href="javascript:"><em class="wechat-ico">
                                            </em>退出登录<span></span></a>
                                        </li>
                                    </ul>
                            </div>  
                        </div>
                        <div v-else class="login" @click="login(true)">登录</div>
                    </div>
                </div>
            </div>
            <LoginName></LoginName>
        </div>
    </div>
</template>

<script>
import LoginName from '../login/login.vue'
import {mapState, mapActions} from 'vuex'
export default {
    name:'BannerName',
    components:{ LoginName },
    data(){
        return{
            keyWords:'',
            goods:''
        }
    },
    methods:{
       ...mapActions('user',['login']),
       logout(){
        // this.$store.state.user.login = false
        this.$router.push({name:'home'})
        this.loginSingel = false
        this.authorization = ''
        this.$store.state.user.information = ''
        localStorage.removeItem('userInformation')
        this.$message({
          showClose: true,
          message: '已退出登录',
          type: 'success'
        });
       },
       getKeyDatas(){
        if(!this.keyWords.trim()){
            this.$message({
                showClose:true,
                message:'请输入有效的关键字哦~',
                type:'warning'
            })
            return 0 
        }
        this.$router.push({
            name:'sort',
            params:{
                bread:this.keyWords
            }
        })
        }
    },
    computed:{
        ...mapState('cart',['shoppingCart']),
        loginSingel:{
            get(){
                return this.$store.state.user.login
            },
            set(val){
                // 退出登录
                this.$store.state.user.login = val
                // 清除浏览器对登录的标记
                localStorage.removeItem('login')
            }
        },
        authorization:{
            get(){
                return this.$store.state.user.authorization
            },
            set(val){
                this.$store.state.user.authorization = val
                localStorage.removeItem('authorization')
                localStorage.removeItem('refreshToken')
            }
        },
        getLogin:{
            get(){
                return Boolean(this.authorization)
            }
        }
    }
}
</script>

<style>
.item-number{
    margin-top: 19px;
    float: left;
    margin-left: 37px;
}
.nav{
    height: 73px;
    background: #fff;
    position: relative;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1)
}
.m-nav{
    margin:0 auto;
    width:1100px;
    height: 73px;
    /* background-color: #f1f7f4; */
    }
.m-nav-left{
    width: 290px;
    height: 70px;
    background-position: 0px -48px; 
    background-image:url("../assets/modules.png");
    float: left;
}
.m-nav-left a{
    width: 290px;
    height: 70px;
    display: inline-block;
    text-decoration: none;
}
.m-nav-m{
    width: 300px;
    height: 70px;
    margin-left: 334px;
    float: left;
    background-color: #fff;
}
.m-nav-m div{
    width: 300px;
    height: 38px;
    padding-top: 1px;
}
.inputbox{
    width: 100%;
    height: 38px;
    background-image: url("../assets/modules.png");
    background-position: 0px -0px;
    margin-top: 15px;
}
.input{
    width: 80%;
    margin-top:10px;
    margin-left: 34px;
    border: 0;
    background: transparent;
    font-size: 12px;
    color: #333;
}
.m-nav-bus{
    width: 36px;
    height: 36px;
    background-position: -110px -158px;
    background-image: url("../assets/modules.png");
    position: relative;
}  
.m-nav-bus a{
    display: inline-block;
    width: 36px;
    height: 36px;
    cursor: pointer;
    text-decoration: none;
}
.m-nav-lo{
    width: 62px;
    height: 36px;
    margin: 15px 0 0 37px;
    cursor: pointer;
    float: left;
}
.m-nav-select :hover .methods{
    display: block;
}
.m-nav-select{
    z-index: 99;
    width: 62px;
    height: 36px;
    position: relative;
}
.login{
    width: 36px;
    height: 36px;
    line-height: 36px;
    text-align: center;
    font-size: 14px;
}
.methods{
    display: none;
    position: absolute;
    z-index: 999;
    left: -55px;
    width: 160px;
    height: auto;
    padding: 0;
    margin: 0;
    box-shadow: 0 4px 7px #555;
    text-shadow: 0 1px 0 rgba(255, 255, 255, 0.9);
}
.methods li{
    list-style: none;
    position: relative;
    z-index: 999;
    font-size: 12px;
    padding-left: 0px;
    color: #333;
    background-color: #fff;
}
.methods li:hover{
    background-color: #dacfcf;
}
.methods li a{
    display: block;
    width: 134px;
    margin: 0;
    padding-left: 6px;
    height: 40px;
    line-height: 40px;
    text-decoration: none;
}
.methods li a em{
    display: inline-block;
    position: relative;
    top: 4px;
    width: 18px;
    font-style: normal;
    text-align: left;
    font-size: inherit;
    margin-right: 9px;
}
.methods li a span{
    top: 0;
    right: 0;
    bottom: 0;
    left: -24px;
}
/* .personnal{
    height: 16px;
    background: url("../assets/phonelog.png") no-repeat;
}
.unlogin{
    height: 16px;
    background: url("../assets/logins.png") no-repeat;
    background-position: -84px -0px;
}
.qq-ico{
    height: 16px;
    background: url("../assets/logins.png") no-repeat;
    background-position: -112px -0px;
} */
</style>