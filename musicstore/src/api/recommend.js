import api from '@/utils/index'

function getRecommendList(params){
    return api.get('http://localhost:8000/commodity/recommend', { params })
}
export default getRecommendList