import streamlit as st

from services.skill_matching_service import compare_with_jd

from utils.file_utils import save_uploaded_file


def show_skill_matching_dashboard():

    st.header("🤝 Skill Matching")

    uploaded = st.file_uploader(

        "Upload Job Description",

        type=["pdf", "docx"]

    )

    if uploaded:

        path = save_uploaded_file(uploaded)

        result = compare_with_jd(path)

        st.metric(

            "Match Score",

            f"{result['score']}%"
        )

        st.progress(result["score"] / 100)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("✅ Matched")

            for s in result["matched"]:

                st.success(s)

        with col2:

            st.subheader("❌ Missing")

            for s in result["missing"]:

                st.error(s)

        st.divider()

        st.subheader("⭐ Extra Skills")

        for s in result["extra"]:

            st.info(s)

        st.divider()

        st.subheader("💡 Recommendation")

        if result["score"] >= 80:

            st.success("Excellent match. Apply!")

        elif result["score"] >= 60:

            st.info("Good match. Improve missing skills.")

        else:

            st.warning("Skill gap is high. Focus on learning before applying.")