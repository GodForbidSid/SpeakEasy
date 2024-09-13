import streamlit as st
import translators as ts
ccss = """
<style>
    .stApp {
        background: linear-gradient(to right, #b721ff, #21d4fd);
        background-size: cover;
        background-repeat: no-repeat;
    }
</style>
"""
st.markdown(ccss, unsafe_allow_html=True)
st.title("SpeakEasy")
st.header("Translate your text with SpeakEasy!")

lang = {
    "English": "en",
    "German": "de",
    "French": "fr",
    "Spanish": "es",
    "Chinese": "zh",
    "Japanese": "ja",
    "Russian": "ru",
    "Italian": "it",
    "Portuguese": "pt"
}

from_language = st.selectbox("Select the source language", list(lang.keys()))
to_language = st.selectbox("Select the target language", list(lang.keys()))
message = st.text_area("Enter the message to be translated:", height=120)
if message:
    translation = ts.translate_text(query_text=message, from_language=lang[from_language], to_language=lang[to_language])
    st.text_area("Translation", translation, height=120)
