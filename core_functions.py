import pathlib,sys,os
import re

from PIL import Image
from encryption_engine import EncryptionEngine


def encrypt_file(file,rails,offset,direction):
    engine=EncryptionEngine(rails,offset,direction)
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)

    with open(file,"r") as f:
        message=f.read()

    encrypted_substance= engine.encrypt(message)
    name=file.replace(".txt","_e.txt")
    with open(name,"w") as f:
        f.write(encrypted_substance)

def decrypt_file(file,rails,offset,direction):
    engine=EncryptionEngine(rails,offset,direction)
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)

    with open(file,"r") as f:
        message=f.read()
    decrypted_substance= engine.decrypt(message)
    if file.endswith("_e.txt"):
        name=file.replace("_e.txt","_d.txt")
    else:
        name=file.replace(".txt","_d.txt")
    with open(name,"w") as f:
        f.write(decrypted_substance)


def glitch_(file,rails,offset,direction):
    engine=EncryptionEngine(rails,offset,direction)
    try:
        image=Image.open(file)
    except FileNotFoundError:
        print("file not found")
    else:
        image_bytes=image.tobytes()
        shuffled=engine.encrypt(image_bytes)
        glitched=bytes.fromhex(shuffled)
        glitched=Image.frombytes(image.mode,image.size,glitched).rotate(180)
        name=pathlib.Path(file).stem
        glitched.save(f"glitched-{name}.png")



def unglitch(file,rails,offset,direction):
    engine=EncryptionEngine(rails,offset,direction)
    try:
        image=Image.open(file).rotate(180)
    except FileNotFoundError:
        print("file not found")
    else:
        image_bytes=image.tobytes()
        shuffled=engine.decrypt(image_bytes)
        glitched=bytes.fromhex(shuffled)
        glitched=Image.frombytes(image.mode,image.size,glitched)#.rotate(180)
        name=pathlib.Path(file).stem
        glitched.save(f"unglitched-{name}.png")

def image_to_hex_nr (file,rails,offset,direction): #havent figured the solution to undo it yet
    engine=EncryptionEngine(rails,offset,direction)
    try:
        image=Image.open(file)
    except FileNotFoundError:
        print("file not found")
    else:
        image_bytes=image.tobytes()
        shuffled=engine.encrypt(image_bytes)
        name=pathlib.Path(file).stem
        with open(f"{name}-hex.txt","w") as f:
            f.write(shuffled)
        print("file {}-hex.txt saved".format(name))

def hex_to_image_nr (file,rails,offset,direction): # as i said in image to hex
    engine=EncryptionEngine(rails,offset,direction)
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)
    with open(file,"r") as f:
        message=f.read()
    decrypted_substance= engine.decrypt(message)
    # decrypted_substance=bytes.fromhex(decrypted_substance)
    # decrypted_substance=Image.frombytes(decrypted_substance,image.mode,image.size,decrypted_substance)
    ...
    #figure out the return of the decrypt function in ts case then build the image from it
    # also think of a way to include this either by adding a new mode which sucks ass or turn off the required mode
    # and make it run directly idk dude important thing figure it out

def image_to_hex(file,rails,offset,direction):
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)
    engine=EncryptionEngine(rails,offset,direction)
    with open(file,"rb") as f:
        substance=f.read()
    encrypted_substance= engine.encrypt(substance)
    name = pathlib.Path(file).stem
    with open(f"{name}.txt","w") as f:
        f.write(encrypted_substance)



def hex_to_image(file,rails,offset,direction):
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)
    engine=EncryptionEngine(rails,offset,direction)
    with open(file,"rb") as f:
        substance=f.read()
    encrypted_substance= engine.decrypt(substance)
    encrypted_substance=bytes.fromhex(encrypted_substance)
    name=pathlib.Path(file).stem
    with open(f"{name}_b_I.png","wb") as f:
        f.write(encrypted_substance)




def sudo():
    if os.geteuid() != 0:
        sys.exit("You must have root privileges to use this script.")

