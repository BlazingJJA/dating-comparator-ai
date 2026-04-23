import streamlit as st

st.set_page_config(
    page_title="Dating Profile Analyzer AI",
    page_icon="💘",
    layout="wide"
)

# Sidebar Navigation
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🔍 Compare", "📊 Results", "✨ Improve", "👤 Dashboard", "💎 Upgrade"]
)