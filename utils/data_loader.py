import json
from pathlib import Path

def load_login_data():
    path = Path("test_data/login_creds.json")
    with open(path) as f:
        return json.load(f)
