import axios from 'axios'

const server = axios.create({
  // 请求公共地址
  baseURL: 'http://huohuohuo.xyz/api',
  timeout: 5000
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

export default server
