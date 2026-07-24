import os
import json

import google.generativeai as genai

from dotenv import load_dotenv
from prompts import JD_EXTRACTION_PROMPT

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def extract_skills(job_description):

    prompt = JD_EXTRACTION_PROMPT + job_description

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown if Gemini wraps JSON
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
