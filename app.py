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

    # 👇 IMPORTANT: define report_mode BEFORE the button
    report_mode = st.selectbox(
        "Select Report Style",
        ["💼 Serious", "😂 Funny", "😈 Brutally Honest"]
    )

    st.divider()

    if st.button("💘 Analyze Compatibility", use_container_width=True):

        if profile_a == "" or profile_b == "":
            st.warning("Please enter both profiles.")
        else:
            st.session_state.profile_a = profile_a
            st.session_state.profile_b = profile_b
            st.session_state.report_mode = report_mode  # now safe
            st.success("Profiles submitted! Go to Results page 👉")

# ---------------- RESULTS PAGE ----------------
elif page == "📊 Results":

    st.title("📊 Compatibility Report")

    if "profile_a" not in st.session_state:
        st.warning("No profiles analyzed yet. Go to Compare page first.")
        st.stop()

    import random

    score = random.randint(35, 97)

    mode = st.session_state.get("report_mode", "💼 Serious")

    st.metric("💘 Compatibility Score", f"{score}%")
    st.divider()

    # ---------------- SERIOUS MODE ----------------
    if "Serious" in mode:

        st.subheader("🔥 Attraction Dynamics")
        st.write("Strong alignment in lifestyle and personality traits.")

        st.subheader("🧠 Personality Match")
        st.write("Complementary communication and shared interests detected.")

        st.subheader("💬 Communication Style")
        st.write("Likely to maintain engaging and emotionally balanced conversations.")

        st.subheader("🏡 Long-term Potential")
        st.write("Values and future goals appear largely compatible.")

        st.subheader("🚩 Risk Signals")
        st.write("Minor lifestyle differences may require compromise.")

    # ---------------- FUNNY MODE ----------------
    elif "Funny" in mode:

        st.subheader("🔥 Attraction Dynamics")
        st.write("You both looked at each other and said: 'Yes. This human will do.'")

        st.subheader("🧠 Personality Match")
        st.write("One of you plans life. The other plans snacks. Together? Balance.")

        st.subheader("💬 Communication Style")
        st.write("From deep talks to terrible memes in 3.5 seconds. Elite range.")

        st.subheader("🏡 Long-term Potential")
        st.write("High probability of hoodie theft and arguing over Netflix.")

        st.subheader("🚩 Risk Signals")
        st.write("Potential conflict over blanket sharing and thermostat control.")

    # ---------------- BRUTALLY HONEST MODE ----------------
    elif "Brutally" in mode:

        st.subheader("🔥 Attraction Dynamics")
        st.write("Strong initial chemistry. Sustainability unclear.")

        st.subheader("🧠 Personality Match")
        st.write("Differences could either create growth or weekly arguments.")

        st.subheader("💬 Communication Style")
        st.write("One overthinks. The other avoids conflict. Proceed carefully.")

        st.subheader("🏡 Long-term Potential")
        st.write("Requires maturity, effort, and realistic expectations.")

        st.subheader("🚩 Risk Signals")
        st.write("Energy mismatch and lifestyle differences detected.")


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
