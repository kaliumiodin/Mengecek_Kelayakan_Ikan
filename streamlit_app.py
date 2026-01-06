import streamlit as st

st.set_page_config(
    page_title="Cek Kelayakan Bahan Pangan",
    page_icon="🥗",
    layout="wide"
)

# ===== SIDEBAR =====
st.sidebar.title("🧭 Navigasi")
menu = st.sidebar.radio(
    "Pilih Bahan Pangan:",
    ["🏠 Beranda", "🐟 Ikan", "🥩 Daging", "🥦 Sayur", "🍎 Buah"]
)

# ===== BERANDA =====
if menu == "🏠 Beranda":
    st.title("🥗 Aplikasi Evaluasi Kelayakan Bahan Pangan")
    st.write("""
    Aplikasi ini membantu menentukan **kelayakan bahan pangan**
    berdasarkan **parameter fisik dan organoleptik**, serta
    memberikan **rekomendasi pengolahan** agar kualitas gizi tetap terjaga.
    """)

    st.info("""
    📌 Bahan yang dapat dievaluasi:
    - Ikan
    - Daging
    - Sayur
    - Buah
    """)

# ===== IKAN =====
elif menu == "🐟 Ikan":
    st.header("🐟 Evaluasi Kesegaran Ikan")

    bau = st.selectbox("Bau ikan", ["Segar", "Agak amis", "Busuk"])
    mata = st.selectbox("Kondisi mata", ["Jernih", "Agak keruh", "Keruh"])
    tekstur = st.selectbox("Tekstur daging", ["Kenyal", "Agak lembek", "Lembek"])

    if st.button("Evaluasi Ikan"):
        if bau == "Busuk" or tekstur == "Lembek":
            st.error("❌ Ikan TIDAK layak diolah")
        elif bau == "Segar" and mata == "Jernih":
            st.success("✅ Ikan segar dan layak")
            st.write("➡️ Rekomendasi: kukus, pepes, atau sup")
        else:
            st.warning("⚠️ Kualitas menurun, segera diolah")

# ===== DAGING =====
elif menu == "🥩 Daging":
    st.header("🥩 Evaluasi Kesegaran Daging")

    warna = st.selectbox("Warna daging", ["Merah segar", "Merah pucat", "Coklat"])
    bau = s
