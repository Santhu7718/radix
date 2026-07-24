import streamlit as st

def show_dashboard(data):
    st.success("✅ Analysis Complete!")

    # -----------------------------
    # Basic Information
    # -----------------------------
    st.subheader("📌 Job Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"🏢 Company\n\n**{data.get('company', 'N/A')}**")
        st.info(f"💼 Role\n\n**{data.get('role', 'N/A')}**")

    with col2:
        st.info(f"📍 Location\n\n**{data.get('location', 'N/A')}**")
        st.info(f"🎯 Experience\n\n**{data.get('experience', 'N/A')}**")

    st.info(f"📄 Employment Type\n\n**{data.get('employment_type', 'N/A')}**")

    st.divider()

    # -----------------------------
    # Summary
    # -----------------------------
    st.subheader("📝 Job Summary")
    st.write(data.get("summary", "No summary available."))

    st.divider()

    # -----------------------------
    # Required Skills
    # -----------------------------
    st.subheader("🛠 Required Skills")

    skills = data.get("required_skills", [])

    if skills:
        for skill in skills:
            st.markdown(f"- ✅ {skill}")
    else:
        st.write("No required skills found.")

    st.divider()

    # -----------------------------
    # Preferred Skills
    # -----------------------------
    st.subheader("⭐ Preferred Skills")

    preferred = data.get("preferred_skills", [])

    if preferred:
        for skill in preferred:
            st.markdown(f"- ⭐ {skill}")
    else:
        st.write("No preferred skills found.")

    st.divider()

    # -----------------------------
    # Responsibilities
    # -----------------------------
    st.subheader("📋 Responsibilities")

    responsibilities = data.get("responsibilities", [])

    if responsibilities:
        for item in responsibilities:
            st.markdown(f"- {item}")
    else:
        st.write("No responsibilities found.")

    st.divider()

    # -----------------------------
    # ATS
    # -----------------------------
    st.subheader("📈 ATS Analysis")

    ats = data.get("ats", {})

    score = ats.get("score", "N/A")
    difficulty = ats.get("difficulty", "N/A")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Score", score)

    with col2:
        st.metric("Difficulty", difficulty)

    reasons = ats.get("reasons", [])

    if reasons:
        st.write("Reasons:")
        for r in reasons:
            st.markdown(f"- {r}")

    st.divider()

    # -----------------------------
    # Raw JSON
    # -----------------------------
    with st.expander("🔽 View Raw JSON"):
        st.json(data)