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
st.title("SpeakEasy")

if "locations" not in st.session_state:
    st.session_state.locations = [
    ("New York", (40.7128, -74.0060)),
    ("Bangalore", (12.9716, 77.5946)),
    ("Los Angeles", (34.0522, -118.2437)),
    ("Mumbai", (19.0760, 72.8777)),
    ("Chicago", (41.8781, -87.6298)),
    ("Delhi", (28.7041, 77.1025)),
    ("Miami", (25.7617, -80.1918))
]


def dispLoc():
    df = pd.DataFrame(st.session_state.locations, columns=["Location", "Coordinates"])
    st.write("### List of Locations and Coordinates")
    st.table(df)


st.write("List of Locations and Coordinates")
if st.button("Show Locations"):
    st.write("Updated List of Locations and Coordinates")
    dispLoc()


st.write("Add a New Location")
newLoc = st.text_input("Location Name")
latitude = st.number_input("Latitude", format="%.6f")
longitude = st.number_input("Longitude", format="%.6f")


if st.button("Add Location"):
    if newLoc:
        st.session_state.locations.append((newLoc, (latitude, longitude)))
        st.success(f"Added location: **{newLoc}** with coordinates ({latitude}, {longitude})")
    else:
        st.warning("Please enter a location name.")
    st.write("Updated Locations")
    dispLoc()


st.write("Remove a Location")
locrmv = st.selectbox("Select Location to Remove", [loc[0] for loc in st.session_state.locations])

if st.button("Remove Location"):
    st.session_state.locations[:] = [loc for loc in st.session_state.locations if loc[0] != locrmv]
    st.success(f"Removed location: **{locrmv}**")
    st.write("Updated Locations")
    dispLoc()