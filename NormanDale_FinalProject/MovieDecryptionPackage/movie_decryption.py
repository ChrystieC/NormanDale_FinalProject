# movie_decryption.py

from cryptography.fernet import Fernet

class MovieDecryption:
    def __init__(self, location_name):
        self.decryption_key = "tpeVVwifsg2Ga_CzYCndI9BC_HHzkj_pT_WyY2t_SeI="
        self.team_encryption = str(teams[location_name])
        self.f = Fernet(self.decryption_key)

    def decrypt_movie(self):
        movie_name = self.f.decrypt(self.team_encryption)
        return movie_name