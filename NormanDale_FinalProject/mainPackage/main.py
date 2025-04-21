from tokenize import group
from ReadDataPackage.read_data import *
from MovieDecryptionPackage.movie_decryption import *
from LocationDecryptionPackage.location_decryption import *

if __name__ == "__main__":

    group_name = "Norman Dale"
    Read_Data = ReadData()

    encrypted_groups = Read_Data.read_json(json_path="Data/EncryptedGroupHints Spring 2025.json",
                                           file_name="encrypted_groups")

    movie_encrypted = Read_Data.read_json(json_path="Data/TeamsAndEncryptedMessagesForDistribution.json",
                                         file_name="movie_encrypted")

    uceng = Read_Data.read_txt(txt_path="Data/UCEnglish.txt", 
                               file_name="uceng")

    Location_decryption = LocationDecryption(location_name=group_name, 
                                             encrypted_data=encrypted_groups, 
                                             uceng=uceng)
    Location_decryption.decryption_location()

    movie_decryption = MovieDecryption(encrypted_data=movie_encrypted, target_key=group_name)
    print(movie_decryption.decrypt_movie())
