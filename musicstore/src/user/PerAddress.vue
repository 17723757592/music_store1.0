<template>
    <div>
      <!-- 选择地址 -->
      <div class="section-address">
        <p class="titleleft">收货地址</p>
        <div class="address-body">
          <ul>
            <li
              v-for="item in addressList" @click="chooseAddress(item)"
              :class="item.id == confirmAddress ? 'in-section' : ''"
              :key="item.id">
              <h2>{{item.contact_personnel}}</h2>
              <p class="phone">{{item.contact_phone}}</p>
              <p class="address">{{item.address}}</p>
            </li>
            <li class="add-address" @click="dialogVisible = true">
              <i class="el-icon-circle-plus-outline"></i>
              <p>添加新地址</p>
            </li>
          </ul>
          <el-dialog title="添加收获地址" :visible.sync="dialogVisible">
            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
              <el-form-item label="名字" prop="name">
                <el-input v-model="ruleForm.name" :style="{width:'90%'}"></el-input>
              </el-form-item>
              <el-form-item label="手机号" prop="number">
                <el-input v-model.number="ruleForm.number" :style="{width:'90%'}"></el-input>
              </el-form-item>
              <el-form-item label="地址" prop="address">
                <el-input v-model="ruleForm.address" :style="{width:'90%'}"></el-input>
              </el-form-item>
            </el-form>
            <div slot="footer" class="dialog-footer" :style="{'text-align':'center'}">
              <el-button @click="dialogVisible = false">取 消</el-button>  
              <el-button type="primary">确 定</el-button>
            </div>
          </el-dialog>
        </div>
      </div>
      <!-- 选择地址END -->
  </div>
</template>

<script>
import getUserAddress from '@/api/getUserAddress'
import {isvalidPhone} from '../utils/phone_number'
export default {
    name:'PerAddress',
    data() {
      const validPhone = (rule, value, callback) => {
        if (!value) {
          callback(new Error('请输入电话号码'))
        } else if (!isvalidPhone(value)) { //判断用户输入的值是否符合规则
          callback(new Error('请输入正确的11位手机号码'))
        } else {
          callback()
        }
      }
      return {
        dialogVisible:false,  
        confirmAddress: '',   
        // 虚拟数据
        addressList:'',
        ruleForm: {
          name: '',
          number: '',
          address: '',
        },
        rules: {
          name: [
            { required: true, message: '请输入您的名字', trigger: 'blur' },
            { min: 2, max: 5, message: '长度在 2 到 5 个字符', trigger: 'blur' }
          ],
          number:[
            { required: true, trigger: 'blur',validator: validPhone}
          ],
          address:[
            { required: true, message: '请输入您的收货地址', trigger: 'blur' },
            { min: 5, max: 30, message: '你的位置信息似乎不正确', trigger: 'blur' }
          ],
        }
      }
    },
    methods:{
      chooseAddress(item) {
        this.confirmAddress = item.id
        this.$emit('getConfirmAddress',this.confirmAddress)
      }
    },
    async created(){
      await getUserAddress().then(res=>{
        this.addressList = res.data
        const defaultId = this.addressList.find((item) => item.id_default === 1)
        if(defaultId){
          this.confirmAddress = defaultId.id
          this.$emit('getConfirmAddress',this.confirmAddress)
        }
      })
    },
    mounted(){
      this.$emit('getConfirmAddress',this.confirmAddress)
    },
    // 解绑自定义事件 getConfirmAddress  
    beforeDestroy(){
    this.$off('getConfirmAddress')
  }

}
</script>

<style>
/* 选择地址CSS48 */
.section-address {
  margin: 0 48px;
  overflow: hidden;
}
.section-address .titleleft {
  color: #333;
  font-size: 18px;  
  line-height: 20px;
  text-align: left;
  margin-bottom: 20px;
}
.address-body{
  overflow: hidden;
}
.address-body li {
  float: left;
  color: #333;
  width: 220px;
  text-align: left;
  height: 178px;
  border: 1px solid #e0e0e0;
  padding: 15px 24px 0;
  margin-right: 17px;
  margin-bottom: 24px;
}
.address-body .in-section {
  border: 1px solid #d33a31;
}
.address-body li h2 {
  font-size: 18px;
  font-weight: normal;
  line-height: 30px;
  margin-bottom: 10px;
}
.address-body li p {
  font-size: 14px;
  color: #757575;
}
.address-body li .address {
  padding: 10px 0;
  max-width: 180px;
  max-height: 88px;
  line-height: 22px;
  overflow: hidden;
}
.address-body .add-address {
  text-align: center;
  line-height: 30px;
}
.address-body .add-address i {
  font-size: 30px;
  padding-top: 50px;
  text-align: center;
}
/* 选择地址CSS END */
</style>