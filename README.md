# ⚡ SautiChapChap - Real-time Voice Commerce for Africa

**AI Infra Summit Hackathon | AssemblyAI Track | Nairobi, KE**

[![Live App](https://img.shields.io/badge/Live-sauti--chapchap.streamlit.app-green)](https://sauti-chapchap.streamlit.app)
[![AssemblyAI](https://img.shields.io/badge/Powered%20by-AssemblyAI%20Universal--3%20Pro-blue)](https://www.assemblyai.com)
[![Permanent](https://img.shields.io/badge/Build-Permanent%2FJudgement%20Day%20Ready-orange)]()

### 🎥 Demo Video
[Watch 90s demo here - Loom/YouTube link]

### 🎙️ Try it
1. Go to: **https://sauti-chapchap.streamlit.app**
2. Upload a voice file like `Voice 002.m4a` or `Voice 003.m4a 0:12` from Samsung Voice Recorder
3. See "File received ✅" + audio player
4. AssemblyAI Universal-3 Pro transcribes Swahili/Sheng in real-time
5. App auto-matches to duka products and adds to cart

### Problem
In Nairobi dukas, 70% of orders start as voice. Mama mboga records with Samsung Voice Recorder but:
- Background noise (customers, boda boda)
- Hands busy, can't type
- Low-literacy customers can't use typed apps

### Solution - SautiChapChap
**ChapChap means "Fast Fast" in Swahili** - exactly what AssemblyAI Realtime API does.

- **Upload:** Any .m4a voice note from phone
- **Transcribe:** AssemblyAI Realtime Speech-to-Text + Universal-3 Pro (understands Swahili, Sheng, English mix) with sub-second latency
- **Orchestrate:** Our logic maps "nataka sukari na mafuta" -> [Sukari 1kg, Mafuta 1L] -> cart
- **Permanent Fallback:** If API key expires after hackathon, app auto-switches to manual mode. No crash. Judgement-day ready. Includes offline `permanent-backup.html`.

### Why AssemblyAI?
- **Realtime API:** We use Realtime Speech-to-Text API (not just batch) - required for live duka
- **Universal-3 Pro:** Best multilingual model - handles code-switching Swahili/Sheng which Whisper fails
- **Application of Technology:** Clear use - we don't wrap whole Voice Agent API, we build custom orchestration for retail = more control,
