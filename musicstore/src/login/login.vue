<template>
  <!-- 登录的页面 -->
    <div>
        <el-dialog title="CloudMusicStore-login" :visible.sync="visible">
          <el-form :model="form" :style="{'text-align':'left'}" >
              <el-form-item label="用户名" :label-width="formLabelWidth">
                  <el-input v-model="form.name" autofocus="true" autocomplete="off" :style="{width:'90%'}"></el-input>
              </el-form-item>
              <el-form-item label="密码" :label-width="formLabelWidth">
                  <el-input v-model="form.pwd" show-password autocomplete="off" :style="{width:'90%'}"></el-input>
              </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer" :style="{'text-align':'center'}">
            <el-button @click="addUser" >注 册</el-button>  
            <el-button type="primary" @click="login">登 录</el-button>
          </div>
        </el-dialog>  
    </div>
</template>

<script>
import getToken from '@/api/login';
import userRegister from '@/api/register';
import { mapMutations } from 'vuex'
// import {mapState} from 'vuex'

export default {
    name:'LoginName',
    data() {
      return {
        form: {
          name:'',
          pwd:'',
          region: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        formLabelWidth: '90px',
        // check:''
      };
    },
    methods:{
      ...mapMutations('user',['changeStatus']),
      async addUser(){
        await userRegister(this.form).then(res=>{
          console.log(res)  
        })
        // let check = localStorage.getItem(this.form.name) || ''
        // if(this.check){
        //   this.$message({
        //   showClose: true,
        //   message: '该用户已注册，请登录',
        //   type: 'error'
        //   });
        //   return 0 
        // }
        this.$message({
          showClose: true,
          message: '恭喜你，注册成功',
          type: 'success'
        });
      },
      success(){
        this.visible = false
        this.$store.state.user.login = true
        // 需要将状态存到浏览器，不然刷新会回到未登录状态
        localStorage.setItem('login', true)
        localStorage.setItem('authorization',this.$store.state.user.authorization)
        this.$message({
          showClose: true,
          message: '登录成功',
          type: 'success'
        });

        
      },
      errorPwd(){
        this.$message({
          showClose: true,
          message: '用户名或密码错误',
          type: 'error'
        });
      },
      async login(){
        await getToken(this.form).then(res=>{
          // 请求用户信息并将信息存放在vuex的user模块
            this.$store.state.user.authorization = res.data.access_token
            // 将refreshToken存放起来token过期会用refreshToken去更新token信息
            localStorage.setItem('refreshToken',res.data.refresh_token)
            // userinformation()会获取用户信息
            this.$store.dispatch('user/userInformation') 
        }).catch(err=>{
          console.log(err);
        })
        // let checkuser = localStorage.getItem(this.form.name) || ''
        // this.$message({
        //   showClose: true,
        //   message: '查无此用户',
        //   type: 'warning'
        // });
        Boolean(this.$store.state.user.authorization) == true ? this.success() : this.errorPwd()
      }
    },
    computed:{
      visible:{
        get(){
          //开启了模块化命名
          return this.$store.state.user.status
        },
        set(val){
          this.changeStatus(val)
        }
      },
      
    },
    watch:{
      form:{
        deep:true,
        handler(val){
          this.form.name = val.name
          this.form.pwd = val.pwd
        }
      }
    },
}
</script>

<style>

</style>