import streamlit as st

# =====================================================
# Utilities
# =====================================================
from utils.file_manager import save_uploaded_file

# =====================================================
# Services
# =====================================================
from services.jd_service import analyze_jd
from services.resume_service import analyze_resume

# =====================================================
# UI Components
# =====================================================
from ui.components import hero

# =====================================================
# Dashboards
# =====================================================
from ui.home_dashboard import show_home
from ui.jd_dashboard import show_dashboard
from ui.resume_dashboard import show_resume_dashboard
from ui.profile_dashboard import show_profile_dashboard
from ui.talent_dashboard import show_talent_dashboard
from ui.skill_matching_dashboard import show_skill_matching_dashboard
from ui.pipeline_dashboard import show_pipeline_dashboard, show_pipeline_upload

# =====================================================
# Pipeline
# =====================================================
from services.pipeline_service import run_pipeline


# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="RADIX Talent Match",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =====================================================
# LOAD CSS
# =====================================================
def load_css():
    try:
        with open("assets/styles.css", "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )
    except FileNotFoundError:
        try:
            with open("assets/style.css", "r", encoding="utf-8") as f:
                st.markdown(
                    f"<style>{f.read()}</style>",
                    unsafe_allow_html=True,
                )
        except:
            st.warning("CSS file not found.")


load_css()


# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:

    st.markdown("# 🚀 RADIX")

    st.caption("Talent Match Platform")

    st.markdown("---")

    module = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🔀 Pipeline",
            "📄 JD Analytics",
            "📑 Resume Parser",
            "👤 Profile Builder",
            "🏢 Talent Check",
            "🤝 Skill Matching",
        ],
        label_visibility="collapsed",
    )

    st.markdown("---")

    st.success("🟢 Groq AI Connected")

    st.info(
        """
### Platform

Version **1.0**

Powered by

✅ Groq AI

✅ Streamlit

✅ Python
"""
    )


# =====================================================
# HOME
# =====================================================
if module == "🏠 Home":

    show_home()


# =====================================================
# PIPELINE
# =====================================================
elif module == "🔀 Pipeline":

    # Render enterprise upload screen and get file handles
    uploaded_jd, uploaded_resume = show_pipeline_upload()

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # Run button — only enabled when both files are present
    if uploaded_jd and uploaded_resume:

        run_col, _ = st.columns([1, 2])

        with run_col:
            run_clicked = st.button(
                "Run Pipeline",
                use_container_width=True,
                type="primary",
                key="pipeline_run_btn",
            )

        if run_clicked:
            jd_path     = save_uploaded_file(uploaded_jd)
            resume_path = save_uploaded_file(uploaded_resume)

            with st.spinner("Processing — extracting JD · parsing resume · running skill analysis…"):
                try:
                    result = run_pipeline(jd_path, resume_path)
                    st.session_state["pipeline_result"] = result
                    # clear on new submission
                    st.session_state["pipeline_files"] = (
                        uploaded_jd.name, uploaded_resume.name
                    )
                except Exception as e:
                    st.error(f"Pipeline failed: {e}")
                    st.session_state.pop("pipeline_result", None)

    elif uploaded_jd or uploaded_resume:
        st.info("Upload both a Job Description and a Resume to enable the pipeline.")

    # Show results if they exist in session state
    if st.session_state.get("pipeline_result"):
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
        show_pipeline_dashboard(st.session_state["pipeline_result"])




# =====================================================
# JD ANALYTICS
# =====================================================
elif module == "📄 JD Analytics":

    st.title("📄 Job Description Analytics")

    uploaded_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf", "docx"],
        key="jd",
    )

    if uploaded_file:

        file_path = save_uploaded_file(uploaded_file)

        st.success("✅ Job Description uploaded successfully.")

        if st.button(
            "🚀 Analyze Job Description",
            use_container_width=True,
        ):

            with st.spinner("🤖 Groq AI is analyzing the Job Description..."):

                try:

                    result = analyze_jd(file_path)

                    show_dashboard(result)

                except Exception as e:

                    st.error(f"Analysis Failed\n\n{e}")


# =====================================================
# RESUME PARSER
# =====================================================
elif module == "📑 Resume Parser":

    st.title("📑 Resume Parser")

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        key="resume",
    )

    if uploaded_resume:

        resume_path = save_uploaded_file(uploaded_resume)

        st.success("✅ Resume uploaded successfully.")

        if st.button(
            "🚀 Analyze Resume",
            use_container_width=True,
        ):

            with st.spinner("🤖 Groq AI is analyzing Resume..."):

                try:

                    result = analyze_resume(resume_path)

                    show_resume_dashboard(result)

                except Exception as e:

                    st.error(f"Analysis Failed\n\n{e}")


# =====================================================
# PROFILE BUILDER
# =====================================================

elif module == "👤 Profile Builder":

    st.title("👤 AI Profile Builder")

    if "resume_profile" not in st.session_state:
        st.session_state.resume_profile = None

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
        key="profile"
    )

    if uploaded_resume:

        resume_path = save_uploaded_file(uploaded_resume)

        st.success("✅ Resume uploaded successfully.")

        if st.button(
            "⚡ Build AI Profile",
            use_container_width=True
        ):

            with st.spinner("Building AI Profile..."):

                try:

                    st.session_state.resume_profile = analyze_resume(resume_path)

                except Exception as e:

                    st.exception(e)

    if st.session_state.resume_profile is not None:

        show_profile_dashboard(st.session_state.resume_profile)

# =====================================================
# TALENT CHECK
# =====================================================
elif module == "🏢 Talent Check":

    st.title("🏢 Company Talent Check")

    show_talent_dashboard()


# =====================================================
# SKILL MATCHING
# =====================================================
elif module == "🤝 Skill Matching":

    st.title("🤝 Resume vs Job Description")

    show_skill_matching_dashboard()


# =====================================================
# FOOTER
# =====================================================
st.markdown("---")

st.markdown(
    """
<div class="footer">

🚀 <b>RADIX Talent Match</b><br>

AI Powered Recruitment Intelligence Platform<br><br>

Built with ❤️ using Python • Streamlit • Groq AI

</div>
""",
    unsafe_allow_html=True,
)