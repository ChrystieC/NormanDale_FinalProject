# Annapoorna
# Decryption key:    tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI=
# File Name : movie_decryption.py
# Student Name: Annapoorna Nair
# email:  nairap
# Assignment Number: Final project
# Due Date:   April 30, 2025
# Course #/Section:   IS4010 Section 1
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: google search ai, chatgpt

# Anything else that's relevant:

import json
from cryptography.fernet import Fernet

def decrypt_json_section(encrypted_data, key_string, target_key):
    """Decrypts a JSON file encrypted with Fernet and returns a specific section."""
    

     f = Fernet(key_string)
     movie_encryption = str (encrypted_data[ target_key])
     decrypted_data = f.decrypt(movie_encryption)
     return decrypted_data

        # Return only the specified section
     

   
# Usage

fernet_key = 'tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI='
target_section = 'Norman Dale'

decrypted_section = decrypt_json_section(encrypted_file, fernet_key, target_section)

