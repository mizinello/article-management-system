# 📝 Article Management System — Sharing Vision Technical Test 2025

Project ini adalah hasil pengerjaan tes Backend & Frontend untuk use case **Post Article** sesuai spesifikasi dari *Sharing Vision Technical Test 2021*.  
Aplikasi dibangun menggunakan **Python Flask** untuk backend dan **Vue 3 (Vite)** untuk frontend.

---

## 🚀 Fitur Utama

### 🔧 Backend (Python Flask)
- REST API untuk CRUD Article
- Validasi data lengkap:
  - `title`: required, min 20 karakter
  - `content`: required, min 200 karakter
  - `category`: required, min 3 karakter
  - `status`: harus `publish`, `draft`, atau `thrash`
- Pagination (limit & offset)
- Migrasi database menggunakan Flask-Migrate
- MySQL sebagai database
- Struktur modular (routes, models, validators, config)
- Soft delete: artikel berpindah ke tab *Trash*

---

### 🖥️ Frontend (Vue 3)
- Halaman **All Posts** dengan tabs:
  - Published
  - Drafts
  - Trashed
- Tabel artikel berisi:
  - Title
  - Category
  - Action (Edit & Trash)
- Halaman **Add New**:
  - Form dengan Title, Content, Category
  - Tombol **Publish** & **Draft**
- Halaman **Edit**:
  - Bisa update Title, Content, Category
  - Tombol Publish / Draft
- Halaman **Preview**:
  - Menampilkan artikel berstatus publish
  - Pagination
- Integrasi penuh ke REST API Flask

---

## 🗄️ Struktur Database (Tabel `posts`)

| Kolom        | Tipe Data         | Keterangan |
|--------------|-------------------|------------|
| id           | INT AUTO_INCREMENT | Primary Key |
| title        | VARCHAR(200)      | min 20 char |
| content      | TEXT              | min 200 char |
| category     | VARCHAR(100)      | min 3 char |
| created_date | TIMESTAMP         | default now |
| updated_date | TIMESTAMP         | auto update |
| status       | VARCHAR(100)      | publish / draft / thrash |

---

