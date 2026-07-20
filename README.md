# 🚀 RADIX Talent Match

> **AI-Powered Recruitment & Candidate Evaluation Platform**

RADIX Talent Match is an intelligent recruitment platform that automates resume analysis, job description understanding, candidate evaluation, and skill matching using Large Language Models (LLMs). The platform helps recruiters make faster, more informed hiring decisions while giving candidates personalized insights into their strengths and areas for improvement.

---

# 📌 Problem Statement

Recruiters spend significant time manually reviewing resumes, comparing candidates with job descriptions, and identifying suitable talent. Traditional Applicant Tracking Systems (ATS) often rely on keyword matching, which can overlook qualified candidates.

RADIX Talent Match solves this problem using AI-powered semantic analysis, enabling intelligent candidate evaluation beyond simple keyword searches.

---

# 🎯 Objectives

- Automate resume parsing
- Analyze job descriptions using AI
- Build structured candidate profiles
- Evaluate candidate strengths and weaknesses
- Calculate job matching scores
- Identify missing skills
- Provide AI-generated recommendations
- Reduce recruitment time and improve hiring accuracy

---

# ✨ Features

## 📄 Resume Parsing
- Upload Resume (PDF)
- AI-based information extraction
- Structured candidate profile generation

Extracts:
- Name
- Contact Details
- Education
- Experience
- Projects
- Technical Skills
- Certifications
- Internships
- Hackathons
- Achievements
- LinkedIn
- GitHub

---

## 📊 Job Description Analytics

Analyze job descriptions to extract:

- Required Skills
- Preferred Skills
- Experience Requirements
- Education Requirements
- Responsibilities
- Technical Stack
- Soft Skills
- Domain
- Keywords

---

## 👤 AI Profile Builder

Edit and manage candidate profiles.

Supports:

- Personal Information
- Education
- Experience
- Projects
- Programming Languages
- Frameworks
- Databases
- Cloud Platforms
- AI Tools
- Soft Skills
- Certifications
- Internships
- Hackathons
- Achievements
- Preferred Roles
- Work Mode
- Expected Salary

---

## 🧠 Talent Check

Evaluate candidates across multiple competency areas:

- Programming
- Technical Skills
- Projects
- Experience
- Education
- AI/ML Knowledge
- Cloud Skills
- Database Skills
- Communication
- Problem Solving
- Certifications
- Career Readiness

Outputs:

- Strengths
- Weaknesses
- AI Recommendations
- Readiness Score

---

## 🎯 Skill Matching

Compare candidate profiles with job descriptions.

Provides:

- Overall Match Percentage
- Matching Skills
- Missing Skills
- ATS Compatibility
- Hiring Recommendation
- Skill Gap Analysis

---

# 🏗 System Architecture

```
                  Resume PDF
                      │
                      ▼
             Resume Upload Module
                      │
                      ▼
             AI Resume Parser
                      │
                      ▼
          Structured Candidate Profile
                      │
                      ▼
             AI Profile Builder
                      │
                      ▼
              Saved Candidate Profile
                      │
          ┌───────────┴────────────┐
          ▼                        ▼
    Talent Check             Skill Matching
          │                        │
          ▼                        ▼
 AI Candidate Evaluation     JD Analytics
          │                        │
          └───────────┬────────────┘
                      ▼
             Final Hiring Report
```

---

# 🛠 Technology Stack

## Frontend
- Streamlit

## Backend
- Python

## AI
- Groq API
- Llama 3.3 70B Versatile
- Prompt Engineering
- NLP

## Data Processing
- JSON
- Regex
- Text Processing

## File Handling
- PDF Resume Parsing

## Storage
- JSON
- Streamlit Session State

---

# 📚 Python Libraries

- streamlit
- groq
- openai (Groq-compatible)
- python-dotenv
- json
- os
- re
- pathlib
- datetime
- typing
- PyPDF2 / pdfplumber

---

# 📂 Project Structure

```
RADIX-Talent-Match/
│
├── app.py
├── requirements.txt
├── README.md
│
├── services/
│   ├── resume_service.py
│   ├── jd_service.py
│   ├── profile_service.py
│   ├── talent_service.py
│   └── matching_service.py
│
├── ui/
│   ├── upload_resume.py
│   ├── jd_analytics.py
│   ├── profile_dashboard.py
│   ├── talent_check.py
│   └── skill_matching.py
│
├── data/
│
├── assets/
│
└── utils/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/RADIX-Talent-Match.git

cd RADIX-Talent-Match
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
```

---

# ▶ Running the Application

```bash
streamlit run app.py
```

---

# 📷 Workflow

```
Upload Resume
      │
      ▼
Resume Parsing
      │
      ▼
Profile Builder
      │
      ▼
Talent Check
      │
      ▼
JD Analytics
      │
      ▼
Skill Matching
      │
      ▼
Final Hiring Report
```

---

# 🌟 Future Enhancements

- Recruiter Dashboard
- Candidate Login
- Multi-Resume Ranking
- Interview Question Generator
- Resume Improvement Suggestions
- PDF Report Generation
- Email Integration
- Database Integration (PostgreSQL/MySQL)
- Authentication & Authorization
- Analytics Dashboard
- Multi-language Support

---

# 👥 Team

**Team Name:** RADIX

Members:

- BOYA SAI KIRAN
- *(Add remaining team members here)*

---

# 📄 License

This project was developed for educational purposes and hackathons.

---

# 🙌 Acknowledgements

- Groq
- Streamlit
- Meta Llama
- Python Community
- Open Source Contributors
