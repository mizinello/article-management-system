import { createRouter, createWebHistory } from 'vue-router'
import AllPosts from '@/views/AllPosts.vue'
import AddNew from '@/views/AddNew.vue'
import EditArticle from '@/views/EditArticle.vue'
import Preview from '@/views/Preview.vue'

const routes = [
  { path: '/', redirect: '/all-posts' },
  { path: '/all-posts', component: AllPosts },
  { path: '/add-new', component: AddNew },
  { path: '/edit/:id', component: EditArticle },
  { path: '/preview', component: Preview }
]

export default createRouter({
  history: createWebHistory(),
  routes
})