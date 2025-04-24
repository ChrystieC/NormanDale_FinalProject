# File Name : read_txt.py
# Student Name: Will Claus
# email:  clausws@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   5/1/2025
# Course #/Section:   IS4010-001
# Semester/Year:   2/2025
# Brief Description of the assignment: 

# Brief Description of what this module does.

# Anything else that's relevant:




def read_txt(self, txt_path, file_name):
    with open(txt_path, "r") as f:
        file_name = f.readlines()

    return file_name
