import streamlit as st
from app.services.profile_service import save_profile


def show_profile_dashboard(resume):

    st.title("👤 AI Profile Builder")
    st.caption("Review, edit and save your professional profile.")

    # =====================================================
    # PERSONAL INFORMATION
    # =====================================================

    st.markdown("## 👤 Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Full Name",
            value=resume.get("name", "")
        )

        email = st.text_input(
            "Email",
            value=resume.get("email", "")
        )

        phone = st.text_input(
            "Phone",
            value=resume.get("phone", "")
        )

    with col2:

        location = st.text_input(
            "Location",
            value=resume.get("location", "")
        )

        linkedin = st.text_input(
            "LinkedIn",
            value=resume.get("linkedin", "")
        )

        github = st.text_input(
            "GitHub",
            value=resume.get("github", "")
        )

    st.divider()

    # =====================================================
    # SUMMARY
    # =====================================================

    st.markdown("## 📝 Professional Summary")

    summary = st.text_area(
        "",
        value=resume.get("professional_summary", ""),
        height=180,
        placeholder="Write a professional summary..."
    )

    st.divider()

    # =====================================================
    # TECHNICAL SKILLS
    # =====================================================

    st.markdown("## 💻 Technical Skills")

    skills = st.text_area(
        "Skills (comma separated)",
        value=", ".join(
            resume.get("technical_skills", [])
        ),
        height=120
    )

    col1, col2 = st.columns(2)

    with col1:

        programming_languages = st.text_input(
            "Programming Languages",
            value=", ".join(
                resume.get("programming_languages", [])
            )
        )

        frameworks = st.text_input(
            "Frameworks",
            value=", ".join(
                resume.get("frameworks", [])
            )
        )

    with col2:

        databases = st.text_input(
            "Databases",
            value=", ".join(
                resume.get("databases", [])
            )
        )

    st.divider()

    # =====================================================
    # CAREER PREFERENCES
    # =====================================================

    st.markdown("## 🎯 Career Preferences")

    col1, col2, col3 = st.columns(3)

    with col1:

        preferred_role = st.selectbox(
            "Preferred Role",
            [
                "AI Engineer",
                "ML Engineer",
                "Data Scientist",
                "Software Engineer",
                "Full Stack Developer",
                "Backend Developer",
                "Frontend Developer",
            ]
        )

    with col2:

        work_mode = st.selectbox(
            "Preferred Work Mode",
            [
                "Remote",
                "Hybrid",
                "Onsite"
            ]
        )

    with col3:

        expected_salary = st.number_input(
            "Expected Salary (LPA)",
            min_value=0,
            max_value=100,
            value=10
        )

    st.write("")

    # =====================================================
    # SAVE BUTTON
    # =====================================================

    if st.button(
        "💾 Save Professional Profile",
        use_container_width=True
    ):

        profile = {

            "name": name,
            "email": email,
            "phone": phone,
            "location": location,
            "linkedin": linkedin,
            "github": github,

            "professional_summary": summary,

            "technical_skills": [
                s.strip()
                for s in skills.split(",")
                if s.strip()
            ],

            "programming_languages": [
                s.strip()
                for s in programming_languages.split(",")
                if s.strip()
            ],

            "frameworks": [
                s.strip()
                for s in frameworks.split(",")
                if s.strip()
            ],

            "databases": [
                s.strip()
                for s in databases.split(",")
                if s.strip()
            ],

            "preferred_role": preferred_role,
            "work_mode": work_mode,
            "expected_salary": expected_salary,
        }

        save_profile(profile)

        st.success("✅ Profile saved successfully!")

        st.balloons()

        st.info(
            "Your profile is now ready for Talent Check and Skill Matching."
        )