import request from '@/network/request'

export function getTime (params) {
  return request({
    url: '/get_time',
    method: 'get',
    params
  })
}

export function postTime (data) {
  return request({
    url: '/post_time',
    method: 'post',
    data
  })
}
