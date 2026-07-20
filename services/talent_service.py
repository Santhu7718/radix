import json
from services.profile_service import load_profile


def load_companies():
    with open("data/companies.json", "r") as f:
        return json.load(f)


def compare_candidate(company_name):

    profile = load_profile()

    companies = load_companies()

    company = companies[company_name]

    candidate_skills = set()

    candidate_skills.update(profile.get("technical_skills", []))
    candidate_skills.update(profile.get("programming_languages", []))
    candidate_skills.update(profile.get("frameworks", []))
    candidate_skills.update(profile.get("databases", []))

    required_skills = set(company["required_skills"])

    matched = sorted(candidate_skills.intersection(required_skills))

    missing = sorted(required_skills.difference(candidate_skills))

    score = round((len(matched) / len(required_skills)) * 100)

    return {
        "company": company_name,
        "industry": company.get("industry", ""),
        "roles": company.get("roles", []),
        "score": score,
        "matched": matched,
        "missing": missing,
        "required": sorted(required_skills)
    }