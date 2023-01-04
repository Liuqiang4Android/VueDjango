import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue') // 建议进行路由懒加载，优化访问性能
  },
  {
    path: '/demo',
    name: 'demo',
    component: () => import('@/views/Demo.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
// 复制代码