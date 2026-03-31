import streamlit as st
import json
from pathlib import Path

DATA_FILE = Path("players_data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"players": []}

data = load_data()
players = data.get("players", [])

# ----------------------------
# Page
# ----------------------------
st.set_page_config(page_title="ROUND 1", layout="centered")

# Underlined title
st.markdown(
    "<h1 style='text-align:center; text-decoration: underline;'>ROUND 1</h1>",
    unsafe_allow_html=True
)

if players:
    st.subheader(", ".join(players))
else:
    st.warning("No players found. Go back and add players.")
