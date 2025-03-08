# E-Commerce Data Dashboard

## 📌 Deskripsi
Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data transaksi e-commerce. Dashboard ini menampilkan:
1. **Analisis Produk** - Kategori produk yang paling banyak dibeli.
2. **Analisis Waktu Pengiriman** - Distribusi waktu pengiriman pesanan ke pelanggan.

---

## 🚀 Cara Menjalankan Dashboard

### **1. Clone Repository atau Download File**
Jika menggunakan Git, jalankan:
```bash
git clone https://github.com/Favmos/Analisis-Data-E-commerce.git 
Navigasi ke direktori tempat aplikasi diekstrak, misalnya:
cd C:\Users\MSI GAMING\Downloads\Dicoding
```
Atau, **unduh dan ekstrak** file ZIP proyek ini ke folder lokal Anda.

### **2. Install Dependensi**
```bash
Membuat Environment dengan perintah : python -m venv venv
Mengaktifkan Environment : venv\Scripts\activate

```
### **3. Install Dependensi**
Pastikan Anda telah menginstal Python 3.7 atau lebih baru, lalu jalankan:
```bash
pip install -r requirements.txt (atau install requirements satu satu secara bergantian)
streamlit==1.25.0
pandas==1.5.3
matplotlib==3.7.1
seaborn==0.12.2
pyngrok==5.2.2
```

### **3. Jalankan Streamlit**
Gunakan perintah berikut untuk menjalankan dashboard:
```bash
streamlit run "Train Streamlit.py"
```

Jika menggunakan **Google Colab**, jalankan kode berikut:
```python
!pip install streamlit pyngrok
from pyngrok import ngrok
!streamlit run Train_Streamlit.py & npx localtunnel --port 8501
```
Link akan muncul untuk mengakses dashboard secara online.

---

## 🔥 Fitur Dashboard
✅ **Top 10 Produk Terlaris** - Menampilkan kategori produk yang paling banyak terjual.
✅ **Distribusi Waktu Pengiriman** - Histogram yang menunjukkan durasi pengiriman pesanan.
✅ **Statistik Pengiriman** - Rata-rata, median, dan variasi waktu pengiriman.

---

## 🛠 Troubleshooting
Jika terjadi error "FileNotFoundError", pastikan dataset telah diekstrak ke lokasi yang benar.
- **Periksa lokasi dataset**: Cek folder "E-Commerce Public Dataset" dalam direktori proyek Anda.
- **Ubah path dataset**: Jika perlu, perbarui `dataset_path` di `Train_Streamlit.py` agar sesuai dengan lokasi file Anda.

---


