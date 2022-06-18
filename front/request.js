import axios from "./axios.js";

let server = axios.create({
	// 请求公共地址
    baseURL: "http://49.232.11.80/api",
    // 超时时间
    timeout: 5000,
})

// 请求拦截
server.interceptors.request.use(config => {
    return config
}, err => {
    // throw new Error(err)
    Promise.reject(err)
})


// 响应拦截
server.interceptors.response.use(res => {
    // res 是服务器返回的数据信息
    // console.log(res);
    return res.data
}, err => {
    throw new Error(err)
})

export function getTime(params) {
    return server({
      url: '/get_time',
      method: 'get',
      params
    })
}

export function postTime(data) {
    return server({
      url: '/post_time',
      method: 'post',
      data
    })
}

