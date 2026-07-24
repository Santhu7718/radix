from app.parser.parser import extract_text

from app.ai.jd_extractor import extract_job_information

from app.exporter.json_export import save_json


def analyze_jd(file_path):

    text = extract_text(file_path)

    result = extract_job_information(text)

    save_json(result)

    return result