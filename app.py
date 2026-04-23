import streamlit as st

st.set_page_config(page_title="Dating Comparator AI", layout="wide")

st.title("🔥 Dating Comparator AI")
st.subheader("Train your personal attraction algorithm")

st.write("Welcome! This app will learn your dating preferences by watching your choices.")

col1, col2 = st.columns(2)

with col1:
    st.header("Profile A")
    st.image("https://picsum.photos/400/500?random=1")
    st.button("Choose A")

with col2:
    st.header("Profile B")
    st.image("https://picsum.photos/400/500?random=2")
    st.button("Choose B")
