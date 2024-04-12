import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Home.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Books
    },
  ]
})

export default router