from services.profile_service import load_profile
from services.jd_service import analyze_jd


def normalize(skills):
    """
    Normalize skill names.
    """

    normalized = set()

    for skill in skills:

        if not skill:
            continue

        normalized.add(skill.strip().lower())

    return normalized


def compare_with_jd(jd_path):

    profile = load_profile()

    jd = analyze_jd(jd_path)

    # ---------------------------------------
    # Candidate Skills
    # ---------------------------------------

    candidate = []

    candidate.extend(profile.get("technical_skills", []))
    candidate.extend(profile.get("programming_languages", []))
    candidate.extend(profile.get("frameworks", []))
    candidate.extend(profile.get("databases", []))

    candidate = normalize(candidate)

    # ---------------------------------------
    # JD Skills
    # ---------------------------------------

    jd_skills = []

    jd_skills.extend(jd.get("required_skills", []))
    jd_skills.extend(jd.get("preferred_skills", []))
    jd_skills.extend(jd.get("programming_languages", []))
    jd_skills.extend(jd.get("frameworks", []))
    jd_skills.extend(jd.get("databases", []))
    jd_skills.extend(jd.get("cloud_platforms", []))
    jd_skills.extend(jd.get("ai_tools", []))
    jd_skills.extend(jd.get("devops_tools", []))
    jd_skills.extend(jd.get("soft_skills", []))

    required = normalize(jd_skills)

    # ---------------------------------------
    # Compare
    # ---------------------------------------

    matched = sorted(candidate & required)

    missing = sorted(required - candidate)

    extra = sorted(candidate - required)

    if len(required) == 0:
        score = 0
    else:
        score = round(
            (len(matched) / len(required)) * 100
        )

    return {

        "score": score,

        "matched": [m.title() for m in matched],

        "missing": [m.title() for m in missing],

        "extra": [m.title() for m in extra],

        "jd": jd
    }