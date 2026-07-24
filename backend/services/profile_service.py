import json
import os

PROFILE_FILE = "profiles/saved_profile.json"


def save_profile(profile):

    os.makedirs("profiles", exist_ok=True)

    with open(PROFILE_FILE, "w") as f:

        json.dump(profile, f, indent=4)


def load_profile():

    if not os.path.exists(PROFILE_FILE):

        return {}

    with open(PROFILE_FILE) as f:

        return json.load(f)