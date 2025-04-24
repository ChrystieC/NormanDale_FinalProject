# Annapoorna
# File Name: movie_decryption.py
# Student Name: Annapoorna Nair
# Email:
# Assignment Number: Final project
# Due Date: April 30, 2025
# Course #/Section: IS4010 Section 1
# Semester/Year: Spring 2025
# Brief Description of the assignment:
# Brief Description of what this module does:
# Citations: google search ai, chatgpt
# Anything else that's relevant:

import json
from cryptography.fernet import Fernet # type: ignore
class MovieDecryption:

    def __init__(self, encrypted_data, target_key):

        self.key_string = "tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI="
        self.movie_encryption = str(encrypted_data[target_key])
        self.f = Fernet(self.key_string)

    def decrypt_movie(self):

        decrypted_data = self.f.decrypt(self.movie_encryption)
        return decrypted_data