import streamlit as st

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
st.header("Welcome to SpeakEasy!")
st.subheader("Translate text or audio from one language to another with ease!")
st.write("This language translator allows you to translate text or audio from one language to another. Simply type in the text you want to translate, select the source and target languages, and click the 'Translate' button.")
if st.button("Get Started!"):
    st.switch_page("pages/1. Login 🔐.py")
