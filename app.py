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
if page == "🏠 Home":

    st.title("💘 Dating Profile Analyzer AI")

    st.markdown("### Find your dating blind spots in 60 seconds")

    st.write(
        "Upload two dating profiles, get AI compatibility insights, "
        "and learn how to attract better matches."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🚀 Start Comparison", use_container_width=True):
            st.session_state.page = "🔍 Compare"

    with col2:
        if st.button("🎯 Try Demo Profiles", use_container_width=True):
            st.session_state.demo_mode = True
            st.session_state.page = "🔍 Compare"

    st.divider()

    st.subheader("How it works")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 1️⃣ Upload Profiles")
        st.write("Paste bios or upload screenshots.")

    with c2:
        st.markdown("### 2️⃣ AI Analysis")
        st.write("We analyze personality & compatibility.")

    with c3:
        st.markdown("### 3️⃣ Get Insights")
        st.write("Receive your dating compatibility report.")
        elif page == "🔍 Compare":

    st.title("🔍 Comparison Lab")

    st.write("Upload two profiles to analyze compatibility.")

    col_left, col_right = st.columns(2)

    # PROFILE A
    with col_left:
        st.subheader("Profile A")

        profile_a = st.text_area(
            "Paste Profile A bio",
            height=250,
            placeholder="Bio, interests, hobbies, lifestyle..."
        )

    # PROFILE B
    with col_right:
        st.subheader("Profile B")

        profile_b = st.text_area(
            "Paste Profile B bio",
            height=250,
            placeholder="Bio, interests, hobbies, lifestyle..."
        )

    st.divider()

    if st.button("💘 Analyze Compatibility", use_container_width=True):

        if profile_a == "" or profile_b == "":
            st.warning("Please enter both profiles.")
        else:
            st.session_state.profile_a = profile_a
            st.session_state.profile_b = profile_b
            st.success("Profiles submitted! Go to Results page 👉")