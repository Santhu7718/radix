import streamlit as st


def show_resume_dashboard(data):

    st.success("✅ Resume Parsed Successfully")

    # =====================================================
    # Candidate Information
    # =====================================================

    st.subheader("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("👤 Name", data.get("name", "N/A"))
        st.metric("📧 Email", data.get("email", "N/A"))
        st.metric("📞 Phone", data.get("phone", "N/A"))

    with col2:
        st.metric("📍 Location", data.get("location", "N/A"))

        linkedin = data.get("linkedin", "")
        github = data.get("github", "")

        if linkedin:
            st.markdown(f"**🔗 LinkedIn:** {linkedin}")

        if github:
            st.markdown(f"**💻 GitHub:** {github}")

    st.divider()

    # =====================================================
    # Professional Summary
    # =====================================================

    st.subheader("📝 Professional Summary")

    st.info(data.get("professional_summary", "No summary available."))

    st.divider()

    # =====================================================
    # Technical Skills
    # =====================================================

    st.subheader("🛠 Technical Skills")

    skills = data.get("technical_skills", [])

    if skills:

        cols = st.columns(3)

        for i, skill in enumerate(skills):
            cols[i % 3].success(skill)

    else:
        st.warning("No technical skills found.")

    st.divider()

    # =====================================================
    # Education
    # =====================================================

    st.subheader("🎓 Education")

    education = data.get("education", [])

    if education:

        for edu in education:

            with st.container():

                st.markdown(f"### 🎓 {edu.get('degree', '')}")

                st.write(f"🏫 **Institution:** {edu.get('institution', '')}")

                st.write(f"📅 **Duration:** {edu.get('year', '')}")

                st.divider()

    else:
        st.info("No education details found.")

    # =====================================================
    # Experience
    # =====================================================

    st.subheader("💼 Experience")

    experience = data.get("experience", [])

    if experience:

        for exp in experience:

            with st.expander(
                f"{exp.get('role','')} - {exp.get('company','')}",
                expanded=False
            ):

                st.write(f"**Company:** {exp.get('company','')}")
                st.write(f"**Role:** {exp.get('role','')}")
                st.write(f"**Duration:** {exp.get('duration','')}")
                st.write("**Description:**")
                st.write(exp.get("description",""))

    else:
        st.info("No experience found.")

    st.divider()

    # =====================================================
    # Projects
    # =====================================================

    st.subheader("🚀 Projects")

    projects = data.get("projects", [])

    if projects:

        for project in projects:

            with st.expander(project.get("title","Project")):

                st.write(project.get("description",""))

                tech = project.get("technologies", [])

                if tech:

                    st.write("**Technologies Used:**")

                    tech_cols = st.columns(4)

                    for i, t in enumerate(tech):
                        tech_cols[i % 4].success(t)

    else:
        st.info("No projects found.")

    st.divider()

    # =====================================================
    # Certifications
    # =====================================================

    st.subheader("📜 Certifications")

    certs = data.get("certifications", [])

    if certs:

        for cert in certs:
            st.success(f"🏅 {cert}")

    else:
        st.info("No certifications found.")

    st.divider()

    # =====================================================
    # ATS Analysis
    # =====================================================

    st.subheader("📊 ATS Analysis")

    ats = data.get("ats", {})

    score = ats.get("score", 0)

    st.metric("ATS Score", f"{score}/100")

    st.progress(score / 100)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### ✅ Strengths")

        strengths = ats.get("strengths", [])

        if strengths:

            for item in strengths:
                st.success(item)

        else:
            st.write("No strengths available.")

    with col2:

        st.markdown("### ⚠ Weaknesses")

        weaknesses = ats.get("weaknesses", [])

        if weaknesses:

            for item in weaknesses:
                st.warning(item)

        else:
            st.write("No weaknesses available.")

    missing = ats.get("missing_sections", [])

    if missing:

        st.markdown("### ❌ Missing Sections")

        for item in missing:
            st.error(item)

    st.divider()

    # =====================================================
    # Raw JSON
    # =====================================================

    with st.expander("🔍 View Raw JSON"):

        st.json(data)