# File Name: main.py
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

from ReadDataPackage.read_json import *
from ReadDataPackage.read_txt import *
from MovieDecryptionPackage.movie_decryption import *
from LocationDecryptionPackage.location_decryption import *
from LoadPhotoPackage.show_photo import *
from PIL import Image

if __name__ == "__main__":

    group_name = "Norman Dale"
    Read_Data_Json = ReadDataJson() # Create an instance of the ReadDataJson class

    encrypted_groups = Read_Data_Json.read_json(json_path="Data/EncryptedGroupHints Spring 2025.json") # Read the encrypted group hints about location

    movie_encrypted = Read_Data_Json.read_json(json_path="Data/TeamsAndEncryptedMessagesForDistribution.json") # Read the encrypted movie hints

    Read_Data_TXT = ReadDataTXT() # Create an instance of the ReadDataTXT class
    uceng = Read_Data_TXT.read_txt(txt_path="Data/UCEnglish.txt") # Read the UCEnglish.txt file for location decryption

    Location_decryption = LocationDecryption(location_name=group_name, 
                                             encrypted_data=encrypted_groups, 
                                             uceng=uceng) # Create an instance of the LocationDecryption class, which is used to decrypt location hint
    location_sentence = Location_decryption.decryption_location() # Decrypt the location hints
    print(f'The decrypted location is: {location_sentence}')

    movie_decryption = MovieDecryption(encrypted_data=movie_encrypted, target_key=group_name) # Create an instance of the MovieDecryption class, which is used to decrypt movie hint
    print(f'The decrypted movie is: {movie_decryption.decrypt_movie()}') # Decrypt the movie hint and print it

    Load_photo = LoadPhoto('group_photo.jpeg') # Create an instance of the LoadPhoto class, which is used to load and show the group photo
    Load_photo.show_photo() # Show the group photo


