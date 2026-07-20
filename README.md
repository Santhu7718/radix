# RADIX Talent Match

A Streamlit-powered AI recruitment intelligence platform for analyzing job descriptions, parsing resumes, building candidate profiles, checking talent readiness, and matching resumes to jobs.

## Features

- **Job Description Analytics**: extract skills, responsibilities, education, certifications, ATS score, and more from uploaded JD files.
- **Resume Parser**: parse PDF/DOCX resumes and extract projects, experience, education, certifications, skills, and achievements.
- **AI Profile Builder**: generate candidate profiles from resumes for quick review and editing.
- **Talent Check**: compare candidate readiness against company-specific requirements and get a match score, missing skills, and a learning roadmap.
- **Skill Matching**: compare uploaded resumes with job descriptions, identify matched/missing/extra skills, and calculate a match score.

## Requirements

- Python 3.10+ recommended
- Streamlit
- Google Gemini / Groq OpenAI-compatible API access
- `requirements.txt` dependencies:
  - streamlit
  - google-generativeai
  - pdfplumber
  - python-docx
  - python-dotenv
  - pandas
  - numpy
  - plotly
  - pydantic
  - reportlab
  - Pillow
  - streamlit-extras

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-org/jd_analytics.git
cd jd_analytics
```

2. Create and activate a Python virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Gemini/Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

## Run the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Then open the provided local URL in your browser.

## Application Modules

- **Home**: overview, workflow, and platform metrics.
- **JD Analytics**: upload a job description file and analyze it with Gemini AI.
- **Resume Parser**: upload a resume file and extract structured candidate information.
- **Profile Builder**: generate an editable AI profile from a resume upload.
- **Talent Check**: analyze candidate readiness for selected companies.
- **Skill Matching**: compare a resume to a job description and measure skill fit.

## Project Structure

- `app.py` — main Streamlit app and navigation.
- `ai/` — AI integration, prompts, and extraction logic for Gemini.
- `parser/` — file parsing for PDF and DOCX content extraction.
- `services/` — business logic for JD analytics, resume analysis, talent comparison, and skill matching.
- `ui/` — Streamlit dashboard components and page layouts.
- `utils/` — helper functions for file handling and utilities.
- `exporter/` — JSON export utilities for analysis results.
- `data/` — company and configuration data.
- `assets/` — CSS styling for the app.
- `output/` — generated analysis output files.

## Notes

- The app relies on the `GROQ_API_KEY` environment variable to connect to the Gemini AI endpoint.
- Supported upload formats: `PDF`, `DOCX`.
- JD analytics results are also saved to `output/jd_analysis.json`.

## License

This repository does not include a license file. Add one if you want to share or publish the project.
