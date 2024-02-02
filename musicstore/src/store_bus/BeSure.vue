<template>
  <!-- 确认订单页面 -->
    <div class="confirmOrder">
      <!-- 头部 -->
      <div class="confirmOrder-header">
        <div class="header-content">
          <p>
            <i class="el-icon-s-order"></i>
          </p>
          <p>确认订单</p>
          <!-- <router-link to></router-link> -->
        </div>
      </div>
      <!-- 头部END -->
  
      <!-- 主要内容容器 -->
      <div class="content">
        <!-- 选择地址 在user里 -->  
        <PerAddress @getConfirmAddress="getConfirmAddress"></PerAddress>
        <!-- 选择地址END -->
        <!-- 商品及优惠券 -->
        <div class="section-goods">
          <p class="titleleft">商品及优惠券</p>
          <div class="goods-list">
            <ul>
              <!-- <li>111</li>
              <li>222</li> -->
              <li v-for="item in checkedShoppingCart" :key="item.id">
                <img :src=item.img>
                <span class="pro-name">{{item.title}}</span>
                <span class="pro-price">{{item.price}}元 x {{item.number}}</span>
                <span class="pro-status"></span>
                <span class="pro-total">{{item.price * item.number}}元</span>
              </li>
            </ul>
          </div>
        </div>
        <!-- 商品及优惠券END -->
  
        <!-- 配送方式 -->
        <div class="section-shipment">
          <p class="titleleft">配送方式</p>
          <p class="shipment">包邮</p>
        </div>
        <!-- 配送方式END -->
  
        <!-- 发票 -->
        <div class="section-invoice">
          <p class="titleleft">发票</p>
          <p class="invoice">电子发票</p>
          <p class="invoice">个人</p>
          <p class="invoice">商品明细</p>
        </div>
        <!-- 发票END -->
  
        <!-- 结算列表 -->
        <div class="section-count">
          <div class="money-box">
            <ul>
              <li>
                <span class="titleleft">商品件数：</span>
                <!-- <span class="value">{{getCheckNum}}件</span> -->
                <span class="value"> {{checkedNumber}} </span>
              </li>
              <li>
                <span class="titleleft">商品总价：</span>
                <!-- <span class="value">{{getTotalPrice}}元</span> -->
                <span class="value">{{getTotalPrice}}</span>
              </li>
              <li>
                <span class="titleleft">活动优惠：</span>
                <span class="value">-0元</span>
              </li>
              <li>
                <span class="titleleft">优惠券抵扣：</span>
                <span class="value">-0元</span>
              </li>
              <li>
                <span class="titleleft">运费：</span>
                <span class="value">0元</span>
              </li>
              <li class="total">
                <span class="titleleft">应付总额：</span>
                <span class="value">
                  <!-- <span class="total-price">{{getTotalPrice}}</span>元 -->
                  <span class="total-price">{{ getTotalPrice }}</span>元
                </span>
              </li>
            </ul>
          </div>
        </div>
        <!-- 结算列表END -->
  
        <!-- 结算导航 -->
        <div class="section-bar">
          <div class="btn">
            <router-link :to="{name:'bus'}" class="btn-base btn-return">返回购物车</router-link>
            <!-- <a href="javascript:void(0);" @click="addOrder" class="btn-base btn-primary">结算</a> -->
            <a href="javascript:void(0);" class="btn-base btn-primary" @click="goResult">提交订单</a>
          </div>
        </div>
        <!-- 确定选择收货地址 -->
        <div class="address_choose">
          <el-dialog title="确定收货地址" :visible.sync="visible">
            <el-table :data="address" highlight-current-row @current-change="handleCurrentChange">
                <el-table-column width="200" property="contact_personnel" label="姓名"></el-table-column>
                <el-table-column  property="contact_phone" label="电话"></el-table-column>
                <el-table-column  property="address" label="地址"></el-table-column>
            </el-table>
            <div style="margin-top: 20px">
              <el-button @click="visible = false">取消</el-button>
              <el-button style="margin-left: 20px" @click="sendCurrent" :style="(currentRow!=null) ? {backgroundColor:'#409EFF',color:'white'} : ''">确定</el-button>
            </div>
          </el-dialog>
        </div>
        <!-- 结算导航END -->
        <el-dialog :visible.sync="singel">
            <el-result icon="success" title="订单提交成功" subTitle="请根据提示进行操作">
              <template slot="extra">
                  <el-button type="" size="medium" @click="toPerOrder">查看我的订单</el-button>
                  <el-button type="primary" size="medium" @click="backHome">返回</el-button>
              </template>
            </el-result>
        </el-dialog>
      </div>
      <!-- 主要内容容器END -->
    </div>
</template>

<script>
import getUserAddress from '@/api/getUserAddress';
import PerAddress from '@/user/PerAddress.vue';
import sendOrder from '@/api/postOrderCommodity';
import createOrderNumber from '@/utils/create_order_number';
// import postOrder from '@/api/postOrder';
// import {nanoid} from 'nanoid'
import getTime from '../utils/get_time'
import {mapGetters} from 'vuex';

export default {
  name:'BeSure',
  components:{PerAddress},
  data() {
    return{
      singel:false,
      visible:false,
      information:this.$store.state.user.information,
      confirmAddress:'',
      address:'',
      currentRow: null,
      message:"fail!!!"
    }
  },
  methods:{
    getConfirmAddress(data){
      this.confirmAddress = data
    },
    handleCurrentChange(val) {
      this.currentRow = val;
    },
    sendCurrent(){
      if(!this.currentRow){
        this.$message({
          showClose: true,
          message: '您还未确认地址哟~',
          type: 'error'
          });
          return 0 
      }
      this.visible = false
      this.confirmAddress = this.currentRow.id
      this.goResult()
    },
    async sendOrderItem(orderData){
      console.log(orderData);
        await sendOrder(orderData).then(res=>{
          console.log(res);
        })
    },
    goResult(){
      const address = this.address.filter((item) => {
        return item.id == this.confirmAddress
      })
      console.log(this.confirmAddress);
      if(!this.confirmAddress){
        this.visible = true
        console.log(this.visible);
        return 0 
      }
      // 订单商品信息
      const orderData = {
        u_id:this.information.username,
        order_id:this.information.id + createOrderNumber(),
        created_time:getTime(),
        // price:this.getTotalPrice,
        // shopping:this.checkedShoppingCart,
        // address:address
      }
      const order = {
        address:address.address,
        contact_personnel:address.contact_personnel,
        contact_phone:address.contact_phone,
        order_sn:orderData.order_id,
        u_id:orderData.u_id,
      }
      this.$store.dispatch('user/unshiftPayedShoppingCart',orderData)
      // this.getPay = true
      const shopping = this.checkedShoppingCart
      const sumFunction = (a, b) => a + b;
      // 订单的总价格
      let orderPrice = 0
      console.log(shopping);
      shopping.forEach((item)=>{
        orderPrice = sumFunction(orderPrice,item.price * item.number)
        orderData.commodity_id = item.commodity_id
        orderData.title = item.title 
        orderData.price = item.price
        orderData.brand_id = item.brand_id
        orderData.category_id = item.category_id
        orderData.pictures = item.img
        orderData.quantity = item.number 
        //发送订单商品信息
        this.sendOrderItem(orderData)
      })
      order.price = orderPrice
      // post订单信息
      // postOrder(order)
      this.$store.commit('cart/resetShoppingCart')
      this.singel = true
    },    
    toPerOrder(){
      this.$router.push({name:'perorder',params:{bread:'我的订单'}})
    },
    backHome(){
      this.$router.push({name:'home'})
    }
  },
  // watch:{
  //   getPay(){
  //     this.payResult.get()
  //   }
  // },
  computed:{
    ...mapGetters('cart',['getTotalPrice','checkedNumber','checkedShoppingCart']),
    // payResult:{
    //   get(val){
    //     return this.getPay == val ? '已结算' : '结算'
    //   }
    // }
  },
  async created(){
    await getUserAddress().then(res=>{
      this.address = res.data
    })
  },
  mounted(){
    console.log(this.confirmAddress);
  },
  // beforeRouteEnter(to,from,next){
  //   sessionStorage.getItem('login')==='true' ? next() : confirm('请先登录')
  // },

}
</script>
<style scoped>
/* 这里需要覆盖原组件的部分样式 */
.section-address {
  margin: 0 48px;
  overflow: hidden;
}
.confirmOrder {
  background-color: #f5f5f5;
  padding-bottom: 120px;    
}
/* 头部CSS */
.confirmOrder .confirmOrder-header {
  background-color: #fff;
  border-bottom: 2px solid #ff6700;
  margin-bottom: 20px;
}
.confirmOrder .confirmOrder-header .header-content {
  width: 1100px;
  margin: 0 auto;
  height: 80px;
}
.confirmOrder .confirmOrder-header .header-content p {
  float: left;
  font-size: 28px;
  line-height: 80px;
  color: #424242;
  margin-right: 20px;
}
.confirmOrder .confirmOrder-header .header-content p i {
  font-size: 45px;
  color: #3f72ad;
  line-height: 80px;
}
/* 头部CSS END */

/* 主要内容容器CSS */
.confirmOrder .content {
  width: 1225px;
  margin: 0 auto;
  padding: 48px 0 0;
  background-color: #fff;
}

/* 商品及优惠券CSS */
.confirmOrder .content .section-goods {
  margin: 0 48px;
  overflow: hidden;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.confirmOrder .content .section-goods p.titleleft {
  color: #333;
  font-size: 18px;
  line-height: 40px;
}
.confirmOrder .content .section-goods .goods-list {
  padding: 5px 0;
  border-bottom: 1px solid #e0e0e0;
}
.confirmOrder .content .section-goods .goods-list li {
  padding: 10px 0;
  color: #424242;
  overflow: hidden;
}
.confirmOrder .content .section-goods .goods-list li img {
  float: left;
  width: 46px;
  height: 46px;
  margin-right: 10px;
}
.confirmOrder .content .section-goods .goods-list li .pro-name {
  float: left;
  width: 650px;
  line-height: 30px;
}
.confirmOrder .content .section-goods .goods-list li .pro-price {
  float: left;
  width: 150px;
  text-align: center;
  line-height: 30px;
}
.confirmOrder .content .section-goods .goods-list li .pro-status {
  float: left;
  width: 83px;
  height: 30px;
  text-align: center;
  line-height: 30px;
}
.confirmOrder .content .section-goods .goods-list li .pro-total {
  float: left;
  width: 190px;
  text-align: center;
  color: #d33a31;
  line-height: 30px;
}
/* 商品及优惠券CSS END

/* 配送方式CSS */
.confirmOrder .content .section-shipment {
  margin: 0 48px;
  padding: 25px 0;
  border-bottom: 1px solid #e0e0e0;
  overflow: hidden;
}
.confirmOrder .content .section-shipment .titleleft {
  float: left;
  width: 150px;
  color: #333;
  text-align: left;
  font-size: 18px;
  line-height: 38px;
}
.confirmOrder .content .section-shipment .shipment {
  float: left;
  line-height: 38px;
  font-size: 14px;
  color: #d33a31;
}
/* 配送方式CSS END */

/* 发票CSS */
.confirmOrder .content .section-invoice {
  margin: 0 48px;
  padding: 25px 0;
  border-bottom: 1px solid #e0e0e0;
  overflow: hidden;
}
.confirmOrder .content .section-invoice .titleleft {
  float: left;
  text-align: left;
  width: 150px;
  color: #333;
  font-size: 18px;
  line-height: 38px;
}
.confirmOrder .content .section-invoice .invoice {
  float: left;
  line-height: 38px;
  font-size: 14px;
  margin-right: 20px;
  color: #d33a31;
}
/* 发票CSS END */

/* 结算列表CSS */
.confirmOrder .content .section-count {
  margin: 0 48px;
  padding: 20px 0;
  overflow: hidden;
}
.confirmOrder .content .section-count .money-box {
  float: right;
  text-align: right;
}
.confirmOrder .content .section-count .money-box .titleleft {
  float: left;
  width: 126px;
  height: 30px;
  display: block;
  line-height: 30px;
  color: #757575;
}
.confirmOrder .content .section-count .money-box .value {
  float: right;
  min-width: 105px;
  height: 30px;
  display: block;
  line-height: 30px;
  color: #d33a31;
}
.confirmOrder .content .section-count .money-box .total .titleleft {
  padding-top: 15px;
}
.confirmOrder .content .section-count .money-box .total .value {
  padding-top: 10px;
}
.confirmOrder .content .section-count .money-box .total-price {
  font-size: 30px;
}
/* 结算列表CSS END */

/* 结算导航CSS */
.confirmOrder .content .section-bar {
  padding: 20px 48px;
  border-top: 2px solid #f5f5f5;
  overflow: hidden;
}
.confirmOrder .content .address_choose{
  border: 1px solid #e0e0e0;
}
.confirmOrder .content .section-bar .btn {
  float: right;
}
.confirmOrder .content .section-bar .btn .btn-base {
  float: left;
  margin-left: 30px;
  width: 158px;
  height: 38px;
  border: 1px solid #b0b0b0;
  font-size: 14px;
  line-height: 38px;
  text-align: center;
}
.confirmOrder .content .section-bar .btn .btn-return {
  color: rgba(0, 0, 0, 0.27);
  border-color: rgba(0, 0, 0, 0.27);
}
.confirmOrder .content .section-bar .btn .btn-primary {
  background: #d33a31;
  border-color: #d33a31;
  color: #fff;
}

</style>