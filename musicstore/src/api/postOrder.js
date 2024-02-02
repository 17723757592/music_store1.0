import api from '@/utils/requests.js'
import qs from 'qs'
// 发送订单信息
function postOrder(order) {
    return api.post('http://localhost:8000/user/order', qs.stringify(
        {   
            order_sn:order.order_sn,
            u_id:order.u_id,
            pay_price:order.price,
            contact_personnel:order.contact_personnel,
            contact_phone:order.contact_phone,
            address:order.address, 
        }))
}
export default postOrder