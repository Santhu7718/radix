from services.profile_service import load_profile
from services.jd_service import analyze_jd


def normalize(skills):
    """
    Normalize skill names to lowercase stripped strings.
    """

    normalized = set()

    for skill in skills:

        if not skill:
            continue

        normalized.add(skill.strip().lower())

    return normalized


def _collect_jd_skills(jd):
    """
    Flatten all skill-related lists from a parsed JD dict.
    """

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

    return jd_skills


def _collect_candidate_skills(profile):
    """
    Flatten all skill-related lists from a parsed resume/profile dict.
    """

    candidate = []

    candidate.extend(profile.get("technical_skills", []))
    candidate.extend(profile.get("programming_languages", []))
    candidate.extend(profile.get("frameworks", []))
    candidate.extend(profile.get("databases", []))
    candidate.extend(profile.get("cloud_platforms", []))
    candidate.extend(profile.get("ai_tools", []))
    candidate.extend(profile.get("soft_skills", []))
    candidate.extend(profile.get("skills", []))

    return candidate


def compare_skills(jd_data, resume_data):
    """
    Core skill-gap comparison.
    Accepts pre-parsed JD dict and resume/profile dict.
    Returns score, matched, missing, and extra skills.
    """

    candidate = normalize(_collect_candidate_skills(resume_data))
    required = normalize(_collect_jd_skills(jd_data))

    matched = sorted(candidate & required)
    missing = sorted(required - candidate)
    extra = sorted(candidate - required)

    score = 0 if len(required) == 0 else round(
        (len(matched) / len(required)) * 100
    )

    return {
        "score": score,
        "matched": [m.title() for m in matched],
        "missing": [m.title() for m in missing],
        "extra": [m.title() for m in extra],
    }


def compare_with_jd(jd_path):
    """
    Legacy entry-point: loads saved profile and compares against a JD file.
    Kept for backward compatibility with the existing Skill Matching sidebar tab.
    """

    profile = load_profile()

    jd = analyze_jd(jd_path)

    result = compare_skills(jd, profile)

    result["jd"] = jd

    return result