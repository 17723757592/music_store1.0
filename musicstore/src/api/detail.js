import api from '@/utils/index'

function getDetail(id){
    return api.get(`http://127.0.0.1:8000/commodity/commodity_info?id=${id}`)
}
export default getDetail