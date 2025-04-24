# read_data.py

import json

class ReadDataJson:
    def read_json(self, json_path, file_name):
        with open(json_path, "r") as f:
            file_name = json.load(f)

        return file_name