import api from '@/utils/requests'

function orderDelete(order_id){
    return api.put(`http://localhost:8000/user/orderDelete?order_id=${order_id}`)
}
export default orderDelete