import api from '@/utils/index'

function getKeyDatas(keyWods){
    return api.get(`http://127.0.0.1:8000/commodity/list?title=${keyWods}`, { keyWods })
}
export default getKeyDatas