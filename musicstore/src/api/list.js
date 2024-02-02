import api from '@/utils/index'

function getCategoryList(category_id){
    return api.get(`http://127.0.0.1:8000/commodity/list?category_id=${category_id}`, { category_id })
}
export default getCategoryList