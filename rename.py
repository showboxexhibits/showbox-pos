import os

for i in os.listdir('.'):
    new_filename = i.lower()
    os.rename(i, new_filename)
