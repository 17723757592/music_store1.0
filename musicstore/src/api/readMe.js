import api from '@/utils/requests.js'

function readMe(params){
    return api.get('http://localhost:8000/user/me', { params })
}
export default readMe