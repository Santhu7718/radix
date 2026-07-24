import json

from app.ai.gemini import client, MODEL_NAME
from app.ai.prompts import RESUME_ANALYSIS_PROMPT


def extract_resume_information(resume_text):
    """
    Extract structured resume information using Groq/OpenAI-compatible API.
    """

    prompt = f"{RESUME_ANALYSIS_PROMPT}\n\n{resume_text}"

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
        # Default fields
        # --------------------------------------------------

        defaults = {
            "name": "",
            "email": "",
            "phone": "",
            "location": "",
            "linkedin": "",
            "github": "",
            "summary": "",
            "skills": [],
            "technical_skills": [],
            "soft_skills": [],
            "projects": [],
            "experience": [],
            "education": [],
            "certifications": [],
            "languages": [],
            "achievements": []
        }

        for key, value in defaults.items():
            data.setdefault(key, value)

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