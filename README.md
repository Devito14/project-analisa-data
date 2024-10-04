# Dashboard Analisis Data: Bike Sharing Dataset

## Deskripsi
Dashboard ini adalah aplikasi analisis data untuk penyewaan sepeda, yang menyajikan analisis data interaktif menggunakan **Streamlit**. Dashboard ini menyajikan visualisasi dan analisis yang membantu dalam memahami pola penyewaan sepeda berdasarkan faktor-faktor seperti cuaca, musim, dan jenis hari dalam seminggu.

## Struktur Direktori
Berikut adalah struktur direktori proyek:
submission/
├───dashboard/
│   ├───dashboard.py            # Kode untuk menjalankan dashboard
│   └───main_data.csv           # Data yang digunakan untuk dashboard.py (sudah bersih)
├───data/
│   └───hour.csv                # Dataset yang belum diolah (masih mungkin ada kesalahan)
├───notebook.ipynb              # File untuk menganalisis Dataset mentah
├───README.md                   # Penjelasan cara menggunakan dashboard
├───requirements.txt            # Daftar pustaka yang dibutuhkan
└───url.text                    # Tautan untuk dashboard


## Setup Environment - Shell/Terminal

1. **Buka terminal**.

2. **Navigasikan ke direktori proyek:**
    ```bash
    cd \go\to\files\path
    ```
    Ubah \go\to\files\path menjadi path penyimpanan file submission

3. **Buat lingkungan virtual menggunakan venv:**
    ```bash
    python -m venv analisa-peminjaman-sepeda
    ```

4. **Aktifkan lingkungan virtual:**
   - **Di Windows**:
     ```bash
     analisa-peminjaman-sepeda\Scripts\activate
     ```
   - **Di Mac/Linux**:
     ```bash
     source analisa-peminjaman-sepeda/bin/activate
     ```

5. **Instal semua dependensi dari `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Untuk menjalankan aplikasi **Streamlit**, gunakan perintah berikut di terminal:

```bash
streamlit run dashboard/dashboard.py
```

## Catatan
- Pastikan Anda telah menginstal Python (versi 3.6 atau lebih baru)
- Aplikasi ini dirancang dan diuji menggunakan Python versi 3.12.2.