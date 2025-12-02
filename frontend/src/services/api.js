import axios from 'axios'

const API_BASE_URL = 'http://localhost:5000'

export default {
  // Create article
  createArticle(data) {
    return axios.post(`${API_BASE_URL}/article/`, data)
  },
  
  // Get all articles
  getArticles(limit = 10, offset = 0) {
    return axios.get(`${API_BASE_URL}/article/${limit}/${offset}`)
  },
  
  // Get single article
  getArticle(id) {
    return axios.get(`${API_BASE_URL}/article/${id}`)
  },
  
  // Update article
  updateArticle(id, data) {
    return axios.put(`${API_BASE_URL}/article/${id}`, data)
  },
  
  // Delete article
  deleteArticle(id) {
    return axios.delete(`${API_BASE_URL}/article/${id}`)
  }
}