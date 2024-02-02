import api from '@/utils/index'

function getRefresh(refreshToken){
    return api.post(`http://localhost:8000/user/refresh_token?refresh_token=${refreshToken}`)
}
export default getRefresh