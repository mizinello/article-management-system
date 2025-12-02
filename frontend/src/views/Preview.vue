<template>
  <div class="container mt-4">
    <h2>Published Articles Preview</h2>
    
    <div v-if="loading" class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    
    <div v-else>
      <!-- Articles Grid -->
      <div class="row">
        <div class="col-md-6 col-lg-4 mb-4" v-for="article in paginatedArticles" :key="article.id">
          <div class="card h-100">
            <div class="card-header">
              <h5 class="card-title mb-0">{{ article.title }}</h5>
              <small class="text-muted">
                <i class="fas fa-tag"></i> {{ article.category }}
              </small>
            </div>
            <div class="card-body">
              <p class="card-text">{{ getContentPreview(article.content) }}</p>
            </div>
            <div class="card-footer text-muted">
              <small>
                <i class="fas fa-calendar"></i> 
                {{ formatDate(article.created_date) }}
              </small>
            </div>
          </div>
        </div>
      </div>
      
      <!-- No Articles Message -->
      <div v-if="publishedArticles.length === 0" class="text-center py-5">
        <i class="fas fa-newspaper fa-3x text-muted mb-3"></i>
        <h4 class="text-muted">No Published Articles</h4>
        <p class="text-muted">Start by creating and publishing your first article!</p>
        <router-link to="/add-new" class="btn btn-primary">
          <i class="fas fa-plus"></i> Add New Article
        </router-link>
      </div>
      
      <!-- Pagination -->
      <nav v-if="totalPages > 1" aria-label="Article pagination">
        <ul class="pagination justify-content-center">
          <li class="page-item" :class="{ disabled: currentPage === 1 }">
            <button class="page-link" @click="changePage(currentPage - 1)" :disabled="currentPage === 1">
              <i class="fas fa-chevron-left"></i> Previous
            </button>
          </li>
          
          <li class="page-item" v-for="page in visiblePages" :key="page" :class="{ active: page === currentPage }">
            <button class="page-link" @click="changePage(page)">{{ page }}</button>
          </li>
          
          <li class="page-item" :class="{ disabled: currentPage === totalPages }">
            <button class="page-link" @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages">
              Next <i class="fas fa-chevron-right"></i>
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'Preview',
  data() {
    return {
      articles: [],
      loading: true,
      currentPage: 1,
      articlesPerPage: 6
    }
  },
  computed: {
    publishedArticles() {
      return this.articles.filter(article => article.status === 'publish')
    },
    totalPages() {
      return Math.ceil(this.publishedArticles.length / this.articlesPerPage)
    },
    visiblePages() {
      const pages = []
      const start = Math.max(1, this.currentPage - 2)
      const end = Math.min(this.totalPages, this.currentPage + 2)
      
      for (let i = start; i <= end; i++) {
        pages.push(i)
      }
      return pages
    },
    paginatedArticles() {
      const start = (this.currentPage - 1) * this.articlesPerPage
      const end = start + this.articlesPerPage
      return this.publishedArticles.slice(start, end)
    }
  },
  methods: {
    async fetchArticles() {
      try {
        const response = await api.getArticles(100, 0)
        this.articles = response.data
        this.loading = false
      } catch (error) {
        console.error('Error fetching articles:', error)
        this.loading = false
      }
    },
    changePage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page
      }
    },
    getContentPreview(content) {
      return content.length > 150 ? content.substring(0, 150) + '...' : content
    },
    formatDate(dateString) {
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }
  },
  mounted() {
    this.fetchArticles()
  }
}
</script>

<style scoped>
.card {
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.1rem;
  line-height: 1.3;
}

.card-text {
  font-size: 0.9rem;
  line-height: 1.5;
}
</style>