<template>
  <div class="container mt-4">
    <h2>All Posts</h2>
    
    <!-- Tabs -->
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'publish' }" 
           @click="activeTab = 'publish'">Published</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'draft' }" 
           @click="activeTab = 'draft'">Drafts</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'thrash' }" 
           @click="activeTab = 'thrash'">Trashed</a>
      </li>
    </ul>
    
    <!-- Articles Table -->
    <div class="tab-content mt-3">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Title</th>
            <th>Category</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="article in filteredArticles" :key="article.id">
            <td>{{ article.title }}</td>
            <td>{{ article.category }}</td>
            <td>
              <button @click="editArticle(article.id)" class="btn btn-sm btn-primary me-2">
                <i class="fas fa-edit"></i> Edit
              </button>
              <button @click="trashArticle(article.id)" class="btn btn-sm btn-danger">
                <i class="fas fa-trash"></i> Trash
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.nav-tabs .nav-link.active {
  background-color: #0d6efd !important;
  color: white !important;
}
</style>

<script>
import api from '@/services/api'

export default {
  name: 'AllPosts',
  data() {
    return {
      articles: [],
      activeTab: 'publish'
    }
  },
  computed: {
    filteredArticles() {
      return this.articles.filter(article => article.status === this.activeTab)
    }
  },
  methods: {
    async fetchArticles() {
      try {
        const response = await api.getArticles(100, 0)
        this.articles = response.data
      } catch (error) {
        console.error('Error fetching articles:', error)
      }
    },
    editArticle(id) {
      this.$router.push(`/edit/${id}`)
    },
    async trashArticle(id) {
      try {
        const article = this.articles.find(a => a.id === id)
        await api.updateArticle(id, { ...article, status: 'thrash' })
        this.fetchArticles()
      } catch (error) {
        console.error('Error trashing article:', error)
      }
    }
  },
  mounted() {
    this.fetchArticles()
  }
}
</script>