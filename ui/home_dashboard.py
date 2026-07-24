import streamlit as st
from ui.components import hero
from ui.components import metric_card
from ui.components import section


def _inject_home_css():
    st.markdown(
        """
        <style>
        /* ---------- Global fade/slide-in for the whole page body ---------- */
        @keyframes fadeInUp {
            0%   { opacity: 0; transform: translateY(16px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes shimmer {
            0%   { background-position: -400px 0; }
            100% { background-position: 400px 0; }
        }

        /* Stagger animation for the main vertical blocks (hero, sections, rows) */
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stVerticalBlock"] > div.element-container {
            animation: fadeInUp 0.6s ease both;
        }

        /* ---------- Markdown intro text ---------- */
        div[data-testid="stMarkdownContainer"] h3 {
            background: linear-gradient(90deg, #6C5CE7, #00C2A8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: 0.3px;
        }

        /* ---------- Metric cards / info / success boxes (stAlert) ---------- */
        div[data-testid="stAlertContainer"],
        div[data-testid="stAlert"] {
            border-radius: 14px !important;
            padding: 16px 18px !important;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.06);
            animation: fadeInUp 0.5s ease both;
            border: 1px solid rgba(0,0,0,0.05);
        }
        div[data-testid="stAlertContainer"]:hover,
        div[data-testid="stAlert"]:hover {
            transform: translateY(-6px) scale(1.015);
            box-shadow: 0 12px 24px rgba(0,0,0,0.12);
        }

        /* Success = workflow steps: make them equal height, centered, pill-like */
        div[data-testid="column"] div[data-testid="stAlertContainer"]:has(svg[data-baseweb="icon"]) {
            text-align: center;
        }

        /* Column gap tightened + equal spacing for responsiveness */
        div[data-testid="stHorizontalBlock"] {
            gap: 1rem;
            flex-wrap: wrap !important;
        }
        div[data-testid="column"] {
            display: flex;
            flex-direction: column;
            justify-content: stretch;
            min-width: 150px;
        }
        div[data-testid="column"] > div {
            flex: 1;
        }

        /* Give each column a slight, staggered entrance delay for a "cascade" feel */
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) { animation: fadeInUp 0.45s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(2) { animation: fadeInUp 0.55s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(3) { animation: fadeInUp 0.65s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) { animation: fadeInUp 0.75s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(5) { animation: fadeInUp 0.85s ease both; }

        /* ---------- Section headers ---------- */
        h2, h3.section-title {
            position: relative;
            padding-bottom: 6px;
        }

        /* ---------- Responsive tweaks for small screens ---------- */
        @media (max-width: 768px) {
            div[data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
            }
            div[data-testid="column"] {
                width: 100% !important;
                min-width: 100% !important;
            }
            div[data-testid="stAlertContainer"],
            div[data-testid="stAlert"] {
                margin-bottom: 10px !important;
            }
        }

        /* Smooth scroll + subtle page fade-in */
        html {
            scroll-behavior: smooth;
        }
        section.main > div {
            animation: fadeInUp 0.4s ease-in-out both;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_home():
    _inject_home_css()

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
    col1, col2, col3, col4 = st.columns(4)
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
            "1",
            "🚀"
        )
    st.write("")
    section("Platform Workflow")
    c1, c2, c3, c4, c5 = st.columns(5)
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
    a, b = st.columns(2)
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
