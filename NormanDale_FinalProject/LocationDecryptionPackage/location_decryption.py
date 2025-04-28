# File Name: location_decryption.py
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

class LocationDecryption:
    """
    This class is used to decrypt the location hints.
    """
    
    def __init__(self, location_name, encrypted_data, uceng):
        """
        Initialize the LocationDecryption class with the location name, encrypted data, and UC English words list.
        @param location_name String: name of the location
        @param encrypted_data Dictionary: dictionary containing the encrypted data
        @param uceng List: list of UC English words
        """
        self.location_name = location_name
        self.encrypted_data = encrypted_data
        self.uceng = uceng

    def decryption_location(self):
        """
        This method decrypts the location hints.
        @return String: decrypted location sentence
        """

        # Get the encrypted data of the provided location.
        self.encrypted_location = self.encrypted_data[self.location_name]
        self.decryption_words = []

        # Loop through each encrypted data to get the UC English word and append in the decryption_words.
        for encryption in self.encrypted_location:
            self.decryption_words.append(self.uceng[int(encryption)].strip())

        # Join the words into a full sentence and print it.
        self.full_sentence = " ".join(self.decryption_words)

        return self.full_sentence