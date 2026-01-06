import streamlit as st

st.set_page_config(
    page_title="Cek Kelayakan Bahan Pangan",
    page_icon="🐟",
    layout="wide"
)

st.markdown("""
<style>
/* Background utama */
.stApp {
    background-color: #e8f5e9;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #a5d6a7;
}

/* Judul */
h1, h2, h3 {
    color: #1b5e20;
}

/* Button */
div.stButton > button {
    background-color: #43a047;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}

/* Selectbox & Input */
div[data-baseweb="select"] > div,
input {
    background-color: #ffffff;
    border-radius: 8px;
}

/* Alert sukses */
div[data-testid="stAlert"] {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "🌿 Pilih Jenis Bahan Pangan",
    ["🐟 Ikan", "🥩 Daging", "🥦 Sayur", "🍎 Buah"]
)
if menu == "🐟 Ikan":
    st.title("🐟 Evaluasi Kelayakan Kesegaran Ikan")

    jenis_ikan = st.selectbox(
        "Jenis ikan",
        ["Ikan Laut", "Ikan Air Tawar"]
    )

    bau = st.selectbox(
        "Bau ikan",
        ["Segar", "Agak amis", "Busuk"]
    )

    mata = st.selectbox(
        "Kondisi mata",
        ["Jernih", "Agak keruh", "Keruh"]
    )

    tekstur = st.selectbox(
        "Tekstur daging",
        ["Kenyal", "Agak lembek", "Lembek"]
    )

    if st.button("🔍 Evaluasi"):
        if bau == "Busuk" or tekstur == "Lembek":
            st.error("❌ Ikan TIDAK layak diolah")
            st.write("➡️ Disarankan untuk dibuang")
        elif bau == "Segar" and mata == "Jernih":
            st.success("✅ Ikan SEGAR")
            st.write("➡️ Olah dengan cara: kukus / pepes")
        else:
            st.warning("⚠️ Kualitas ikan MENURUN")
            st.write("➡️ Olah segera, hindari penyimpanan lama")
