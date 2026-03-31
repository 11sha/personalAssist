
import streamlit as st
import json
from pathlib import Path

# ----------------------------
# Persistence (simple + safe)
# ----------------------------
DATA_FILE = Path("players_data.json")

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"num_players": 4, "players": []}

def save_data(num_players, players):
    with open(DATA_FILE, "w") as f:
        json.dump(
            {"num_players": num_players, "players": players},
            f,
            indent=2
        )

data = load_data()

# ----------------------------
# Page layout
# ----------------------------
st.set_page_config(page_title="TITLE", layout="centered")

st.title("TITLE")
st.subheader("sub heading")

st.write(
    "This is a short text section. "
    "It can explain the game, rules, or purpose of the app."
)

st.divider()

# ----------------------------
# Number of players selector
# ----------------------------
st.subheader("NUMBER OF PLAYERS")

if "num_players" not in st.session_state:
    st.session_state.num_players = data["num_players"]

col_minus, col_num, col_plus = st.columns([1, 2, 1])

with col_minus:
    if st.button("➖"):
        st.session_state.num_players = max(1, st.session_state.num_players - 1)

with col_num:
    st.markdown(
        f"<h1 style='text-align:center'>{st.session_state.num_players}</h1>",
        unsafe_allow_html=True
    )

with col_plus:
    if st.button("➕"):
        st.session_state.num_players += 1

st.divider()

# ----------------------------
# Player name inputs
# ----------------------------
st.subheader("PLAYER NAMES")

players = []
existing_players = data.get("players", [])

for i in range(st.session_state.num_players):
    default_name = (
        existing_players[i]
        if i < len(existing_players)
        else f"Player {i + 1}"
    )

    name = st.text_input(
        label=f"Player {i + 1} Name",
        value=default_name,
        key=f"player_{i}"
    )
    players.append(name)

# ----------------------------
# Save state
# ----------------------------
save_data(st.session_state.num_players, players)

st.success("✅ Player count and names saved")
