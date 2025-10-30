import streamlit as st
from transcribe import transcribe_audio
from summarize import summarize_text

st.title("🧠 Transcripteur & Résumeur vocal IA")

uploaded_file = st.file_uploader("Dépose ton fichier audio", type=["wav", "mp3", "m4a"])

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())
    status_placeholder = st.empty()  # crée un conteneur vide
    status_placeholder.info("⏳ Transcription en cours...")
    transcribiption = transcribe_audio("temp.wav")
    status_placeholder.empty()  # efface le message une fois fini
    st.success("✅ Transcription terminée !")
    st.text_area("Transcription", transcribiption, height=200)
    
if st.button("Générer un résumé"):
    status_placeholder.info("⏳ Résumé en cours...")
    status_placeholder.empty()
    summary = summarize_text(transcribiption)
    st.text_area("Résumé", summary, height=70)
