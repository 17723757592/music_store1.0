import api from '@/utils/requests.js'
import qs from 'qs'

function userRegister(from){
    return api.post('http://localhost:8000/user/create', qs.stringify({username:from.name, password:from.pwd}))
}
export default userRegister