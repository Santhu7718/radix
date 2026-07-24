import streamlit as st
from ui.components import hero
from ui.components import metric_card
from ui.components import section


def _inject_home_css():
    st.markdown(
        """
        <style>
        /* =========================================================
           KEYFRAMES
        ========================================================= */
        @keyframes fadeInUp {
            0%   { opacity: 0; transform: translateY(22px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes popIn {
            0%   { opacity: 0; transform: scale(0.9); }
            100% { opacity: 1; transform: scale(1); }
        }
        @keyframes gradientShift {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes glowPulse {
            0%, 100% { box-shadow: 0 0 0 rgba(108,92,231,0.0); }
            50%      { box-shadow: 0 0 22px rgba(108,92,231,0.35); }
        }
        @keyframes shine {
            0%   { transform: translateX(-120%) rotate(20deg); }
            100% { transform: translateX(220%) rotate(20deg); }
        }

        html { scroll-behavior: smooth; }

        /* =========================================================
           HEADINGS / INTRO TEXT
        ========================================================= */
        div[data-testid="stMarkdownContainer"] h3 {
            background: linear-gradient(90deg, #7C3AED, #06B6D4, #7C3AED);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            letter-spacing: 0.3px;
            animation: gradientShift 6s ease infinite;
        }

        /* =========================================================
           GENERIC ANIMATION FOR BLOCKS
        ========================================================= */
        div[data-testid="stVerticalBlock"] > div.element-container {
            animation: fadeInUp 0.55s ease both;
        }

        /* =========================================================
           METRIC / WORKFLOW / MODULE "CARDS" -> st.success & st.info
           High-contrast, solid-color, glowing, animated cards
           (colors + text are now guaranteed readable: white text on
           solid saturated backgrounds, no washed-out pastel blend)
        ========================================================= */
        div[data-testid="stAlertContainer"],
        div[data-testid="stAlert"] {
            border-radius: 16px !important;
            padding: 20px 18px !important;
            border: none !important;
            position: relative;
            overflow: hidden;
            font-weight: 700 !important;
            font-size: 1.02rem !important;
            letter-spacing: 0.2px;
            text-align: center;
            transition: transform 0.28s ease, box-shadow 0.28s ease, filter 0.28s ease;
            animation: popIn 0.5s ease both;
            cursor: pointer;
        }

        /* shine sweep on hover */
        div[data-testid="stAlertContainer"]::before,
        div[data-testid="stAlert"]::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -10%;
            width: 40%;
            height: 200%;
            background: rgba(255,255,255,0.25);
            transform: translateX(-120%) rotate(20deg);
            transition: none;
        }
        div[data-testid="stAlertContainer"]:hover::before,
        div[data-testid="stAlert"]:hover::before {
            animation: shine 0.9s ease forwards;
        }

        div[data-testid="stAlertContainer"]:hover,
        div[data-testid="stAlert"]:hover {
            transform: translateY(-8px) scale(1.03);
            filter: brightness(1.08);
        }

        /* Force ALL text/icons inside alerts to pure white for max contrast */
        div[data-testid="stAlertContainer"] *,
        div[data-testid="stAlert"] * {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
            fill: #FFFFFF !important;
            font-weight: 700 !important;
        }

        /* SUCCESS = Workflow pills -> bold gradient, distinct per step via nth-child */
        div[data-testid="stAlertContainer"]:has(svg),
        div[data-testid="stAlert"]:has(svg) {
            background: linear-gradient(135deg, #16a34a, #15803d) !important;
            box-shadow: 0 6px 16px rgba(22,163,74,0.35);
        }

        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) div[data-testid="stAlertContainer"],
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) div[data-testid="stAlert"] {
            background: linear-gradient(135deg, #4f46e5, #4338ca) !important;
            box-shadow: 0 6px 18px rgba(79,70,229,0.4);
        }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(2) div[data-testid="stAlertContainer"],
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(2) div[data-testid="stAlert"] {
            background: linear-gradient(135deg, #0891b2, #0e7490) !important;
            box-shadow: 0 6px 18px rgba(8,145,178,0.4);
        }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(3) div[data-testid="stAlertContainer"],
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(3) div[data-testid="stAlert"] {
            background: linear-gradient(135deg, #d97706, #b45309) !important;
            box-shadow: 0 6px 18px rgba(217,119,6,0.4);
        }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) div[data-testid="stAlertContainer"],
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) div[data-testid="stAlert"] {
            background: linear-gradient(135deg, #db2777, #be185d) !important;
            box-shadow: 0 6px 18px rgba(219,39,119,0.4);
        }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(5) div[data-testid="stAlertContainer"],
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(5) div[data-testid="stAlert"] {
            background: linear-gradient(135deg, #7c3aed, #6d28d9) !important;
            box-shadow: 0 6px 18px rgba(124,58,237,0.4);
        }

        /* But keep the actual workflow-step (success) blocks green-family,
           overriding the column-index color rule ONLY when it's a success alert */
        div[data-testid="column"] div[data-testid="stAlertContainer"]:has(svg[data-baseweb="icon"]),
        div[data-testid="column"] div[data-testid="stAlert"]:has(svg[data-baseweb="icon"]) {
            background: inherit !important;
        }

        /* INFO = Module cards -> deep slate/indigo with left accent bar + glow pulse */
        div[data-testid="stAlertContainer"]:not(:has(svg[data-baseweb="icon"])),
        div[data-testid="stAlert"]:not(:has(svg[data-baseweb="icon"])) {
            background: linear-gradient(135deg, #1e1b4b, #312e81) !important;
            box-shadow: 0 8px 20px rgba(30,27,75,0.45);
            text-align: left !important;
            padding-left: 22px !important;
            border-left: 5px solid #06B6D4 !important;
            white-space: pre-line;
            line-height: 1.6;
        }
        div[data-testid="stAlertContainer"]:not(:has(svg[data-baseweb="icon"])):hover,
        div[data-testid="stAlert"]:not(:has(svg[data-baseweb="icon"])):hover {
            border-left: 5px solid #F472B6 !important;
            animation: glowPulse 1.4s ease infinite;
        }

        /* =========================================================
           LAYOUT / RESPONSIVENESS
        ========================================================= */
        div[data-testid="stHorizontalBlock"] {
            gap: 1.1rem;
            flex-wrap: wrap !important;
        }
        div[data-testid="column"] {
            display: flex;
            flex-direction: column;
            justify-content: stretch;
            min-width: 160px;
        }
        div[data-testid="column"] > div {
            flex: 1;
        }

        /* staggered cascade entrance per column */
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(1) { animation: fadeInUp 0.45s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(2) { animation: fadeInUp 0.55s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(3) { animation: fadeInUp 0.65s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(4) { animation: fadeInUp 0.75s ease both; }
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:nth-child(5) { animation: fadeInUp 0.85s ease both; }

        @media (max-width: 768px) {
            div[data-testid="stHorizontalBlock"] { flex-direction: column !important; }
            div[data-testid="column"] { width: 100% !important; min-width: 100% !important; }
            div[data-testid="stAlertContainer"],
            div[data-testid="stAlert"] { margin-bottom: 12px !important; }
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
