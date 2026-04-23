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

# ---------------- HOME PAGE ----------------
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
        st.button("🚀 Start Comparison", use_container_width=True)

    with col2:
        st.button("🎯 Try Demo Profiles", use_container_width=True)

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


# ---------------- COMPARE PAGE ----------------
elif page == "🔍 Compare":

    st.title("🔍 Comparison Lab")
    st.write("Upload two profiles to analyze compatibility.")

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Profile A")
        profile_a = st.text_area(
            "Paste Profile A bio",
            height=250,
            placeholder="Bio, interests, hobbies, lifestyle..."
        )

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


# ---------------- RESULTS PAGE ----------------
elif page == "📊 Results":

    st.title("📊 Compatibility Report")

    if "profile_a" not in st.session_state:
        st.warning("No profiles analyzed yet. Go to Compare page first.")
        st.stop()

    profile_a = st.session_state.profile_a
    profile_b = st.session_state.profile_b

    import random

    score = random.randint(55, 95)

    st.metric("💘 Compatibility Score", f"{score}%")

    st.divider()

    st.subheader("🔥 Attraction Dynamics")
    st.write("You both show strong lifestyle and personality alignment.")

    st.subheader("🧠 Personality Match")
    st.write("Shared interests and communication style detected.")

    st.subheader("💬 Communication Style")
    st.write("Likely to enjoy engaging conversations and shared humour.")

    st.subheader("🏡 Long-term Potential")
    st.write("Values and goals show promising long-term compatibility.")

    st.subheader("🚩 Risk Signals")
    st.write("Minor lifestyle differences may require compromise.")

    st.divider()

    st.button("✨ Improve My Profile", use_container_width=True)


# ---------------- IMPROVE PAGE ----------------
elif page == "✨ Improve":
    st.title("✨ Profile Improver")
    st.info("Profile optimization coming next step 🔥")


# ---------------- DASHBOARD PAGE ----------------
elif page == "👤 Dashboard":
    st.title("👤 Dashboard")
    st.info("User analytics coming soon 🔥")


# ---------------- UPGRADE PAGE ----------------
elif page == "💎 Upgrade":
    st.title("💎 Upgrade to Pro")
    st.info("Pricing page coming soon 🔥")