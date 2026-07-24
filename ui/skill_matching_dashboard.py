import streamlit as st

from services.jd_service import analyze_jd
from services.resume_service import analyze_resume
from services.skill_matching_service import compare_skills
from utils.file_utils import save_uploaded_file


def show_skill_matching_dashboard():

    st.subheader("Upload Documents")

    col_resume, col_jd = st.columns(2, gap="large")

    with col_resume:
        st.markdown("##### Your Resume")
        uploaded_resume = st.file_uploader(
            "Resume",
            type=["pdf", "docx"],
            key="sm_resume",
            label_visibility="collapsed",
            help="Upload your resume (PDF or DOCX)",
        )
        if uploaded_resume:
            st.success(f"✅ {uploaded_resume.name}")

    with col_jd:
        st.markdown("##### Job Description")
        uploaded_jd = st.file_uploader(
            "Job Description",
            type=["pdf", "docx"],
            key="sm_jd",
            label_visibility="collapsed",
            help="Upload the job description (PDF or DOCX)",
        )
        if uploaded_jd:
            st.success(f"✅ {uploaded_jd.name}")

    st.markdown("")

    # ── Only run when both files are present ──────────────────────
    if uploaded_resume and uploaded_jd:

        run_col, _ = st.columns([1, 2])
        with run_col:
            run_clicked = st.button(
                "Analyse Match",
                use_container_width=True,
                type="primary",
                key="sm_run_btn",
            )

        if run_clicked:

            resume_path = save_uploaded_file(uploaded_resume)
            jd_path     = save_uploaded_file(uploaded_jd)

            with st.spinner("Analysing skills — this may take a moment…"):
                try:
                    resume_data = analyze_resume(resume_path)
                    jd_data     = analyze_jd(jd_path)
                    result      = compare_skills(jd_data, resume_data)
                    result["jd"]     = jd_data
                    result["resume"] = resume_data
                    st.session_state["sm_result"] = result
                except Exception as e:
                    st.error(f"Analysis failed: {e}")
                    st.session_state.pop("sm_result", None)

    elif uploaded_resume or uploaded_jd:
        st.info("Upload both your resume and the job description to run the match analysis.")

    # ── Results ────────────────────────────────────────────────────
    if st.session_state.get("sm_result"):
        _render_results(st.session_state["sm_result"])


def _render_results(result: dict):

    score   = result["score"]
    matched = result["matched"]
    missing = result["missing"]
    extra   = result["extra"]
    jd      = result.get("jd", {})
    resume  = result.get("resume", {})

    # Derive display names
    role      = jd.get("role") or "the role"
    candidate = resume.get("name") or "Candidate"

    # Score colour
    if score >= 80:
        bar_color = "#10B981"
        label = "Excellent Match"
        rec   = "Strong alignment. You are a top candidate — apply now."
    elif score >= 60:
        bar_color = "#F59E0B"
        label = "Good Match"
        rec   = "Solid fit. Consider upskilling in the missing areas before applying."
    elif score >= 40:
        bar_color = "#EF4444"
        label = "Moderate Match"
        rec   = "Notable skill gaps. Focus on the missing skills to improve your chances."
    else:
        bar_color = "#DC2626"
        label = "Low Match"
        rec   = "Significant gaps. This role may require skills you have not yet developed."

    st.markdown("---")

    # ── Score row ─────────────────────────────────────────────────
    st.markdown(
        f"""
        <div style="
            display:flex; align-items:center; gap:24px;
            background:#F8FAFC; border:1px solid #E2E8F0;
            border-radius:12px; padding:20px 28px; margin-bottom:20px;
        ">
            <div style="text-align:center; min-width:80px;">
                <div style="font-size:2.4rem; font-weight:800; color:{bar_color}; line-height:1;">
                    {score}%
                </div>
                <div style="font-size:0.72rem; font-weight:700; color:#64748B;
                    text-transform:uppercase; letter-spacing:0.5px; margin-top:2px;">
                    Match Score
                </div>
            </div>
            <div style="flex:1;">
                <div style="font-size:1rem; font-weight:700; color:#0F172A; margin-bottom:6px;">
                    {label} — {candidate} vs. {role}
                </div>
                <div style="background:#E2E8F0; border-radius:99px; height:8px; overflow:hidden;">
                    <div style="width:{score}%; height:100%; background:{bar_color};
                        border-radius:99px; transition:width 0.6s ease;">
                    </div>
                </div>
                <div style="font-size:0.82rem; color:#475569; margin-top:8px;">
                    {len(matched)} matched &nbsp;·&nbsp; {len(missing)} missing &nbsp;·&nbsp;
                    {len(extra)} additional
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Three columns ──────────────────────────────────────────────
    col1, col2, col3 = st.columns(3, gap="medium")

    def _tag(text, bg, fg, border):
        return (
            f'<div style="padding:6px 0; border-bottom:1px solid #F1F5F9;'
            f'font-size:0.83rem; font-weight:600; color:{fg};">{text}</div>'
        )

    def _empty():
        return '<p style="font-size:0.8rem;color:#94A3B8;margin:0;">None</p>'

    def _col_card(title, dot_color, count, items, fg):
        body = "".join(_tag(i, "", fg, "") for i in items) if items else _empty()
        return f"""
        <div style="background:#F8FAFC; border:1px solid #E2E8F0;
            border-radius:10px; padding:16px; height:100%;">
            <div style="display:flex; align-items:center; gap:8px;
                margin-bottom:12px; padding-bottom:10px; border-bottom:1px solid #E2E8F0;">
                <div style="width:8px;height:8px;border-radius:50%;
                    background:{dot_color};flex-shrink:0;"></div>
                <span style="font-size:0.78rem;font-weight:700;
                    text-transform:uppercase;letter-spacing:0.5px;color:{dot_color};">
                    {title}
                </span>
                <span style="margin-left:auto;font-size:0.7rem;font-weight:700;
                    background:#E2E8F0;color:#475569;border-radius:999px;padding:2px 8px;">
                    {count}
                </span>
            </div>
            {body}
        </div>
        """

    with col1:
        st.markdown(
            _col_card("Matched", "#10B981", len(matched), matched, "#065F46"),
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            _col_card("Missing", "#EF4444", len(missing), missing, "#991B1B"),
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            _col_card("Additional", "#F59E0B", len(extra), extra, "#92400E"),
            unsafe_allow_html=True,
        )

    # ── Recommendation banner ──────────────────────────────────────
    if score >= 80:
        rec_bg, rec_border, rec_icon_bg, icon = "#F0FDF4", "#86EFAC", "#DCFCE7", "✓"
    elif score >= 60:
        rec_bg, rec_border, rec_icon_bg, icon = "#FFFBEB", "#FDE68A", "#FEF3C7", "⚡"
    elif score >= 40:
        rec_bg, rec_border, rec_icon_bg, icon = "#FFF7ED", "#FDBA74", "#FFEDD5", "△"
    else:
        rec_bg, rec_border, rec_icon_bg, icon = "#FEF2F2", "#FECACA", "#FEE2E2", "✕"

    st.markdown(
        f"""
        <div style="display:flex; align-items:flex-start; gap:16px;
            background:{rec_bg}; border:1px solid {rec_border};
            border-radius:12px; padding:18px 22px; margin-top:16px;">
            <div style="width:40px;height:40px;border-radius:10px;
                background:{rec_icon_bg};display:flex;align-items:center;
                justify-content:center;font-size:1.1rem;flex-shrink:0;">
                {icon}
            </div>
            <div>
                <div style="font-size:0.9rem;font-weight:700;color:#0F172A;margin-bottom:4px;">
                    Recommendation
                </div>
                <div style="font-size:0.85rem;color:#334155;line-height:1.6;">
                    {rec}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Raw JSON (collapsed) ───────────────────────────────────────
    with st.expander("View Raw JSON", expanded=False):
        t1, t2, t3 = st.tabs(["Match Data", "JD Data", "Resume Data"])
        with t1:
            st.json({"score": score, "matched": matched,
                     "missing": missing, "extra": extra})
        with t2:
            st.json(jd)
        with t3:
            st.json(resume)