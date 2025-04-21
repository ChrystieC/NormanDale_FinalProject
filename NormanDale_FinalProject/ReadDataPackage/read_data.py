# read_data.py

import json

class ReadData:
    def read_json(self, json_path, file_name):
        with open(json_path, "r") as f:
            file_name = json.load(f)

        return file_name

    def read_txt(self, txt_path, file_name):
        with open(txt_path, "r") as f:
            file_name = f.readlines()

        return file_name