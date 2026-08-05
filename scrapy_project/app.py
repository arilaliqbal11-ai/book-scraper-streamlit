import streamlit as st
import json
import os

# Path menuju file JSON hasil crawl
DATA_PATH = "data/books.json"

st.set_page_config(page_title="Book Search (Scraped via Scrapy)", layout="wide")
st.title("📚 Book Search (Scraped via Scrapy)")

# Load data dari JSON
if os.path.exists(DATA_PATH):
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    # Cek lokasi alternatif jika folder data berada di subfolder
    alt_path = "../data/books.json"
    if os.path.exists(alt_path):
        with open(alt_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        st.warning("Data belum tersedia. Jalankan crawler terlebih dahulu.")
        st.stop()

# Input pencarian
query = st.text_input("Cari judul buku:", "")

# Filter data berdasarkan judul
if query:
    filtered = [item for item in data if query.lower() in item.get("title", "").lower()]
else:
    filtered = data

st.markdown(f"### Ditemukan {len(filtered)} hasil")
st.write("---")

# Menampilkan data buku
for item in filtered:
    st.markdown(f"### [{item.get('title', 'No Title')}]({item.get('link', '#')})")
    st.markdown(f"**Price:** `{item.get('price', '-')}` | **Rating:** `{item.get('rating', '-')}` | **Availability:** `{item.get('availability', '-')}`")
    st.write("---")