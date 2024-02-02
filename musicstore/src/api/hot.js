import api from '@/utils/index'

function getHotList(params){
    return api.get('http://localhost:8000/commodity/hot', { params })
}
export default getHotList