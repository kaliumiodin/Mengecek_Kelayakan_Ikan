import streamlit as st

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Smart Food Freshness Checker",
    page_icon="🥬",
    layout="wide"
)

# ======================
# CSS CUSTOM (GREEN THEME)
# ======================
st.markdown("""
<style>
.main {
    background-color: #f4fff6;
}
h1, h2, h3 {
    color: #1b7f5c;
}
.stButton>button {
    background-color: #2ecc71;
    color: white;
    border-radius: 10px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #27ae60;
}
.stSidebar {
    background-color: #e6f7ec;
}
div[data-testid="stMetric"] {
    background-color: #eafff1;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# SIDEBAR NAVIGASI
# ======================
menu = st.sidebar.radio(
    "🌿 Navigasi",
    (
        "🏠 Home",
        "🐟 Ikan",
        "🥩 Daging",
        "🥬 Sayur",
        "🍎 Buah",
        "ℹ️ Tentang"
    )
)

# ======================
# HOME
# ======================
if menu == "🏠 Home":
    st.title("🌿 Smart Food Freshness Checker")
    st.subheader("Evaluasi Kesegaran & Rekomendasi Pengolahan Bahan Pangan")

    st.markdown("""
    Aplikasi ini membantu menentukan **kelayakan bahan pangan**
    (ikan, daging, sayur, dan buah) berdasarkan parameter organoleptik
    serta memberikan **langkah pengolahan yang disarankan**.
    """)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🐟 Ikan", "Organoleptik")
    col2.metric("🥩 Daging", "Keamanan")
    col3.metric("🥬 Sayur", "Kesegaran")
    col4.metric("🍎 Buah", "Kematangan")

# ======================
# IKAN
# ======================
elif menu == "🐟 Ikan":
    st.header("🐟 Evaluasi Kesegaran Ikan")

    bau = st.selectbox("Bau", ["Segar", "Agak Asam", "Busuk"])
    tekstur = st.selectbox("Tekstur", ["Kenyal", "Lembek"])
    insang = st.selectbox("Warna Insang", ["Merah Cerah", "Pucat", "Coklat"])
    hari = st.number_input("Lama Penyimpanan (hari)", 0, 14)

    if st.button("🔍 Evaluasi Ikan"):
        skor = 0
        if bau != "Segar": skor += 2
        if tekstur != "Kenyal": skor += 1
        if insang != "Merah Cerah": skor += 2
        if hari > 3: skor += 2

        if skor >= 6:
            st.error("❌ Ikan tidak layak konsumsi")
            st.write("➡️ **Tindakan:** Buang bahan pangan")
        elif skor >= 3:
            st.warning("⚠️ Ikan kurang segar")
            st.write("➡️ **Tindakan:** Masak suhu tinggi")
        else:
            st.success("✅ Ikan segar")
            st.write("➡️ **Tindakan:** Kukus, pepes, atau tumis cepat")

# ======================
# DAGING
# ======================
elif menu == "🥩 Daging":
    st.header("🥩 Evaluasi Kelayakan Daging")

    warna = st.selectbox("Warna Daging", ["Merah Cerah", "Coklat", "Abu-abu"])
    bau = st.selectbox("Bau", ["Segar", "Asam", "Busuk"])
    lendir = st.selectbox("Lendir", ["Tidak Ada", "Ada"])
    hari = st.number_input("Lama Penyimpanan (hari)", 0, 7)

    if st.button("🔍 Evaluasi Daging"):
        skor = 0
        if warna != "Merah Cerah": skor += 2
        if bau != "Segar": skor += 2
        if lendir == "Ada": skor += 2
        if hari > 3: skor += 2

        if skor >= 6:
            st.error("❌ Daging tidak layak konsumsi")
        elif skor >= 3:
            st.warning("⚠️ Daging harus dimasak matang")
        else:
            st.success("✅ Daging layak konsumsi")

# ======================
# SAYUR
# ======================
elif menu == "🥬 Sayur":
    st.header("🥬 Evaluasi Kesegaran Sayur")

    warna = st.selectbox("Warna", ["Hijau Segar", "Kusam", "Menguning"])
    tekstur = st.selectbox("Tekstur", ["Renyah", "Layu"])
    bercak = st.selectbox("Bercak", ["Tidak Ada", "Ada"])

    if st.button("🔍 Evaluasi Sayur"):
        if warna == "Hijau Segar" and tekstur == "Renyah" and bercak == "Tidak Ada":
            st.success("✅ Sayur segar → kukus / tumis cepat")
        else:
            st.warning("⚠️ Sayur menurun kualitas → segera olah")

# ======================
# BUAH
# ======================
elif menu == "🍎 Buah":
    st.header("🍎 Evaluasi Kesegaran Buah")

    aroma = st.selectbox("Aroma", ["Normal", "Fermentasi"])
    tekstur = st.selectbox("Tekstur", ["Keras", "Lembek"])
    jamur = st.selectbox("Jamur", ["Tidak Ada", "Ada"])

    if st.button("🔍 Evaluasi Buah"):
        if aroma == "Normal" and tekstur == "Keras" and jamur == "Tidak Ada":
            st.success("✅ Buah segar → konsumsi langsung")
        else:
            st.warning("⚠️ Buah rusak → olah atau buang")

# ======================
# TENTANG
# ======================
elif menu == "ℹ️ Tentang":
    st.header("ℹ️ Tentang Aplikasi")
    st.write("""
    Aplikasi edukatif berbasis logika pemrograman pangan.
    Digunakan untuk pembelajaran dan bukan pengganti uji laboratorium.
    """)
