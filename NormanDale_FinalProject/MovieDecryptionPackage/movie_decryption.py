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
# Citations: google search ai, 

# Anything else that's relevant:

from cryptography.fernet import Fernet

def decrypt_json_movie(filepath, key):
    """
    Decrypts a JSON file using a provided key.

    Returns the raw decrypted string instead of a dictionary.
    """
    try:
        f = Fernet(key)
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data.decode()  
    except Exception as e:
        print(f"Decryption error: {e}")
        return None

# Example Usage
key = b'tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI='  
filepath = 'encrypted_data.json' #I haven't adjusted yet since I need to double check which file has the movie stuff

decrypted_data = decrypt_json_movie(filepath, key)

if decrypted_data:
    print("Decrypted data:")
    print(decrypted_data)  
else:
    print("Decryption failed.")
