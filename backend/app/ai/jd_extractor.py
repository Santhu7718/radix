import json

from app.ai.gemini import client, MODEL_NAME
from app.ai.prompts import JD_ANALYSIS_PROMPT


def extract_job_information(job_text):
    """
    Extract structured job information from a Job Description
    using Groq/OpenAI-compatible API.
    """

    prompt = f"{JD_ANALYSIS_PROMPT}\n\n{job_text}"

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        result = response.choices[0].message.content.strip()

        # Remove markdown if model returns it
        result = (
            result.replace("```json", "")
                  .replace("```", "")
                  .strip()
        )

        data = json.loads(result)

        # --------------------------------------------------
        # Ensure required keys exist
        # --------------------------------------------------

        defaults = {
            "company": "",
            "role": "",
            "location": "",
            "experience": "",
            "employment_type": "",
            "education": "",
            "certifications": [],
            "salary": "",
            "summary": "",
            "required_skills": [],
            "preferred_skills": [],
            "programming_languages": [],
            "frameworks": [],
            "databases": [],
            "cloud_platforms": [],
            "ai_tools": [],
            "devops_tools": [],
            "soft_skills": [],
            "responsibilities": [],
            "skills": []
        }

        for key, value in defaults.items():
            data.setdefault(key, value)

        # --------------------------------------------------
        # ATS Defaults
        # --------------------------------------------------

        data.setdefault(
            "ats",
            {
                "score": 75,
                "difficulty": "Medium",
                "reasons": [
                    "ATS analysis generated automatically."
                ]
            }
        )

        return data

    except json.JSONDecodeError:

        return {
            "status": "error",
            "message": "Invalid JSON returned by the model.",
            "raw_response": result if "result" in locals() else ""
        }

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }