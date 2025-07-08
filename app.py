import streamlit as st
import spacy
import gdown
import zipfile
from pathlib import Path

# --- Configuration ---
DRIVE_FOLDER_URL = "https://drive.google.com/file/d/1zSPRvW5u0qhO-269WQmfW5hLGDybKye1/view?usp=sharing"
MODEL_ZIP_PATH = "model-best.zip"
MODEL_DIR = Path("model-best")

@st.cache_resource
def load_model():
    # Download and unzip the model if not already present
    if not MODEL_DIR.exists():
        st.info("Downloading custom NER model...")
        gdown.download(DRIVE_FOLDER_URL, MODEL_ZIP_PATH, quiet=False)
        with zipfile.ZipFile(MODEL_ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(".")
    return spacy.load(MODEL_DIR)

nlp = load_model()

# UI
st.set_page_config(page_title="Custom NER", layout="wide")
st.title("🧠 Named Entity Recognition (NER)")
st.markdown("This app uses your custom spaCy model for detecting entities like names, addresses, etc.")

# Input
text_input = st.text_area("✍️ Enter text below:", height=200, value="""Your text here...""")
uploaded_file = st.file_uploader("📄 Or upload a .txt file", type=["txt"])
if uploaded_file is not None:
    text_input = uploaded_file.read().decode("utf-8")

# Prediction
if st.button("🚀 Run NER"):
    if not text_input.strip():
        st.warning("Please enter some text.")
    else:
        doc = nlp(text_input)
        st.markdown("### 📌 Detected Entities")
        if not doc.ents:
            st.info("No entities found.")
        else:
            for ent in doc.ents:
                st.markdown(f"- **{ent.text}** → `{ent.label_}`")
        st.markdown("### 🖍️ Highlighted Text")
        st.markdown(spacy.displacy.render(doc, style="ent", jupyter=False), unsafe_allow_html=True)
