import streamlit as st

# HARUS PALING ATAS
st.set_page_config(
    page_title="Cek Kelayakan Bahan Pangan",
    page_icon="🥬",
    layout="wide"
)

# CSS KUAT (DIJAMIN WORK)
st.markdown("""
<style>
.stApp {
    background-color: #e8f5e9;
}

section[data-testid="stSidebar"] {
    background-color: #a5d6a7;
}

h1, h2, h3 {
    color: #1b5e20;
}

div.stButton > button {
    background-color: #2e7d32;
    color: white;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    font-weight: bold;
}

div[data-baseweb="select"] > div {
    background-color: #ffffff;
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGASI
menu = st.sidebar.radio(
    "🌱 Pilih Bahan Pangan",
    ["🏠 Home", "🐟 Ikan", "🥩 Daging", "🥦 Sayur", "🍎 Buah"]
)

# HOME
if menu == "🏠 Home":
    st.title("🌿 Aplikasi Evaluasi Kelayakan Bahan Pangan")
    st.write("""
    Aplikasi ini membantu mengevaluasi **kesegaran dan kelayakan bahan pangan**
    berdasarkan parameter fisik dan organoleptik.
    """)
    st.success("Pilih kategori bahan pangan di sidebar")

# IKAN
elif menu == "🐟 Ikan":
    st.title("🐟 Evaluasi Kesegaran Ikan")

    bau = st.selectbox("Bau", ["Segar", "Agak amis", "Busuk"])
    mata = st.selectbox("Mata", ["Jernih", "Agak keruh", "Keruh"])
    tekstur = st.selectbox("Tekstur daging", ["Kenyal", "Agak lembek", "Lembek"])

    if st.button("Evaluasi Ikan"):
        if bau == "Busuk" or tekstur == "Lembek":
            st.error("❌ Ikan tidak layak diolah")
        elif bau == "Segar" and mata == "Jernih":
            st.success("✅ Ikan segar")
            st.write("➡️ Olah: kukus, pepes, atau sup")
        else:
            st.warning("⚠️ Mutu menurun, segera diolah")

# DAGING
elif menu == "🥩 Daging":
    st.title("🥩 Evaluasi Kesegaran Daging")

    warna = st.selectbox("Warna", ["Merah segar", "Merah pucat", "Coklat"])
    bau = st.selectbox("Bau", ["Segar", "Asam", "Busuk"])
    lendir = st.selectbox("Permukaan", ["Tidak berlendir", "Berlendir"])

    if st.button("Evaluasi Daging"):
        if bau == "Busuk" or lendir == "Berlendir":
            st.error("❌ Daging tidak layak konsumsi")
        elif warna == "Merah segar":
            st.success("✅ Daging masih layak")
            st.write("➡️ Olah: rebus atau tumis matang")
        else:
            st.warning("⚠️ Kualitas menurun")

# SAYUR
elif menu == "🥦 Sayur":
    st.title("🥦 Evaluasi Kesegaran Sayur")

    warna = st.selectbox("Warna", ["Segar", "Layuh", "Menguning"])
    bau = st.selectbox("Bau", ["Normal", "Tidak sedap"])
    tekstur = st.selectbox("Tekstur", ["Keras", "Lembek"])

    if st.button("Evaluasi Sayur"):
        if bau == "Tidak sedap" or tekstur == "Lembek":
            st.error("❌ Sayur tidak layak")
        elif warna == "Segar":
            st.success("✅ Sayur layak konsumsi")
            st.write("➡️ Olah: tumis cepat / kukus")
        else:
            st.warning("⚠️ Segera olah")

# BUAH
elif menu == "🍎 Buah":
    st.title("🍎 Evaluasi Kesegaran Buah")

    warna = st.selectbox("Warna", ["Cerah", "Kusam"])
    bau = st.selectbox("Bau", ["Normal", "Fermentasi"])
    tekstur = st.selectbox("Tekstur", ["Keras", "Lembek"])

    if st.button("Evaluasi Buah"):
        if bau == "Fermentasi":
            st.error("❌ Buah tidak layak")
        elif warna == "Cerah" and tekstur == "Keras":
            st.success("✅ Buah segar")
            st.write("➡️ Konsumsi langsung / jus")
        else:
            st.warning("⚠️ Mutu menurun")

