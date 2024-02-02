import api from '@/utils/index'
// 轮播图接口
function getBannerList(params){
    return api.get('http://localhost:8000/banner/list', { params })
}
export default getBannerList