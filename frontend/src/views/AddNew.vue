<template>
  <div class="container mt-4">
    <h2>Add New Article</h2>
    
    <form @submit.prevent="submitArticle">
      <div class="mb-3">
        <label class="form-label">Title</label>
        <input v-model="article.title" type="text" class="form-control" required>
      </div>
      
      <div class="mb-3">
        <label class="form-label">Content</label>
        <textarea v-model="article.content" class="form-control" rows="10" required></textarea>
      </div>
      
      <div class="mb-3">
        <label class="form-label">Category</label>
        <input v-model="article.category" type="text" class="form-control" required>
      </div>
      
      <div class="mb-3">
        <button type="button" @click="saveAsDraft" class="btn btn-secondary me-2">
          Save as Draft
        </button>
        <button type="button" @click="publish" class="btn btn-primary">
          Publish
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import api from '@/services/api'

export default {
  name: 'AddNew',
  data() {
    return {
      article: {
        title: '',
        content: '',
        category: '',
        status: 'draft'
      }
    }
  },
  methods: {
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
        await api.createArticle(this.article)
        this.$router.push('/all-posts')
      } catch (error) {
        console.error('Error creating article:', error)
        alert('Error creating article. Please check the validation requirements.')
      }
    }
  }
}
</script>