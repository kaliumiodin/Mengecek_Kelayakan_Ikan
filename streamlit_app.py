import streamlit as st

st.set_page_config(
    page_title="Cek Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

# ===== BERANDA =====
st.title("🥗 Aplikasi Evaluasi Kelayakan Bahan Pangan")

st.subheader("Sistem Pendukung Keputusan Berbasis Parameter Organoleptik")

st.write("""
**Selamat datang!**

Aplikasi ini dirancang untuk membantu pengguna dalam **mengevaluasi kelayakan
dan kesegaran bahan pangan** sebelum diolah atau dikonsumsi.
Evaluasi dilakukan berdasarkan **parameter organoleptik sederhana**
seperti warna, bau, tekstur, serta kondisi fisik bahan pangan.
""")

st.markdown("---")

st.header("🎯 Tujuan Aplikasi")
st.write("""
1. Membantu menentukan apakah bahan pangan masih **layak diolah atau dikonsumsi**
2. Mengurangi risiko konsumsi bahan pangan yang tidak aman
3. Memberikan **rekomendasi pengolahan** agar mutu dan kandungan gizi tetap terjaga
""")

st.markdown("---")

st.header("📌 Fitur Utama")
st.write("""
- Evaluasi kelayakan **ikan**
- Evaluasi kelayakan **daging**
- Evaluasi kelayakan **sayur**
- Evaluasi kelayakan **buah**
- Rekomendasi metode pengolahan yang sesuai
""")

st.info("👉 Gunakan menu navigasi untuk memilih jenis bahan pangan yang ingin dievaluasi.")
