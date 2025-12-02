<template>
  <div class="container mt-4">
    <h2>Edit Article</h2>
    
    <div v-if="loading" class="text-center">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
    
    <form v-else @submit.prevent="submitArticle">
      <div class="mb-3">
        <label class="form-label">Title</label>
        <input v-model="article.title" type="text" class="form-control" required>
        <div class="form-text">Minimum 20 characters required</div>
      </div>
      
      <div class="mb-3">
        <label class="form-label">Content</label>
        <textarea v-model="article.content" class="form-control" rows="10" required></textarea>
        <div class="form-text">Minimum 200 characters required</div>
      </div>
      
      <div class="mb-3">
        <label class="form-label">Category</label>
        <input v-model="article.category" type="text" class="form-control" required>
        <div class="form-text">Minimum 3 characters required</div>
      </div>
      
      <div class="mb-3">
        <button type="button" @click="saveAsDraft" class="btn btn-secondary me-2">
          <i class="fas fa-save"></i> Save as Draft
        </button>
        <button type="button" @click="publish" class="btn btn-primary me-2">
          <i class="fas fa-paper-plane"></i> Publish
        </button>
        <router-link to="/all-posts" class="btn btn-outline-secondary">
          <i class="fas fa-times"></i> Cancel
        </router-link>
      </div>
    </form>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'EditArticle',
  data() {
    return {
      article: {
        title: '',
        content: '',
        category: '',
        status: 'draft'
      },
      loading: true
    }
  },
  methods: {
    async fetchArticle() {
      try {
        const response = await api.getArticle(this.$route.params.id)
        this.article = response.data
        this.loading = false
      } catch (error) {
        console.error('Error fetching article:', error)
        this.$router.push('/all-posts')
      }
    },
    async saveAsDraft() {
      this.article.status = 'draft'
      await this.submitArticle()
    },
    async publish() {
      this.article.status = 'publish'
      await this.submitArticle()
    },
    async submitArticle() {
      try {
        await api.updateArticle(this.$route.params.id, this.article)
        this.$router.push('/all-posts')
      } catch (error) {
        console.error('Error updating article:', error)
        alert('Error updating article. Please check the validation requirements.')
      }
    }
  },
  mounted() {
    this.fetchArticle()
  }
}
</script>