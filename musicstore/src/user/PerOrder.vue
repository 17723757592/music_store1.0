<template>
  <div>
    <!-- 订单信息页面 -->
    <div class="section-goods" v-if="showList.length > 0">
      <p class="titleleft">订单:</p>
      <div class="goods-list" v-for="order in showList" :key="order.order_id">
        <div class="order-box">
          <div class="order-statue">
            <p>等待付款</p>
            <span class="order-time">{{ order.goods[0].create_time }}</span> |
            <span class="order-user">{{information.nickname}}</span> |
            <span class="order-number">订单编号：{{ order.order_id }}</span> |
            <span class="methods-pay"> 在线支付</span>
            <span class="total-price">应付价格：<i>{{ order.price }}</i> 元</span>
          </div>
          <!-- <div class="address-box">
            <p>送到:</p>
            <div class="address-body">
              <li v-for="item in order.address" :key="item.id">
                <h2>{{item.contact_personnel}}</h2>
                <p class="phone">{{item.contact_phone}}</p>
                <p class="address">{{item.address}}</p>
              </li>
            </div>
          </div> -->
          <div class="item-box">
            <div class="contend">
              <ul>
                <li v-for="item in order.goods" :key="item.commodity_id">
                  <!-- <img :src="$target + item.productImg" /> -->
                  <img class="pro-img" :src=item.pictures alt="">
                  <div class="pro-name">{{item.title}}</div>
                  <div class="pro-price">{{item.price}}元 x {{item.quantity}}</div>
                  <!-- <div class="pro-total">实付：{{item.price * item.number}}元</div> -->
                </li>
              </ul>
            </div>
            <ul class="action">
              <li class="action-pay">立即付款</li>
              <li class="action-delete">订单详情</li>
              <li class="action-delete" @click="deletePayedShoppingCart(order.order_id)">取消订单</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <h3>你还没有下单，快去看看吧</h3>
    </div>
  </div>
</template>

<script>
import getOrderList from '@/api/orderList';
import orderDelete from '@/api/deleteOrder';
// import getOrderNumber from '@/api/order';

// import { mapState } from 'vuex';
export default {
    name:'PerOrder',
    data(){
      return{
        address:'',
        confromAddress:'',
        orderList:[],
        showList:[],
        information:this.$store.state.user.information
      }
    },
    created(){
      this.getOrder()
      // this.confromAddress = JSON.parse(sessionStorage.getItem('address'))
      // console.log(this.confromAddress);
      // this.address = this.$store.state.user.address.find(item=>item.id == this.confromAddress)
      // await getOrderNumber().then(res=>{
      //   let orderArr = []
      //   res.data.forEach(e=>{
      //     orderArr.push(e.order_sn)
      //   })
      //   this.$store.dispatch('user/addOrderNumber',orderArr)
      // }) 

        // console.log(this.information);

      // await this.$store.dispatch('user/userInformation')
    },
    methods:{
      deletePayedShoppingCart(order_id){
        this.$confirm('确定要取消这个订单吗', '删除提示', { type: 'warning' }).then(() => {
          this.$store.dispatch('user/deletePayedShoppingCart',order_id)
          // 删除订单
          orderDelete(order_id)
          this.getOrder()
          console.log(this.showList);
          }).catch(()=>{
            return 0
          })
      },
      getOrder(){
        getOrderList().then(res=>{
          this.orderList = res.data
          console.log(this.orderList);
          // 重置被渲染的订单列表重新请求数据，因为之前的会和后面的冲突
          this.showList = []
          // api传回的每条商品都是根据时间降序的
          this.orderList.forEach(item => {
            let {order_id} = item;
            if(!this.showList[order_id]){
              this.showList[order_id] = {
                order_id,
                goods:[],
                price:'',
                update_time:new Date(item.update_time)
                // 如果一个订单号有多条商品，最先传入的时间就是最新时间
              }
            }

            this.showList[order_id].goods.push(item)
            const sumFunction = (a, b) => a + b;
            let sum = 0
            this.showList[order_id].goods.forEach((item) =>{
              sum = sumFunction(sum, item.price * item.quantity)
            })
            this.showList[order_id].price = sum
          })
          // 转为对象
          this.showList = Object.values(this.showList)
          // 将updata_time最新的订单放在前面
          this.showList.sort((a,b)=>{
              return( b.update_time - a.update_time)  
          })
          console.log(this.showList);
        }).catch(rej=>{
          console.log(rej);
        })
          // this.orderList = rej.data
          // console.log(this.orderList);
          // // 重置被渲染的订单列表重新请求数据，因为之前的会和后面的冲突
          // this.showList = []
          // // api传回的每条商品都是根据时间降序的
          // this.orderList.forEach(item => {
          //   let {order_id} = item;
          //   if(!this.showList[order_id]){
          //     this.showList[order_id] = {
          //       order_id,
          //       goods:[],
          //       price:'',
          //       update_time:new Date(item.update_time)
          //       // 如果一个订单号有多条商品，最先传入的时间就是最新时间
          //     }
          //   }

          //   this.showList[order_id].goods.push(item)
          //   const sumFunction = (a, b) => a + b;
          //   let sum = 0
          //   this.showList[order_id].goods.forEach((item) =>{
          //     sum = sumFunction(sum, item.price * item.quantity)
          //   })
          //   this.showList[order_id].price = sum
          // })
          // // 转为对象
          // this.showList = Object.values(this.showList)
          // // 将updata_time最新的订单放在前面
          // this.showList.sort((a,b)=>{
          //     return( b.update_time - a.update_time)  
          // })
      },
  }
}
</script>

<style scoped>
.section-goods {
  width: 900px;
  margin: 0 auto;
  overflow: hidden;
  text-align: left;
  /* border-bottom: 1px solid #e0e0e0; */
}
.total-price{
  margin-left:30px ;
  
}
.total-price i{
  color: #d33a31;
  font-size: 30px;
  font-style: normal;
}
.order-statue{
  color: #e0e0e0;
  font-size: 18px;
  padding: 25px  25px;
  background-color: #fffaf7;
  border-bottom: 1px solid  #feccac;
}
.order-statue p {
  color: #ff6700;
}
.order-statue span {
  margin-top: 35px;
  font-weight: 400;
  color: #757575;
  font-size: 15px;
}
.order-number{
  padding-bottom: 20px;
  font-weight: bold;
  color:black;
}

.order-box{
  width: auto;
  border: 1px solid  #d33a31;
}
.address-box{
  float: right;
}
.item-box{
  overflow: hidden;
  padding: 15px;
  /* margin-bottom: 15px; */
}
.contend{
  float: left;
  overflow: hidden;
}
/* .item-box ul{
  width: auto;
  min-height: 180px;
  padding: 25px  25px;
} */
.contend ul li {
  margin-bottom: 15px;
  width: 513px;
}
.titleleft {
  color: #333;
  font-size: 18px;
  margin: 0 48px;
  line-height: 40px;
}
.goods-list {
  position: relative;
  padding: 8px 48px;
  overflow: hidden;
  /* border-bottom: 1px solid #e0e0e0; */
}
.contend li {
  color: #424242;
  overflow: hidden;
}
.contend li img {
  float: left;
  width: 30px;
  height: 30px;
  margin-top:15px;
  margin-right:10px;
}
.contend li .pro-img {
  width: 80px;
  height: 80px;
}
.contend li .pro-name {
  padding-top:35px;
  white-space:nowrap; 
  overflow: hidden;
  text-overflow: ellipsis;
}
/* .goods-list li .pro-price {
  line-height: 30px;
} */
.action{
  float: right;
}
.action li {
  display: block;
  width: 118px;
  height: 28px;
  font-size: 12px;
  text-align: center;
  line-height: 28px;
  cursor: pointer;
  list-style: none;
  margin: 0 0 10px auto;
  color: #b0b0b0;
  border: 1px solid #b0b0b0;
}
.action li:first-child{
  background: #ff6700;
  border-color: #ff6700;
  margin-top: 10px;
  color: #fff;
}
/* .action-delete{
  position: absolute;
  bottom: 10px;
  width: 70px;
  height: 20px;
  line-height: 20px;
  cursor: pointer;
  text-align: center;
  border: 1px solid #d33a31;
  border-radius: 5%;

} */
</style>