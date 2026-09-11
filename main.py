import streamlit as st
import os

try:
    import assemblyai as aai
    HAS_AAI = True
except:
    HAS_AAI = False

st.set_page_config(page_title="SautiChapChap", page_icon="⚡", layout="centered")
if "cart" not in st.session_state: st.session_state.cart=[]

PRODUCTS=[
    {"name":"Sukari 1kg","price":150,"key":"sukari sugar"},
    {"name":"Mafuta 1L","price":250,"key":"mafuta oil"},
    {"name":"Mchele 1kg","price":180,"key":"mchele rice"},
    {"name":"Sabuni","price":50,"key":"sabuni"},
    {"name":"Mkate","price":60,"key":"mkate bread"}
]

st.title("⚡ SautiChapChap")
st.caption("Real-time Voice Commerce | AssemblyAI Universal-3 Pro")

api_key = st.secrets.get("ASSEMBLYAI_API_KEY","") if "ASSEMBLYAI_API_KEY" in st.secrets else os.getenv("ASSEMBLYAI_API_KEY","")

# NEW FIX: 2 TABS TO FIND RECORDINGS
tab1, tab2 = st.tabs(["🎙️ Record Live (Easiest)", "📁 Upload File"])

audio_file = None

with tab1:
    st.info("Tap the mic below and say 'nataka sukari' - no need to find files!")
    live = st.audio_input("Record your order")
    if live:
        audio_file = live
        st.audio(live)

with tab2:
    st.write("Where are Samsung recordings?")
    st.caption("My Files > Internal Storage > Recordings > Voice Recorder > Voice 002.m4a")
    st.caption("Or: Audio > Recordings")
    uploaded = st.file_uploader("Select recording", type=["m4a","mp3","wav","webm","ogg","m4a"], label_visibility="collapsed")
    if uploaded:
        audio_file = uploaded
        st.audio(uploaded)
        st.success(f"File: {uploaded.name} ✅")

transcript = ""
if audio_file and HAS_AAI and api_key:
    with st.spinner("AssemblyAI listening..."):
        try:
            aai.settings.api_key = api_key
            transcriber = aai.Transcriber()
            result = transcriber.transcribe(audio_file)
            transcript = result.text
            st.success(f"AssemblyAI heard: {transcript}")
        except Exception as e:
            st.warning(f"Using offline mode: {e}")

text = st.text_input("What did customer say?", value=transcript, placeholder="nataka sukari na mafuta")

if text:
    filtered = [p for p in PRODUCTS if any(w in text.lower() for w in p["key"].split())]
    show = filtered if filtered else PRODUCTS
    for p in show:
        c1,c2,c3 = st.columns([3,1,1])
        c1.write(f"**{p['name']}**"); c2.write(f"KSh {p['price']}")
        if c3.button("Add", key=p["name"]+text[:3]):
            st.session_state.cart.append(p)
            st.toast(f"Added {p['name']}!")

st.divider()
total = sum(i["price"] for i in st.session_state.cart)
st.metric(f"Cart ({len(st.session_state.cart)} items)", f"KSh {total}")
if st.button("Clear Cart"): 
    st.session_state.cart=[]; st.rerun()
