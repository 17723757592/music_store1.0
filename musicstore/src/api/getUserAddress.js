import api from '@/utils/requests.js'
// 用户地址接口
function getUserAddress(params){
    return api.get('http://localhost:8000/user/address', { params })
}
export default getUserAddress