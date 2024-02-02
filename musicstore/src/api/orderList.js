import request from '@/utils/requests'

// 获取订单
function getOrderList(params) {
    return request.get('http://localhost:8000/user/readOrder', { params })
}
export default getOrderList