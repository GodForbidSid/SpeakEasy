import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #b721ff, #21d4fd);
        background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)

destinations = {
    "Eiffel Tower": {"landmark", "romantic", "cultural"},
    "Great Wall of China": {"historical", "adventure", "landmark"},
    "Bali Beach": {"beach", "relaxing", "adventure"},
    "Louvre Museum": {"cultural", "art", "museum"},
    "Colosseum": {"historical", "landmark", "cultural"},
    "Machu Picchu": {"historical", "adventure", "landmark"},
    "Santorini": {"beach", "romantic", "relaxing", "scenic"},
    "Mount Fuji": {"adventure", "scenic", "landmark", "nature"},
    "Times Square": {"landmark", "urban", "cultural"},
    "Pyramids of Giza": {"historical", "landmark", "adventure"},
    "Sydney Opera House": {"landmark", "cultural", "urban"},
    "Amazon Rainforest": {"adventure", "nature", "scenic"},
    "Niagara Falls": {"landmark", "scenic", "nature"},
    "Venice Canals": {"romantic", "cultural", "scenic"},
    "Yellowstone National Park": {"adventure", "nature", "scenic"},
    "Disneyland": {"adventure", "family", "fun"},
    "Buckingham Palace": {"landmark", "cultural", "historical"},
    "Grand Canyon": {"adventure", "scenic", "nature"},
    "Sagrada Familia": {"landmark", "cultural", "art"},
    "Tokyo Tower": {"landmark", "urban", "cultural"},
}

all_tags = {
    "landmark", "romantic", "cultural", "historical", "adventure", "beach", 
    "relaxing", "art", "museum", "scenic", "nature", "urban", "family", "fun"
}

st.title("Tag-Based Destination Search")


st.subheader("Select Your Preferences")
user_preferences = st.multiselect("Choose tags:", all_tags)

partial_matches = {}
full_matches = {}

# Partial match: Intersection
st.subheader("Matching Destinations (Partial)")
if user_preferences:
    user_prefs_set = set(user_preferences)
    partial_matches = {d: t for d, t in destinations.items() if t.intersection(user_prefs_set)}
    
    if partial_matches:
        for destination, tags in partial_matches.items():
            st.write(f"**{destination}:** Matches on {', '.join(tags)}")
    else:
        st.write("No partial matches found.")
else:
    st.write("Please select some tags.")

# Full match: Union & Sub-Set
st.subheader("Matching Destinations (Full)")
if user_preferences:
    full_matches = {d: t for d, t in destinations.items() if t.issubset(user_prefs_set)}

    if full_matches:
        for destination, tags in full_matches.items():
            st.write(f"**{destination}:** Full match with {', '.join(tags)}")
    else:
        st.write("No full matches found.")

# Difference
st.subheader("Tags Difference (Selected but Not in Destination)")
if user_preferences:
    for destination, tags in destinations.items():
        difference_tags = user_prefs_set - tags
        if difference_tags:
            st.write(f"**{destination}:** Missing tags compared to your selection: {', '.join(difference_tags)}")
        else:
            st.write(f"**{destination}:** No missing tags, fully or partially matches your selection.")

# Symmetric Difference
st.subheader("Symmetric Difference (Tags not in Both)")
if user_preferences:
    for destination, tags in destinations.items():
        symmetric_diff_tags = user_prefs_set.symmetric_difference(tags)
        if symmetric_diff_tags:
            st.write(f"**{destination}:** Tags that differ: {', '.join(symmetric_diff_tags)}")
        else:
            st.write(f"**{destination}:** No differing tags between your selection and the destination.")

# Summary of all matches
st.subheader("Summary of Matches")
all_matches = set(partial_matches.keys()).union(full_matches.keys())
if all_matches:
    for destination in all_matches:
        st.write(f"- {destination}")
else:
    st.write("No destinations match your preferences.")
