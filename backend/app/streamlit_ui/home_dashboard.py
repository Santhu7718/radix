import streamlit as st

from app.streamlit_ui.components import hero
from app.streamlit_ui.components import metric_card
from app.streamlit_ui.components import section


def show_home():

    hero(
        "🚀 RADIX Talent Match",
        "AI Powered Recruitment Intelligence Platform"
    )

    st.write("")

    section("Welcome")

    st.markdown(
        """
### How ready are you for your next job?

One platform to analyze Job Descriptions,
parse resumes,
build candidate profiles,
perform talent analysis,
and compare candidates with real jobs.

"""
    )

    st.write("")

    col1,col2,col3,col4 = st.columns(4)

    with col1:

        metric_card(
            "Job Modules",
            "5",
            "📄"
        )

    with col2:

        metric_card(
            "Companies",
            "5",
            "🏢"
        )

    with col3:

        metric_card(
            "AI Engine",
            "Groq",
            "🤖"
        )

    with col4:

        metric_card(
            "Version",
            "1.0",
            "🚀"
        )

    st.write("")

    section("Platform Workflow")

    c1,c2,c3,c4,c5 = st.columns(5)

    with c1:
        st.success("① JD")

    with c2:
        st.success("② Resume")

    with c3:
        st.success("③ Profile")

    with c4:
        st.success("④ Talent")

    with c5:
        st.success("⑤ Match")

    st.write("")

    section("Modules")

    a,b = st.columns(2)

    with a:

        st.info("""
📄 JD Analytics

Extract

Skills

ATS

Responsibilities

Education
""")

        st.info("""
👤 Profile Builder

Auto Profile

Editable

Save Profile
""")

        st.info("""
🤝 Skill Matching

Match %

Missing Skills

Recommendation
""")

    with b:

        st.info("""
📑 Resume Parser

Projects

Experience

Education

Certifications
""")

        st.info("""
🏢 Talent Check

Company Analysis

Readiness

Career Advice
""")