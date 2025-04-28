# File Name: read_json.py
# Student Name: Annapoorna Nair, Eirlys Vo, Will Claus, Chrystie Cadet
# Email: nairap@mail.uc.edu, vopq@mail.uc.edu, clausws@mail.uc.edu, cadetce@mail.uc.edu
# Assignment Number: Final project
# Due Date: May 1st, 2025
# Course #/Section: IS4010 Section 001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Decrypt the location and movie hints and show the group photo with a movie quote at the decrypted location.
# Brief Description of what this module does: Work on final project. 
# Citations: ChatGPT, https://cryptography.io/en/latest/fernet/, https://stackoverflow.com/questions/48176531/python-pil-image-verify-returns-none, https://stackoverflow.com/questions/48176531/python-pil-image-verify-returns-none
# Anything else that's relevant: N/A

import json

class ReadDataJson:
    """
    This class is used to read JSON files.
    """
    def read_json(self, json_path):
        """
        Read the JSON file and return the data.
        @param json_path String: The path to the JSON file.
        @return file Dictionary: The data read from the JSON file.
        """
        with open(json_path, "r") as f:
            file = json.load(f)

        return file