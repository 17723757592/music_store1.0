import api from '@/utils/requests.js'
// 用户信息接口
function getUserInformation(params){
    return api.get('http://localhost:8000/user/me', { params })
}
export default getUserInformation