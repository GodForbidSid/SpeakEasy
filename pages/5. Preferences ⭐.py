import streamlit as st
import pandas as pd

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


if 'data' not in st.session_state:
    st.session_state.data = {}


def load_data():
    try:
        df = pd.read_csv('pages/travelers.csv')
        if 'TravelerID' in df.columns:
            st.session_state.data = df.set_index('TravelerID').to_dict(orient='index')
        else:
            st.error("The CSV file does not contain a 'TravelerID' column.")
    except Exception as e:
        st.error(f"Error loading data: {e}")


def save_data():
    df = pd.DataFrame.from_dict(st.session_state.data, orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'TravelerID'}, inplace=True)
    df.to_csv('pages/travelers.csv', index=False)

load_data()

st.title("Traveler's Preferences")


st.subheader("Add Traveler")
tid_add = st.text_input("Traveler ID", key="add_tid")
name_add = st.text_input("Name", key="add_name")
destination_add = st.text_input("Destination", key="add_destination")
if st.button("Add Traveler"):
    if tid_add in st.session_state.data:
        st.error(f"Traveler ID {tid_add} already exists!")
    else:
        st.session_state.data[tid_add] = {'Name': name_add, 'Destination': destination_add}
        save_data()
        st.success(f"Traveler {tid_add} added successfully!")


st.subheader("Remove Traveler")
tid_remove = st.text_input("Traveler ID to remove", key="remove_tid")
if st.button("Remove Traveler"):
    if int(tid_remove) in st.session_state.data:
        del st.session_state.data[int(tid_remove)]
        save_data()
        st.success(f"Traveler {tid_remove} removed successfully!")
    else:
        st.error(f"Traveler ID {tid_remove} not found!")


st.subheader("Update Traveler")
tid_update = st.text_input("Traveler ID to update", key="update_tid")
name_update = st.text_input("New Name", key="update_name")
destination_update = st.text_input("New Destination", key="update_destination")
if st.button("Update Traveler"):
    if int(tid_update) in st.session_state.data:
        st.session_state.data[int(tid_update)] = {'Name': name_update, 'Destination': destination_update}
        save_data()
        st.success(f"Traveler {tid_update} updated successfully!")
    else:
        st.error(f"Traveler ID {tid_update} not found!")


st.subheader("Search Traveler")
tid_search = st.text_input("Traveler ID to search", key="search_tid")
if st.button("Search Traveler"):
    if int(tid_search) in st.session_state.data.keys():
        st.write(st.session_state.data[int(tid_search)])
    else:
        st.error(f"Traveler ID {tid_search} not found!")


st.subheader("Current Traveler Data")
st.write(st.session_state.data)