import os
from pathlib import Path

def spaces2dashes():
    for dirpath, dirnames, filenames in os.walk("practice"):
        for fname in filenames:
            oldname = filenames/fname
            newname = filenames/fname.replace(" ", "-")
            print("Replacing ", oldname.name, "with", newname.name)
            oldname.rename(newname)

def dashes2spaces():
    for dirpath, dirnames, filenames in os.walk("practice"):
        for fname in filenames:
            oldname = filenames/fname
            newname = filenames/fname.replace("-", " ")
            print("Replacing ", oldname.name , "with ", newname.name)
            oldname.rename(newname)

#space2dashes()
#dashes2spaces()