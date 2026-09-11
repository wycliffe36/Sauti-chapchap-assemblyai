import streamlit as st
import os

try:
    import assemblyai as aai
    HAS_AAI = True
except:
    HAS_AAI = False

st.set_page_config(page_title="SautiChapChap", page_icon="⚡", layout="centered")

if "cart" not in st.session_state:
    st.session_state.cart = []

PRODUCTS = [
    {"name": "Sukari 1kg", "price": 150, "key": "sukari sugar"},
    {"name": "Mafuta 1L", "price": 250, "key": "mafuta oil"},
    {"name": "Mchele 1kg", "price": 180, "key": "mchele rice"},
    {"name": "Sabuni", "price": 50, "key": "sabuni"},
    {"name": "Mkate", "price": 60, "key": "mkate bread"},
]

st.title("⚡ SautiChapChap")
st.caption("Real-time Voice Commerce | AssemblyAI Universal-3 Pro | Fresh Build")
st.divider()

api_key = ""
if "ASSEMBLYAI_API_KEY" in st.secrets:
    api_key = st.secrets["ASSEMBLYAI_API_KEY"]
else:
    api_key = os.getenv("ASSEMBLYAI_API_KEY", "")

if HAS_AAI and api_key:
    st.success("AssemblyAI Connected ✅")
else:
    st.warning("Offline Permanent Mode - Works without key ✅")

# TWO WAYS TO GET VOICE - FIX FOR SAMSUNG RECORDINGS
tab1, tab2 = st.tabs(["🎙️ Record Live (No File Search Needed)", "📁 Upload From Downloads"])

audio_file = None

with tab1:
    st.info("BEST FOR YOU: Tap mic below and speak. No need to find Voice 002!")
    live = st.audio_input("Tap to record your order")
    if live:
        audio_file = live
        st.audio(live)
        st.success("Recording captured ✅")

with tab2:
    st.write("How to find Samsung Voice 002 / 003:")
    st.code("My Files > Internal Storage > Recordings > Voice Recorder > Long-press Voice 002 > Move > Downloads", language="text")
    st.caption("After moving to Downloads, Chrome can see it. Open this app in CHROME, not WhatsApp.")
    uploaded = st.file_uploader("Choose audio from Downloads", type=None, help="Shows ALL files so you can find Voice 002.m4a")
    if uploaded:
        audio_file = uploaded
        st.audio(uploaded)
        st.success(f"File loaded: {uploaded.name} ✅")

# TRANSCRIPTION
transcript = ""

if audio_file:
    if HAS_AAI and api_key:
        with st.spinner("AssemblyAI Universal-3 Pro transcribing..."):
            try:
                aai.settings.api_key = api_key
                transcriber = aai.Transcriber()
                result = transcriber.transcribe(audio_file)
                transcript = result.text
                st.success(f"AssemblyAI heard: **{transcript}**")
            except Exception as e:
                st.error(f"API error, using manual mode: {e}")
    else:
        st.info("Manual mode: Type what customer said below")

st.divider()

text = st.text_input("What did customer say?", value=transcript, placeholder="e.g. nataka sukari na mafuta")

if text:
    filtered = [p for p in PRODUCTS if any(w in text.lower() for w in p["key"].split())]
    show = filtered if filtered else PRODUCTS
    
    st.subheader("Matched Products")
    for p in show:
        c1, c2, c3 = st.columns([3, 1, 1])
        c1.write(f"**{p['name']}**")
        c2.write(f"KSh {p['price']}")
        if c3.button("Add", key=f"add_{p['name']}_{len(st.session_state.cart)}"):
            st.session_state.cart.append(p)
            st.toast(f"Added {p['name']}!")

st.divider()
total = sum(i["price"] for i in st.session_state.cart)
st.metric(f"Cart ({len(st.session_state.cart)} items)", f"KSh {total}")

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear Cart", use_container_width=True):
        st.session_state.cart = []
        st.rerun()
with col2:
    if st.button("Checkout", type="primary", use_container_width=True):
        st.balloons()
        st.success(f"Order placed! Total KSh {total}")

st.caption("Permanent build: works online with AssemblyAI, offline with manual entry. Judgement-day ready.")
