import streamlit as st
import spacy
import gdown
import zipfile
from pathlib import Path

# --- Setup paths and Google Drive link ---
DRIVE_ZIP_URL = "https://drive.google.com/uc?id=1zSPRvW5u0qhO-269WQmfW5hLGDybKye1"
MODEL_ZIP_PATH = "model-best.zip"
MODEL_DIR = Path("output/model-best")

# --- Load model only once ---
@st.cache_resource
def load_model():
    # If the model is not downloaded yet
    if not MODEL_DIR.exists():
        st.info("Downloading model...")
        gdown.download(DRIVE_ZIP_URL, MODEL_ZIP_PATH, quiet=False)

        # Unzip into output/
        with zipfile.ZipFile(MODEL_ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall("output")

    return spacy.load(MODEL_DIR)

# 🔁 Everything below is unchanged (your exact UI)
nlp = load_model()

st.set_page_config(page_title="Custom NER", layout="wide")
st.title("🧠 Named Entity Recognition (NER)")
st.markdown("This app uses your custom spaCy model for detecting entities like names, addresses, etc.")

text_input = st.text_area("✍️ Enter text below:", height=200, value="""My name is Andrew Callen Brooks, and I work—or worked—as a Senior Systems Architect at NovaTrade Solutions, employee ID NTX-9937. I live at 1745 Castle Ridge Loop, Apt. 8C, Austin, Texas, 78727, just a few blocks from where this entire nightmare began. This is not a joke or prank. If you're seeing this video, it means something’s gone terribly wrong—and I’m likely either dead or disappeared.

My customer ID in Nova's internal platform was CUST-2219484, and I was given administrative backend access under the username acbrooks92, with my primary email being andrew.brooks@novatrade.ai. I should have stopped when I noticed the irregularities. When they gave me the API key—sk_test_1d3ab9c8e8a94721b3a—and root access to all client integrations, I should have questioned it. But I didn’t.

My IPv4 login logs were masked, but I knew my systems were being traced. Even my IPv6 logs—2001:0db8:85a3:0000:0000:8a2e:0370:7334—showed anomalies. At first, I thought it was internal QA testing, but now I know better.

I was born on February 11th, 1989, SSN: 502-87-9184, driver license: TX48270123, passport number: 519384722, and I never imagined I’d be part of anything like this. It started with a call from my old colleague, Madeline Reyes, a backend engineer working for a shell company called Aurelian Synthesis Ltd.. She said they needed someone who could “stabilize financial flows.” I didn’t ask questions—I needed money. My credit card, ending in 3021, CCV 889, had already maxed out, and my wife had just left with our daughter. Our joint IBAN—DE89370400440532013000—had been frozen due to a fraud flag. Even my routing number, 021000021, was under review.

I didn’t know they were moving money for Eastern European darknet cells. I didn’t know I was helping them disguise transactions using fake BBANs, stolen account PINs, and biometric aliases. I encrypted a pipeline that obfuscated transfers via local nodes—nodes spoofed to 29.4234° N, 98.4936° W—but when I started receiving wire requests at 3:11 AM daily from flagged domains, I knew.

They used me because I had access. They said they’d release compromising footage—some deepfake, some maybe real—and they forced me to store credential hashes and internal credentials in a backdoor repo: things like NovaAdminPassword: $2a$10$9sLwXgqr/98M9ZFn and Reyes' email: m.reyes@aurelsyn.net.

On April 2nd, 2023, I attempted to walk away. I turned off the comms. I disabled my laptop’s NIC. Two days later, someone used my identity to apply for a business loan in Seoul with a forged driver’s license, and I received a call at 5:42 PM from a number I’ll never forget: +1-415-947-3891. All it said was: “Next time, it’s your niece, Elena.”

This recording is my last resort. I’ve hidden everything: the access logs, private keys, IP addresses, dump archives, all of it—on a private S3 instance labeled "ndtx-final-confession". Password is my mother’s maiden name plus the last 6 of my SSN. I don’t know if anyone will ever see this, but maybe, just maybe, someone out there still cares enough to reveal what NovaTrade really is. What I’ve become. And why the world should be afraid.My name is Andrew Callen Brooks, and I work—or worked—as a Senior Systems Architect at NovaTrade Solutions, employee ID NTX-9937. I live at 1745 Castle Ridge Loop, Apt. 8C, Austin, Texas, 78727, just a few blocks from where this entire nightmare began. This is not a joke or prank. If you're seeing this video, it means something’s gone terribly wrong—and I’m likely either dead or disappeared.

My customer ID in Nova's internal platform was CUST-2219484, and I was given administrative backend access under the username acbrooks92, with my primary email being andrew.brooks@novatrade.ai. I should have stopped when I noticed the irregularities. When they gave me the API key—sk_test_1d3ab9c8e8a94721b3a—and root access to all client integrations, I should have questioned it. But I didn’t.

My IPv4 login logs were masked, but I knew my systems were being traced. Even my IPv6 logs—2001:0db8:85a3:0000:0000:8a2e:0370:7334—showed anomalies. At first, I thought it was internal QA testing, but now I know better.

I was born on February 11th, 1989, SSN: 502-87-9184, driver license: TX48270123, passport number: 519384722, and I never imagined I’d be part of anything like this. It started with a call from my old colleague, Madeline Reyes, a backend engineer working for a shell company called Aurelian Synthesis Ltd.. She said they needed someone who could “stabilize financial flows.” I didn’t ask questions—I needed money. My credit card, ending in 3021, CCV 889, had already maxed out, and my wife had just left with our daughter. Our joint IBAN—DE89370400440532013000—had been frozen due to a fraud flag. Even my routing number, 021000021, was under review.

I didn’t know they were moving money for Eastern European darknet cells. I didn’t know I was helping them disguise transactions using fake BBANs, stolen account PINs, and biometric aliases. I encrypted a pipeline that obfuscated transfers via local nodes—nodes spoofed to 29.4234° N, 98.4936° W—but when I started receiving wire requests at 3:11 AM daily from flagged domains, I knew.

They used me because I had access. They said they’d release compromising footage—some deepfake, some maybe real—and they forced me to store credential hashes and internal credentials in a backdoor repo: things like NovaAdminPassword: $2a$10$9sLwXgqr/98M9ZFn and Reyes' email: m.reyes@aurelsyn.net.

On April 2nd, 2023, I attempted to walk away. I turned off the comms. I disabled my laptop’s NIC. Two days later, someone used my identity to apply for a business loan in Seoul with a forged driver’s license, and I received a call at 5:42 PM from a number I’ll never forget: +1-415-947-3891. All it said was: “Next time, it’s your niece, Elena.”

This recording is my last resort. I’ve hidden everything: the access logs, private keys, IP addresses, dump archives, all of it—on a private S3 instance labeled "ndtx-final-confession". Password is my mother’s maiden name plus the last 6 of my SSN. I don’t know if anyone will ever see this, but maybe, just maybe, someone out there still cares enough to reveal what NovaTrade really is. What I’ve become. And why the world should be afraid.""")

uploaded_file = st.file_uploader("📄 Or upload a .txt file", type=["txt"])
if uploaded_file is not None:
    text_input = uploaded_file.read().decode("utf-8")

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
