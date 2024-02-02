import axios from "axios";
import store from "@/store";
import getRefresh from "@/api/refreshToken";
import { Message } from 'element-ui';

const service = axios.create({
    baseURL: process.env.BASE_API,    // 请求前置连接
    timeout: 10 * 1000, // 超时时间
    // withCredentials: false, // 跨域问题时设置
})

service.interceptors.request.use(
    (config) => {
        if (store.state.user && store.state.user.authorization) {
            config.headers.Authorization = " Bearer "+store.state.user.authorization
        }
        return config
    },
    (error) => {
        // 弹窗提示
        console.log(error);
        return Promise.reject(error)
    }
)


service.interceptors.response.use(
    (response) => {
        /**
         * 1、鉴权：401，403: 
         *      1、退出登录 
         *      2、重新鉴权：
         *          1、失败退出登录
         *          2、成功再次发起请求
         * 2、错误信息弹窗提示，并返回错误信息
         * 2xx
         * 
         * {
            code: 200,
            data: {},
            message: 'success'
           }
         */

        console.log('-----');
        console.log(response);

        const res = response.data

        if (response.status > 199 && response.status < 300) {
            return res
        }

        // if ([401, 403].includes(response.status)) {
        // if (response.status == 401){
        // console.log("token失效了");
        // const refreshToken = window.localStorage.refreshToken
        // getRefresh(refreshToken).then(res=>{
        //     const {token, refreshToken} = res.data.data
        //     console.log(res.data.data);
        //     window.localStorage.setItem('token', token)
        //     window.localStorage.setItem('refreshToken', refreshToken)
        // })
        //     // 退出登录
        // }

        // 弹窗提示
        console.log(res.code);
        return Promise.reject(new Error(res.message))

    },
   (error) => {
        console.log(error);
        if (error.response && error.response.status == 401){
            console.log("token失效了");
            const refreshToken = window.localStorage.refreshToken
            // 用refresh_token 刷新token
            return getRefresh(refreshToken).then(res=>{
                const {access_token, refresh_token} = res.data
                store.state.user.authorization = access_token
                console.log(res);
                window.localStorage.setItem('authorization', access_token)
                window.localStorage.setItem('refreshToken', refresh_token)
                const config = error.config
                // 重置一下配置 
                config.headers.Authorization = " Bearer "+store.state.user.authorization
                config.baseURL = '' // url已经带上了/api，避免出现/api/api的情况
                // 重试当前请求并返回promise
                return service(config)  
            }).catch(rej=>{
                console.error('refreshtoken error =>', rej)
                
                //刷新token失败，，跳转到首页重新登录
                window.location.href = '/'
                localStorage.removeItem('authorization')
                //提醒用户过期
                Message({
                    message:'你已经长时间没有登录了，请重新登陆',   
                    type:'warning',
                    center:true,
                    duration:5000,
                    showClose:true
                }
                )

            })
        }
        return Promise.reject(error+'1111')
    }
)

export default service