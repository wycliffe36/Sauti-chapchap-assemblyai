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
st.caption("Real-time Voice Commerce | AssemblyAI Universal-3 Pro | Hackathon Fresh")

api_key = st.secrets.get("ASSEMBLYAI_API_KEY","") if "ASSEMBLYAI_API_KEY" in st.secrets else os.getenv("ASSEMBLYAI_API_KEY","")

uploaded = st.file_uploader("Upload Voice 002 / Voice 003.m4a", type=["m4a","mp3","wav","webm"])
transcript = ""

if uploaded:
    st.audio(uploaded)
    st.success(f"File received: {uploaded.name} ✅")
    if HAS_AAI and api_key:
        with st.spinner("AssemblyAI Realtime transcribing..."):
            try:
                aai.settings.api_key = api_key
                transcriber = aai.Transcriber()
                result = transcriber.transcribe(uploaded)
                transcript = result.text
                st.success(f"AssemblyAI heard: {transcript}")
            except Exception as e:
                st.warning(f"Fallback mode: {e}")
    else:
        st.info("Permanent fallback mode - no API key needed")

text = st.text_input("What did customer say?", value=transcript, placeholder="nataka sukari")
if text:
    filtered = [p for p in PRODUCTS if any(w in text.lower() for w in p["key"].split())]
    show = filtered if filtered else PRODUCTS
    for p in show:
        c1,c2,c3 = st.columns([3,1,1])
        c1.write(f"**{p['name']}**"); c2.write(f"KSh {p['price']}")
        if c3.button("Add", key=p["name"]):
            st.session_state.cart.append(p)
            st.toast("Added!")

st.divider()
total = sum(i["price"] for i in st.session_state.cart)
st.metric(f"Cart ({len(st.session_state.cart)} items)", f"KSh {total}")
if st.button("Clear"):
    st.session_state.cart=[]; st.rerun()
