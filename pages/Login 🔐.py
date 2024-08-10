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

users = {
    "sanidhya" : "owner@999",
    "user1" : "password1",
    "user2" : "password2",
    "admin" : "password"
}

cnt = 3

st.title("Login Page")
username = st.text_input("Enter Username", max_chars=10)
password = st.text_input("Enter Password", max_chars=10, type='password')
submit_button = st.button("Login")

if submit_button:
    if username in users and users[username] == password:
        st.success("Logged In!")
    elif username in users and users[username] != password:
        st.error("Incorrect Password!")
        cnt -= 1
    elif cnt == 0:
        st.error("Account Locked!")
        st.error("No Attempts Remaining!")
        st.error("Try Again After Sometime!")
    else:
        st.error("User Not Found!")
        cnt -= 1
        st.write("Remaining Attempt : ", cnt)