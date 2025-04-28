# File Name: show_photo.py
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

from PIL import Image
import os

class LoadPhoto:
    """
    This class is used to load and show a photo.
    """
    def __init__(self, path):
        """
        Initialize the LoadPhoto class with the path to the photo.
        @param path String: path of the photo
        """
        self.path = path

    def show_photo(self):
        """
        This method loads and shows the photo.
        @return: None
        """
        try:
            current_dir = os.path.dirname(__file__) # Get the current directory of this file (show_photo.py)
            parent_path = os.path.dirname(current_dir) # Get the parent directory of this file 
            img_path = os.path.join(parent_path, 'Data', self.path) # Construct the full path to the image file

            # Open the image and verify if it is valid
            img = Image.open(img_path) 
            img.verify()
            print("Image is verified")

            # Show the image
            img = Image.open(img_path)
            img.show()
        except Exception as e:
            # Throw an exception if the image is not valid
            print(e)