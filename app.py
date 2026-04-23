import streamlit as st
import random

st.set_page_config(page_title="Dating Comparator AI", layout="wide")

# ---------- SESSION MEMORY ----------
if "score_a" not in st.session_state:
    st.session_state.score_a = 0
if "score_b" not in st.session_state:
    st.session_state.score_b = 0
if "comparisons" not in st.session_state:
    st.session_state.comparisons = 0

# ---------- FAKE PROFILE DATA ----------
names = ["Emma", "Sophie", "Lily", "Ava", "Mia", "Zoe"]
bios = [
    "Coffee lover ☕ | Hiking addict ⛰️",
    "Dog mom 🐶 | Gym & health 💪",
    "Travel addict ✈️ | Sushi lover 🍣",
    "Artist 🎨 | Deep conversations 🧠",
    "Beach days 🌊 | Wine nights 🍷",
]

profile_a = {
    "name": random.choice(names),
    "bio": random.choice(bios),
    "image": "https://picsum.photos/400/500?random=1"
}

profile_b = {
    "name": random.choice(names),
    "bio": random.choice(bios),
    "image": "https://picsum.photos/400/500?random=2"
}

# ---------- UI ----------
st.title("🔥 Dating Comparator AI")
st.write("The app learns your taste by your choices")

col1, col2 = st.columns(2)

# ---------- BUTTON FUNCTIONS ----------
def choose_a():
    st.session_state.score_a += 1
    st.session_state.comparisons += 1

def choose_b():
    st.session_state.score_b += 1
    st.session_state.comparisons += 1

# ---------- PROFILE A ----------
with col1:
    st.header("Profile A")
    st.image(profile_a["image"])
    st.subheader(profile_a["name"])
    st.write(profile_a["bio"])
    st.button("💚 Choose A", on_click=choose_a)

# ---------- PROFILE B ----------
with col2:
    st.header("Profile B")
    st.image(profile_b["image"])
    st.subheader(profile_b["name"])
    st.write(profile_b["bio"])
    st.button("💚 Choose B", on_click=choose_b)

# ---------- STATS ----------
st.divider()
st.subheader("🧠 Learning stats")

st.write("Comparisons made:", st.session_state.comparisons)
st.write("Votes for A:", st.session_state.score_a)
st.write("Votes for B:", st.session_state.score_b)
