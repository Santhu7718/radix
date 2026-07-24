from services.jd_service import analyze_jd
from services.resume_service import analyze_resume
from services.skill_matching_service import compare_skills


def _recommendation(score: int) -> str:
    if score >= 80:
        return "Excellent Match — Strong candidate. Ready to apply!"
    elif score >= 60:
        return "Good Match — Consider upskilling in missing areas before applying."
    elif score >= 40:
        return "Moderate Match — Significant skill gaps exist. Focus on learning."
    else:
        return "Low Match — This role requires skills not yet present in the resume."


def run_pipeline(jd_path: str, resume_path: str) -> dict:
    """
    End-to-end pipeline:
      1. Parse + AI-extract Job Description
      2. Parse + AI-extract Resume
      3. Compare skills and calculate match score
      4. Return a unified PipelineResult dict

    Args:
        jd_path:     Absolute file path to the Job Description (PDF/DOCX).
        resume_path: Absolute file path to the Resume (PDF/DOCX).

    Returns:
        {
            "jd":     { ...jd_data },
            "resume": { ...resume_data },
            "match":  { score, matched, missing, extra },
            "recommendation": str
        }
    """

    # -------------------------------------------------------
    # Stage 1 — Job Description
    # -------------------------------------------------------
    jd_data = analyze_jd(jd_path)

    if jd_data.get("status") == "error":
        raise RuntimeError(f"JD extraction failed: {jd_data.get('message')}")

    # -------------------------------------------------------
    # Stage 2 — Resume
    # -------------------------------------------------------
    resume_data = analyze_resume(resume_path)

    if resume_data.get("status") == "error":
        raise RuntimeError(f"Resume extraction failed: {resume_data.get('message')}")

    # -------------------------------------------------------
    # Stage 3 — Skill Matching
    # -------------------------------------------------------
    match = compare_skills(jd_data, resume_data)

    return {
        "jd": jd_data,
        "resume": resume_data,
        "match": match,
        "recommendation": _recommendation(match["score"]),
    }
