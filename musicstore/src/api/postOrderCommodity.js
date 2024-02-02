import api from '@/utils/requests.js'
// 发送订单商品信息
function sendOrder(orderData){
    return api.post('http://localhost:8000/user/order_commodity', orderData)
}
export default sendOrder