import Vue from 'vue'
import VueRouter from 'vue-router'

const HomeView = () => import('@/views/HomeView')
const HostView = () => import('@/views/HostView')
const GuestView = () => import('@/views/GuestView')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: HomeView
  },
  {
    path: '/host',
    component: HostView
  },
  {
    path: '/guest',
    component: GuestView
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  linkActiveClass: 'active'
})

export default router
