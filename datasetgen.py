import os
import shutil

source_folder = "PATH_CLIC/train"
dest_folder = "train"

def filenamegenerator():
    i = 0
    while True:
        yield f"img{i}.png"
        i+=1
filename_gen = filenamegenerator()
for subfolder in os.listdir(source_folder):
    for file in os.listdir(f"{source_folder}/{subfolder}"):
        source = f"{source_folder}/{subfolder}/{file}"
        dest = f"{dest_folder}/{next(filename_gen)}"
        if os.path.isfile(source):
            shutil.copy(source, dest)