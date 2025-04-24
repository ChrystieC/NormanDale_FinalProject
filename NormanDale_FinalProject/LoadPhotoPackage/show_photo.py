# show_photo.py

from PIL import Image
import os

class LoadPhoto:
    def __init__(self, path):
        self.path = path

    def show_photo(self):
        try:
            current_dir = os.path.dirname(__file__)
            img_path = os.path.join(current_dir, self.path)

            img = Image.open(img_path)
            img.verify()
            print("Image is verified")
            img.show()
        except Exception as e:
            print(e)


Load_photo = LoadPhoto('group_photo.png')
Load_photo.show_photo()