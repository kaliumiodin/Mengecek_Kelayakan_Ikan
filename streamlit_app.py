import streamlit as st

st.set_page_config(
    page_title="Cek Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

st.title("Aplikasi Evaluasi Kelayakan Bahan Pangan")

st.subheader("Sistem Pendukung Keputusan Berbasis Parameter Organoleptik")

st.write(
    "Selamat datang di aplikasi evaluasi kelayakan bahan pangan. "
    "Aplikasi ini bertujuan membantu pengguna dalam menentukan apakah "
    "bahan pangan masih layak untuk diolah atau dikonsumsi berdasarkan "
    "parameter organoleptik sederhana."
)

st.markdown("---")

st.header("Tujuan Aplikasi")
st.write(
    "- Menilai kelayakan bahan pangan\n"
    "- Mengurangi risiko konsumsi bahan tidak layak\n"
    "- Memberikan rekomendasi pengolahan yang tepat"
)

st.markdown("---")

st.header("Fitur Utama")
st.write(
    "- Evaluasi ikan\n"
    "- Evaluasi daging\n"
    "- Evaluasi sayur\n"
    "- Evaluasi buah"
)

st.info("Gunakan menu navigasi untuk melanjutkan evaluasi bahan pangan.")
