import api from '@/utils/index.js'
import qs from 'qs'

function getToken(form){
    return api.post('http://localhost:8000/user/token', qs.stringify({username:form.name, password:form.pwd}))
}
export default getToken