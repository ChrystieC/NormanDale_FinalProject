# read_data.py

import json

class ReadData:
    # def __init__(self, json_path = None, txt_path = None):
    #     self.json_path = json_path
    #     self.txt_path = txt_path

    def read_json(json_path, file_name):
        with open(json_path, "r") as f:
            file_name = json.load(f)

        return file_name

    def read_txt(txt_path, file_name):
        with open(txt_path, "r") as f:
            file_name = f.readlines()

        return file_name