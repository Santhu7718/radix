import os

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def save_uploaded_file(uploaded_file):
    """
    Save uploaded Streamlit file.
    Returns the saved file path.
    """

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return file_path