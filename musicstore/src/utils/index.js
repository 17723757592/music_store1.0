import axios from "axios";

const api = axios.create({
    baseURL: process.env.BASE_API,    // 请求前置连接
    timeout: 10 * 1000, // 超时时间
    // withCredentials: false, // 跨域问题时设置
})
        
api.interceptors.request.use(config => {
    // config 请求的信息
   return config // 将配置完成的config对象返回出去 如果不返回 请求则不会进行
}, err => {
   // 请求发生错误时的处理 抛出错误
  Promise.reject(err)
})

api.interceptors.response.use(res => {
    // 我们一般在这里处理，请求成功后的错误状态码 例如状态码是500，404，403
    // res 是所有相应的信息
   return Promise.resolve(res)
}, err => {
    // 服务器响应发生错误时的处理
    Promise.reject(err)
})
export default api
