import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#inialisasi variabel all_df
all_df = pd.read_csv("dashboard/main_data.csv")

#Mengatur judul
st.title("Bike Sharing Dashboard")

#Menampilkan dataset
st.subheader("Dataframe Head")
st.dataframe(all_df.head())

#Menampilkan statistics
st.subheader("Descriptive Statistics")
st.write(all_df.describe(include="all"))

# Visualisasi Distribusi Penyewaan berdasarkan Musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
plt.figure(figsize=(10,6))
sns.barplot(x="season", y="cnt", data=all_df)
plt.title("Pengaruh Musim terhadap Jumlah Penyewaan Sepeda")
plt.xlabel("Musim (1: Musim Dingin, 2: Musim Semi, 3: Musim Panas, 4: Musim Gugur)")
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

#Visualisasi Hari dalam seminggu vs Penyewaan
st.subheader("Hubungan Hari dalam Seminggu dan Penyewaan")
plt.figure(figsize=(10,6))
sns.barplot(x="weekday", y="cnt", data=all_df)
plt.title("Pengaruh Hari dalam Seminggu terhadap Jumlah Penyewaan Sepeda")
plt.xlabel("Hari")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(plt)

#Visualisasi Cuaca vs Penyewaan
st.subheader("Hubungan Cuaca dan Penyewaan")
plt.figure(figsize=(10,6))
sns.boxplot(x="weathersit", y="cnt", data=all_df)
plt.title("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda")
plt.xlabel("Cuaca")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(plt)


# Insight dari analisis
st.subheader("Insight dari Analisis")
insight_text = """
1. Rata-rata penyewaan sepeda adalah sekitar 1020.6 dengan variasi yang tinggi, menunjukkan 
   bahwa penyewaan sangat dipengaruhi oleh faktor-faktor eksternal seperti cuaca dan musim.
2. Cuacanya berpengaruh terhadap jumlah penyewa sepeda semakin bagus dan semakin cerah cuacanya 
   akan membuat jumlah penyewaan sepeda menjadi meningkat.
3. Berdasarkan analisa dengan menampilkan barplot,promosi penyewaan sepeda paling baik dilakukan 
   pada musim gugur dan pada hari kamis atau jumat. Selain itu, penting untuk memperhatikan cuaca 
   pada saat promosi.
"""
st.write(insight_text)
