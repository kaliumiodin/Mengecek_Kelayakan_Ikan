import streamlit as st

# ======================
# KONFIGURASI HALAMAN
# ======================
st.set_page_config(
    page_title="Smart Fish Quality Checker",
    page_icon="🐟",
    layout="wide"
)

# ======================
# SIDEBAR NAVIGASI
# ======================
menu = st.sidebar.radio(
    "📌 Menu Navigasi",
    (
        "🏠 Beranda",
        "🔍 Evaluasi Kesegaran Ikan",
        "🍳 Rekomendasi Pengolahan",
        "ℹ️ Tentang Aplikasi"
    )
)

# ======================
# BERANDA
# ======================
if menu == "🏠 Beranda":
    st.title("🐟 Smart Fish Quality Checker")
    st.markdown(
        """
        Aplikasi ini membantu mengevaluasi **kelayakan kesegaran ikan**
        berdasarkan parameter organoleptik dan penyimpanan,
        serta memberikan **langkah pengolahan terbaik** agar nutrisi tidak rusak.
        """
    )

    st.info("📌 Cocok untuk mahasiswa pangan, laboratorium, dan UMKM perikanan.")

# ======================
# EVALUASI IKAN
# ======================
elif menu == "🔍 Evaluasi Kesegaran Ikan":
    st.title("🔍 Evaluasi Kesegaran Ikan")

    col1, col2 = st.columns(2)

    with col1:
        jenis_ikan = st.selectbox(
            "Jenis Ikan",
            ["Ikan Berlemak", "Ikan Daging Putih", "Ikan Air Tawar", "Ikan Kecil"]
        )

        bau = st.selectbox(
            "Bau",
            ["Segar", "Agak Asam", "Busuk"]
        )

        tekstur = st.selectbox(
            "Tekstur Daging",
            ["Kenyal", "Agak Lembek", "Lembek"]
        )

        mata = st.selectbox(
            "Kondisi Mata",
            ["Jernih", "Agak Keruh", "Keruh"]
        )

    with col2:
        warna_insang = st.selectbox(
            "Warna Insang",
            ["Merah Cerah", "Merah Pucat", "Coklat"]
        )

        lendir = st.selectbox(
            "Lendir",
            ["Bening", "Agak Keruh", "Keruh & Lengket"]
        )

        suhu = st.number_input(
            "Suhu Penyimpanan (°C)",
            min_value=0,
            max_value=30,
            step=1
        )

        hari = st.number_input(
            "Lama Penyimpanan (hari)",
            min_value=0,
            max_value=14,
            step=1
        )

    if st.button("🧪 Analisis Kelayakan"):
        skor = 0

        if bau != "Segar": skor += 2
        if tekstur != "Kenyal": skor += 1
        if mata != "Jernih": skor += 1
        if warna_insang != "Merah Cerah": skor += 2
        if lendir != "Bening": skor += 1
        if suhu > 5: skor += 1
        if hari > 3: skor += 2

        st.markdown("---")
        st.subheader("📊 Hasil Evaluasi")

        if skor >= 7:
            st.error("❌ IKAN TIDAK LAYAK DIOlah")
            st.write("🔴 Risiko pembusukan tinggi")
            st.write("➡️ **Langkah:** Buang, tidak disarankan konsumsi")

        elif skor >= 4:
            st.warning("⚠️ IKAN KURANG SEGAR")
            st.write("🟡 Risiko sedang")
            st.write("➡️ **Langkah:** Olah dengan suhu tinggi segera")

        else:
            st.success("✅ IKAN MASIH SEGAR")
            st.write("🟢 Risiko rendah")
            st.write("➡️ **Langkah:** Aman diolah dengan metode minim panas")

# ======================
# REKOMENDASI OLAHAN
# ======================
elif menu == "🍳 Rekomendasi Pengolahan":
    st.title("🍳 Rekomendasi Pengolahan Ikan")

    st.markdown(
        """
        ### Metode Pengolahan Aman Nutrisi:
        - 🟢 **Ikan segar:** Kukus, pepes, tumis cepat  
        - 🟡 **Kurang segar:** Goreng matang, sup panas  
        - 🔴 **Tidak segar:** Tidak direkomendasikan  
        
        ### Tips Menjaga Nutrisi:
        - Hindari pemanasan terlalu lama  
        - Gunakan suhu stabil  
        - Minimalkan kontak udara  
        """
    )

# ======================
# TENTANG
# ======================
elif menu == "ℹ️ Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")
    st.write(
        """
        Aplikasi ini dikembangkan sebagai media edukasi
        untuk evaluasi kesegaran ikan berbasis logika pemrograman.
        
        📌 Tidak menggantikan uji laboratorium resmi.
        """
    )
