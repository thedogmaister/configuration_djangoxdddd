import json
import os

__BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_settings():
    with open("{0}/{1}".format(__BASE_DIR, "../settings.json")) as data_file:
        data = json.load(data_file)
    return data