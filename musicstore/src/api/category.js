import api from '@/utils/index'

function getCategory(params){
    return api.get('http://localhost:8000/commodity/category', { params })
}
export default getCategory