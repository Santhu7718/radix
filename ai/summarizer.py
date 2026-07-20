from ai.gemini import client, MODEL_NAME


def generate_summary(job_text):
    """
    Generate a concise summary of a Job Description
    using Groq/OpenAI-compatible API.
    """

    prompt = f"""
Summarize the following Job Description in under 120 words.

Return only the summary.

Job Description:

{job_text}
"""

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
        )

        summary = response.choices[0].message.content.strip()

        return summary

    except Exception as e:

        return f"Error generating summary: {str(e)}"