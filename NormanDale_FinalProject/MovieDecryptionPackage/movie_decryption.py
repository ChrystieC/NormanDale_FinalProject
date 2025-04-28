# File Name: movie_decryption.py
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
from cryptography.fernet import Fernet # type: ignore
class MovieDecryption:
    """
    This class is used to decrypt the movie hints using the Fernet symmetric encryption algorithm.
    """

    def __init__(self, encrypted_data, target_key):
        """
        Initialize the MovieDecryption class with the encrypted data and target key.
        @param encrypted_data Dictionary: The encrypted data containing the movie hints.
        @param target_key String: The key used to identify the movie hint in the encrypted data.
        """
        
        self.key_string = "tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI=" # Assign the default key string to an attribute
        self.movie_encryption = str(encrypted_data[target_key])
        self.f = Fernet(self.key_string)

    def decrypt_movie(self):
        """
        Decrypt the movie hint using the Fernet symmetric encryption algorithm.
        @return String: The decrypted movie hint.
        """
        decrypted_data = self.f.decrypt(self.movie_encryption)
        return decrypted_data