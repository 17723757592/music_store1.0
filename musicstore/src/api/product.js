import request from '@/utils/requests'

export function getProductList(params) {
    return request.get('/store_item.json', { params })
    // return request({
    //     url: '/store_item.json',
    //     method: 'GET',
    //     params: params,

    //     responseType: 'blob',
    //     timeout: 100 * 1000,
    // })

    // return request.post('/store_item.json', params)
    // return request({
    //     url: '/store_item.json',
    //     method: 'POST',
    //     data: params,

    //     // responseType: 'blob',
    //     // timeout: 100 * 1000,
    // })
}
