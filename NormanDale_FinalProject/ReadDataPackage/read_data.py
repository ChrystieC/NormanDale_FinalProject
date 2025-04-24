# read_data.py

import json

class ReadData:
    def read_json(file_path):
        with open(file_path, "r") as f:
            return json.load(f)


