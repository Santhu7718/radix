import streamlit as st

# ─────────────────────────────────────────────────────────────────
# CSS — injected once per page load
# ─────────────────────────────────────────────────────────────────

PIPELINE_CSS = """
<style>
/* ── PIPELINE HEADER BAR ──────────────────────────────────────── */
.pipe-header {
    background: #0F172A;
    border-radius: 14px;
    padding: 28px 36px;
    margin-bottom: 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
}
.pipe-header-left h1 {
    color: #F8FAFC !important;
    font-size: 1.55rem !important;
    font-weight: 700 !important;
    margin: 0 0 4px 0 !important;
    letter-spacing: -0.3px;
}
.pipe-header-left p {
    color: #94A3B8 !important;
    font-size: 0.875rem;
    margin: 0;
}
.pipe-badge {
    background: rgba(99,102,241,0.15);
    border: 1px solid rgba(99,102,241,0.35);
    color: #A5B4FC !important;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    white-space: nowrap;
}

/* ── STEPPER ──────────────────────────────────────────────────── */
.stepper-wrap {
    display: flex;
    align-items: center;
    margin-bottom: 36px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 36px;
    gap: 0;
}
.step-item {
    display: flex;
    align-items: center;
    flex: 1;
    gap: 12px;
}
.step-circle {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    font-weight: 700;
    flex-shrink: 0;
}
.step-circle.done   { background:#10B981; color:white !important; }
.step-circle.active { background:#6366F1; color:white !important; }
.step-circle.idle   { background:#E2E8F0; color:#94A3B8 !important; }
.step-label h4 {
    margin: 0 0 2px 0;
    font-size: 0.85rem;
    font-weight: 700;
    color: #1E293B !important;
}
.step-label p {
    margin: 0;
    font-size: 0.75rem;
    color: #64748B !important;
}
.step-connector {
    flex: 1;
    height: 2px;
    background: #E2E8F0;
    margin: 0 16px;
    position: relative;
}
.step-connector.done {
    background: linear-gradient(90deg,#10B981,#6366F1);
}

/* ── SECTION DIVIDER ──────────────────────────────────────────── */
.section-card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 28px 32px;
    margin-bottom: 24px;
}
.section-title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid #F1F5F9;
}
.section-title-left {
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-number {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    background: #6366F1;
    color: white !important;
    font-size: 0.78rem;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
}
.section-title-left h3 {
    margin: 0;
    font-size: 1rem;
    font-weight: 700;
    color: #0F172A !important;
}
.section-subtitle {
    font-size: 0.78rem;
    color: #94A3B8 !important;
}

/* ── KV GRID ──────────────────────────────────────────────────── */
.kv-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 20px;
}
.kv-grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 20px;
}
.kv-cell {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 14px 16px;
}
.kv-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #64748B !important;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 5px;
}
.kv-value {
    font-size: 0.95rem;
    font-weight: 700;
    color: #0F172A !important;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.kv-value.highlight {
    color: #6366F1 !important;
}

/* ── SUMMARY BOX ──────────────────────────────────────────────── */
.summary-box {
    background: #F8FAFC;
    border-left: 3px solid #6366F1;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    margin-bottom: 18px;
    font-size: 0.875rem;
    color: #334155 !important;
    line-height: 1.65;
}

/* ── SKILL TAGS ───────────────────────────────────────────────── */
.tag-group-label {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    color: #64748B !important;
    margin-bottom: 8px;
    margin-top: 14px;
}
.tags-row {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
    margin-bottom: 4px;
}
.tag {
    display: inline-flex;
    align-items: center;
    border-radius: 6px;
    padding: 4px 11px;
    font-size: 0.78rem;
    font-weight: 600;
    white-space: nowrap;
}
.tag.blue   { background:#EEF2FF; color:#4338CA !important; border:1px solid #C7D2FE; }
.tag.sky    { background:#F0F9FF; color:#0369A1 !important; border:1px solid #BAE6FD; }
.tag.green  { background:#F0FDF4; color:#15803D !important; border:1px solid #86EFAC; }
.tag.red    { background:#FEF2F2; color:#B91C1C !important; border:1px solid #FECACA; }
.tag.amber  { background:#FFFBEB; color:#B45309 !important; border:1px solid #FDE68A; }
.tag.slate  { background:#F1F5F9; color:#475569 !important; border:1px solid #CBD5E1; }

/* ── MATCH SECTION ────────────────────────────────────────────── */
.match-score-block {
    display: flex;
    align-items: center;
    gap: 32px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 24px;
}
.score-donut-wrap {
    position: relative;
    width: 110px;
    height: 110px;
    flex-shrink: 0;
}
.score-donut-wrap svg {
    transform: rotate(-90deg);
}
.score-center-text {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
    pointer-events: none;
}
.score-num {
    font-size: 1.4rem;
    font-weight: 800;
    line-height: 1;
    display: block;
}
.score-pct {
    font-size: 0.7rem;
    font-weight: 600;
    color: #64748B !important;
}
.match-meta {
    flex: 1;
}
.match-meta h2 {
    font-size: 1.2rem;
    font-weight: 700;
    margin: 0 0 6px 0;
}
.match-meta p {
    font-size: 0.875rem;
    color: #475569 !important;
    line-height: 1.6;
    margin: 0 0 14px 0;
}
.progress-track {
    width: 100%;
    height: 8px;
    background: #E2E8F0;
    border-radius: 99px;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 0.6s ease;
}

/* ── SKILLS COMPARISON TABLE ──────────────────────────────────── */
.skills-table {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 16px;
    margin-top: 20px;
}
.skills-col {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 16px;
}
.skills-col-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
    padding-bottom: 10px;
    border-bottom: 1px solid #E2E8F0;
}
.skills-col-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}
.skills-col-header span {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.skills-col-count {
    margin-left: auto;
    font-size: 0.7rem;
    font-weight: 700;
    background: #E2E8F0;
    color: #475569 !important;
    border-radius: 999px;
    padding: 2px 8px;
}

/* ── RECOMMENDATION BANNER ────────────────────────────────────── */
.rec-banner {
    border-radius: 12px;
    padding: 20px 24px;
    margin-top: 24px;
    display: flex;
    align-items: flex-start;
    gap: 16px;
}
.rec-banner-icon {
    width: 44px;
    height: 44px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
}
.rec-banner h4 {
    margin: 0 0 4px 0;
    font-size: 0.95rem;
    font-weight: 700;
}
.rec-banner p {
    margin: 0;
    font-size: 0.86rem;
    line-height: 1.55;
}
.rec-green  { background:#F0FDF4; border:1px solid #86EFAC; }
.rec-amber  { background:#FFFBEB; border:1px solid #FDE68A; }
.rec-orange { background:#FFF7ED; border:1px solid #FDBA74; }
.rec-red    { background:#FEF2F2; border:1px solid #FECACA; }
.rec-green  .rec-banner-icon { background:#DCFCE7; }
.rec-amber  .rec-banner-icon { background:#FEF3C7; }
.rec-orange .rec-banner-icon { background:#FFEDD5; }
.rec-red    .rec-banner-icon { background:#FEE2E2; }

/* ── RAW JSON EXPANDER ────────────────────────────────────────── */
.json-section {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 24px;
    margin-top: 24px;
}

/* ── UPLOAD ZONE CARDS ────────────────────────────────────────── */
.upload-card {
    background: #FFFFFF;
    border: 1.5px dashed #CBD5E1;
    border-radius: 14px;
    padding: 28px 24px;
    text-align: center;
    transition: border-color 0.2s, background 0.2s;
}
.upload-card:hover {
    border-color: #6366F1;
    background: #F5F3FF;
}
.upload-card-icon {
    font-size: 2rem;
    margin-bottom: 8px;
}
.upload-card h4 {
    font-size: 0.95rem;
    font-weight: 700;
    color: #0F172A !important;
    margin: 0 0 4px 0;
}
.upload-card p {
    font-size: 0.8rem;
    color: #94A3B8 !important;
    margin: 0;
}
.upload-ready {
    border-color: #10B981 !important;
    background: #F0FDF4 !important;
}
.upload-ready-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #DCFCE7;
    color: #15803D !important;
    border: 1px solid #86EFAC;
    border-radius: 999px;
    padding: 4px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-top: 8px;
}
</style>
"""


# ─────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────

def _score_color(score: int) -> str:
    if score >= 80: return "#10B981"
    if score >= 60: return "#F59E0B"
    if score >= 40: return "#EF4444"
    return "#DC2626"

def _score_label(score: int) -> str:
    if score >= 80: return "Excellent"
    if score >= 60: return "Good"
    if score >= 40: return "Moderate"
    return "Low"

def _rec_class(score: int) -> str:
    if score >= 80: return "rec-green"
    if score >= 60: return "rec-amber"
    if score >= 40: return "rec-orange"
    return "rec-red"

def _rec_icon(score: int) -> str:
    if score >= 80: return "✓"
    if score >= 60: return "⚡"
    if score >= 40: return "△"
    return "✕"

def _kv(label: str, value: str, highlight: bool = False) -> str:
    cls = "kv-value highlight" if highlight else "kv-value"
    return (
        f'<div class="kv-cell">'
        f'  <div class="kv-label">{label}</div>'
        f'  <div class="{cls}" title="{value}">{value or "—"}</div>'
        f'</div>'
    )

def _tag(text: str, color: str = "slate") -> str:
    return f'<span class="tag {color}">{text}</span>'

def _tags_block(items: list, color: str = "slate") -> str:
    if not items:
        return '<span style="font-size:0.8rem;color:#94A3B8;">None</span>'
    return '<div class="tags-row">' + "".join(_tag(i, color) for i in items) + "</div>"

def _section_header(num: int, title: str, subtitle: str = "") -> str:
    return f"""
    <div class="section-title-row">
      <div class="section-title-left">
        <div class="section-number">{num}</div>
        <h3>{title}</h3>
      </div>
      {'<span class="section-subtitle">' + subtitle + '</span>' if subtitle else ''}
    </div>
    """


# ─────────────────────────────────────────────────────────────────
# Stage 1 — Job Description
# ─────────────────────────────────────────────────────────────────

def _render_jd(jd: dict):
    ats = jd.get("ats", {})
    role = jd.get("role") or "—"
    company = jd.get("company") or "—"
    location = jd.get("location") or "—"
    exp = jd.get("experience") or "—"
    emp_type = jd.get("employment_type") or "—"
    ats_score = ats.get("score", 0)
    ats_diff = ats.get("difficulty") or "—"

    kv_row1 = (
        _kv("Role / Position", role, highlight=True)
        + _kv("Company", company)
        + _kv("Location", location)
        + _kv("Experience Required", exp)
    )
    kv_row2 = (
        _kv("Employment Type", emp_type)
        + _kv("Education", jd.get("education") or "—")
        + _kv("ATS Difficulty", ats_diff)
        + _kv("ATS Score", f"{ats_score} / 100")
    )

    summary = jd.get("summary", "")
    summary_html = (
        f'<div class="summary-box">{summary}</div>'
        if summary else ""
    )

    # Skill groups
    req   = jd.get("required_skills", [])
    pref  = jd.get("preferred_skills", [])
    langs = jd.get("programming_languages", [])
    fw    = jd.get("frameworks", [])
    dbs   = jd.get("databases", [])
    cloud = jd.get("cloud_platforms", [])
    ai_t  = jd.get("ai_tools", [])
    devops= jd.get("devops_tools", [])
    soft  = jd.get("soft_skills", [])

    skills_html = ""
    groups = [
        ("Required Skills", req, "blue"),
        ("Preferred Skills", pref, "sky"),
        ("Languages", langs, "slate"),
        ("Frameworks", fw, "slate"),
        ("Databases", dbs, "slate"),
        ("Cloud Platforms", cloud, "slate"),
        ("AI / ML Tools", ai_t, "slate"),
        ("DevOps", devops, "slate"),
        ("Soft Skills", soft, "slate"),
    ]
    for label, items, color in groups:
        if items:
            skills_html += f'<div class="tag-group-label">{label}</div>'
            skills_html += _tags_block(items, color)

    st.markdown(
        f"""
        <div class="section-card">
            {_section_header(1, "Job Description Analysis", f"Role: {role} · {company}")}
            <div class="kv-grid">{kv_row1}</div>
            <div class="kv-grid">{kv_row2}</div>
            {summary_html}
            {skills_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────
# Stage 2 — Resume
# ─────────────────────────────────────────────────────────────────

def _render_resume(resume: dict):
    ats   = resume.get("ats", {})
    name  = resume.get("name") or "—"
    email = resume.get("email") or "—"
    phone = resume.get("phone") or "—"
    loc   = resume.get("location") or "—"
    li    = resume.get("linkedin") or "—"
    gh    = resume.get("github") or "—"
    ats_s = ats.get("score", 0)

    kv_row = (
        _kv("Full Name", name, highlight=True)
        + _kv("Email", email)
        + _kv("Phone", phone)
        + _kv("Location", loc)
    )
    kv_row2 = (
        _kv("LinkedIn", li)
        + _kv("GitHub", gh)
        + _kv("Resume ATS Score", f"{ats_s} / 100")
        + _kv("ATS Strengths", f"{len(ats.get('strengths', []))} found")
    )

    summary = resume.get("professional_summary") or resume.get("summary") or ""
    summary_html = (
        f'<div class="summary-box">{summary}</div>'
        if summary else ""
    )

    # Skills
    tech   = resume.get("technical_skills", [])
    langs  = resume.get("programming_languages", [])
    fw     = resume.get("frameworks", [])
    dbs    = resume.get("databases", [])
    cloud  = resume.get("cloud_platforms", [])
    ai_t   = resume.get("ai_tools", [])
    soft   = resume.get("soft_skills", [])

    skills_html = ""
    groups = [
        ("Technical Skills", tech, "sky"),
        ("Languages", langs, "slate"),
        ("Frameworks", fw, "slate"),
        ("Databases", dbs, "slate"),
        ("Cloud Platforms", cloud, "slate"),
        ("AI / ML Tools", ai_t, "slate"),
        ("Soft Skills", soft, "slate"),
    ]
    for label, items, color in groups:
        if items:
            skills_html += f'<div class="tag-group-label">{label}</div>'
            skills_html += _tags_block(items, color)

    # Education & Experience summary
    edu   = resume.get("education", [])
    edu_html = ""
    if edu:
        edu_html += '<div class="tag-group-label">Education</div><div class="tags-row">'
        for e in edu:
            deg  = e.get("degree", "")
            inst = e.get("institution", "")
            yr   = e.get("year", "")
            label = f"{deg} — {inst}" + (f" ({yr})" if yr else "")
            edu_html += _tag(label.strip(" —"), "slate")
        edu_html += "</div>"

    exp   = resume.get("experience", [])
    exp_html = ""
    if exp:
        exp_html += '<div class="tag-group-label">Work Experience</div><div class="tags-row">'
        for e in exp:
            label = f"{e.get('role','')}, {e.get('company','')}".strip(", ")
            if label:
                exp_html += _tag(label, "sky")
        exp_html += "</div>"

    certs = resume.get("certifications", [])
    certs_html = ""
    if certs:
        certs_html += '<div class="tag-group-label">Certifications</div>'
        certs_html += _tags_block(certs, "amber")

    st.markdown(
        f"""
        <div class="section-card">
            {_section_header(2, "Resume Analysis", f"Candidate: {name}")}
            <div class="kv-grid">{kv_row}</div>
            <div class="kv-grid">{kv_row2}</div>
            {summary_html}
            {skills_html}
            {edu_html}
            {exp_html}
            {certs_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────
# Stage 3 — Match Analysis
# ─────────────────────────────────────────────────────────────────

def _render_match(match: dict, recommendation: str, jd: dict, resume: dict):
    score   = match["score"]
    matched = match["matched"]
    missing = match["missing"]
    extra   = match["extra"]
    color   = _score_color(score)
    label   = _score_label(score)
    r_class = _rec_class(score)
    r_icon  = _rec_icon(score)

    C  = 2 * 3.14159 * 44
    dash = C * score / 100
    gap  = C - dash

    role   = jd.get("role", "the role")
    cname  = resume.get("name", "Candidate")

    # Donut SVG
    donut_svg = f"""
    <svg width="110" height="110" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="44" fill="none" stroke="#E2E8F0" stroke-width="10"/>
        <circle cx="50" cy="50" r="44" fill="none" stroke="{color}" stroke-width="10"
            stroke-dasharray="{dash:.1f} {gap:.1f}" stroke-linecap="round"
            transform="rotate(-90 50 50)"/>
    </svg>
    """

    # Progress bar
    progress_bar = f"""
    <div class="progress-track">
        <div class="progress-fill" style="width:{score}%;background:{color};"></div>
    </div>
    """

    # Skills comparison columns
    def col_body(items: list, tag_color: str) -> str:
        if not items:
            return '<p style="font-size:0.78rem;color:#94A3B8;margin:0;">None</p>'
        return "".join(
            f'<div style="padding:6px 0;border-bottom:1px solid #F1F5F9;font-size:0.82rem;'
            f'font-weight:600;color:#1E293B;">{i}</div>'
            for i in items
        )

    matched_col = f"""
    <div class="skills-col">
        <div class="skills-col-header">
            <div class="skills-col-dot" style="background:#10B981;"></div>
            <span style="color:#065F46;">Matched</span>
            <span class="skills-col-count">{len(matched)}</span>
        </div>
        {col_body(matched, "green")}
    </div>
    """
    missing_col = f"""
    <div class="skills-col">
        <div class="skills-col-header">
            <div class="skills-col-dot" style="background:#EF4444;"></div>
            <span style="color:#991B1B;">Missing</span>
            <span class="skills-col-count">{len(missing)}</span>
        </div>
        {col_body(missing, "red")}
    </div>
    """
    extra_col = f"""
    <div class="skills-col">
        <div class="skills-col-header">
            <div class="skills-col-dot" style="background:#F59E0B;"></div>
            <span style="color:#92400E;">Additional</span>
            <span class="skills-col-count">{len(extra)}</span>
        </div>
        {col_body(extra, "amber")}
    </div>
    """

    # ATS analysis for JD
    ats_reasons = jd.get("ats", {}).get("reasons", [])
    ats_html = ""
    if ats_reasons:
        ats_items = "".join(
            f'<li style="font-size:0.82rem;color:#475569;margin-bottom:4px;">{r}</li>'
            for r in ats_reasons
        )
        ats_html = f"""
        <div class="tag-group-label" style="margin-top:20px;">ATS Screening Factors</div>
        <ul style="margin:8px 0 0 16px;padding:0;">{ats_items}</ul>
        """

    st.markdown(
        f"""
        <div class="section-card">
            {_section_header(3, "Skill Match Analysis", f"{cname} vs. {role}")}

            <div class="match-score-block">
                <div class="score-donut-wrap">
                    {donut_svg}
                    <div class="score-center-text">
                        <span class="score-num" style="color:{color};">{score}</span>
                        <span class="score-pct">% MATCH</span>
                    </div>
                </div>
                <div class="match-meta">
                    <h2 style="color:{color};">{label} Match</h2>
                    <p>
                        <strong>{len(matched)}</strong> of <strong>{len(matched)+len(missing)}</strong>
                        required skills matched &nbsp;·&nbsp;
                        <strong>{len(missing)}</strong> gaps identified &nbsp;·&nbsp;
                        <strong>{len(extra)}</strong> additional skills
                    </p>
                    {progress_bar}
                </div>
            </div>

            <div class="skills-table">
                {matched_col}
                {missing_col}
                {extra_col}
            </div>

            {ats_html}

            <div class="rec-banner {r_class}">
                <div class="rec-banner-icon">{r_icon}</div>
                <div>
                    <h4 style="color:#0F172A;">Recommendation</h4>
                    <p style="color:#334155;">{recommendation}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────
# Raw JSON
# ─────────────────────────────────────────────────────────────────

def _render_raw(result: dict):
    with st.expander("View Raw JSON Output", expanded=False):
        t1, t2, t3 = st.tabs(["Job Description", "Resume", "Match Data"])
        with t1:
            st.json(result["jd"])
        with t2:
            st.json(result["resume"])
        with t3:
            st.json(result["match"])


# ─────────────────────────────────────────────────────────────────
# Pipeline header + stepper (shown above results)
# ─────────────────────────────────────────────────────────────────

def _render_pipeline_header(score: int):
    color = _score_color(score)
    st.markdown(
        f"""
        <div class="pipe-header">
            <div class="pipe-header-left">
                <h1>Talent Match Pipeline</h1>
                <p>AI-powered end-to-end candidate screening and skill gap analysis</p>
            </div>
            <div>
                <span class="pipe-badge">Analysis Complete</span>
            </div>
        </div>

        <div class="stepper-wrap">
            <div class="step-item">
                <div class="step-circle done">✓</div>
                <div class="step-label">
                    <h4>JD Extraction</h4>
                    <p>Role, skills &amp; requirements parsed</p>
                </div>
            </div>
            <div class="step-connector done"></div>
            <div class="step-item">
                <div class="step-circle done">✓</div>
                <div class="step-label">
                    <h4>Resume Parsing</h4>
                    <p>Candidate profile structured</p>
                </div>
            </div>
            <div class="step-connector done"></div>
            <div class="step-item">
                <div class="step-circle done">✓</div>
                <div class="step-label">
                    <h4>Skill Matching</h4>
                    <p>Gap analysis at <span style="color:{color};font-weight:800;">{score}%</span> match</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────
# Public entry point
# ─────────────────────────────────────────────────────────────────

def show_pipeline_dashboard(result: dict):
    """Render the enterprise-grade 3-stage pipeline results dashboard."""
    st.markdown(PIPELINE_CSS, unsafe_allow_html=True)

    score = result["match"]["score"]
    _render_pipeline_header(score)
    _render_jd(result["jd"])
    _render_resume(result["resume"])
    _render_match(result["match"], result["recommendation"], result["jd"], result["resume"])
    _render_raw(result)


def show_pipeline_upload():
    """
    Render the enterprise upload interface.
    Returns (uploaded_jd, uploaded_resume) Streamlit UploadedFile objects or (None, None).
    """
    st.markdown(PIPELINE_CSS, unsafe_allow_html=True)

    # Page header
    st.markdown(
        """
        <div class="pipe-header">
            <div class="pipe-header-left">
                <h1>Talent Match Pipeline</h1>
                <p>Upload a Job Description and a Resume to run the full AI-powered screening pipeline</p>
            </div>
            <span class="pipe-badge">Ready</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Stepper — idle state
    st.markdown(
        """
        <div class="stepper-wrap">
            <div class="step-item">
                <div class="step-circle active">1</div>
                <div class="step-label">
                    <h4>Upload Documents</h4>
                    <p>JD + Resume (PDF or DOCX)</p>
                </div>
            </div>
            <div class="step-connector"></div>
            <div class="step-item">
                <div class="step-circle idle">2</div>
                <div class="step-label">
                    <h4>AI Extraction</h4>
                    <p>Parse &amp; structure both documents</p>
                </div>
            </div>
            <div class="step-connector"></div>
            <div class="step-item">
                <div class="step-circle idle">3</div>
                <div class="step-label">
                    <h4>Skill Analysis</h4>
                    <p>Match score &amp; gap report</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_jd, col_res = st.columns(2, gap="large")

    with col_jd:
        st.markdown(
            """
            <div class="upload-card">
                <div class="upload-card-icon">📋</div>
                <h4>Job Description</h4>
                <p>PDF or DOCX · Max 10 MB</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        uploaded_jd = st.file_uploader(
            "Job Description",
            type=["pdf", "docx"],
            key="pipeline_jd",
            label_visibility="collapsed",
        )
        if uploaded_jd:
            st.markdown(
                f'<div class="upload-ready-badge">✓ &nbsp;{uploaded_jd.name}</div>',
                unsafe_allow_html=True,
            )

    with col_res:
        st.markdown(
            """
            <div class="upload-card">
                <div class="upload-card-icon">👤</div>
                <h4>Candidate Resume</h4>
                <p>PDF or DOCX · Max 10 MB</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        uploaded_resume = st.file_uploader(
            "Resume",
            type=["pdf", "docx"],
            key="pipeline_resume",
            label_visibility="collapsed",
        )
        if uploaded_resume:
            st.markdown(
                f'<div class="upload-ready-badge">✓ &nbsp;{uploaded_resume.name}</div>',
                unsafe_allow_html=True,
            )

    return uploaded_jd, uploaded_resume
