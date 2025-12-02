<template>
  <div id="app">
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <router-link class="navbar-brand" to="/">
          <i class="fas fa-newspaper"></i> Article Management
        </router-link>
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="/all-posts" active-class="active">
                <i class="fas fa-list"></i> All Posts
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/add-new" active-class="active">
                <i class="fas fa-plus"></i> Add New
              </router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/preview" active-class="active">
                <i class="fas fa-eye"></i> Preview
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="py-4">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-light text-center py-3 mt-5">
      <div class="container">
        <p class="mb-0 text-muted">
          <i class="fas fa-copyright"></i> 2024 Article Management System
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}

.navbar-brand {
  font-weight: bold;
}

.nav-link.active {
  color: #fff !important;
  background-color: rgba(255, 255, 255, 0.1);
  border-radius: 0.25rem;
}

.table th {
  background-color: #f8f9fa;
  border-top: none;
}

.btn {
  border-radius: 0.25rem;
}

.form-control:focus {
  border-color: #80bdff;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.nav-tabs .nav-link.active {
  background-color: #007bff;
  border-color: #007bff;
  color: white;
}

.nav-tabs .nav-link:hover {
  border-color: #e9ecef #e9ecef #dee2e6;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>