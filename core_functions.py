import pathlib,sys,os
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

def sudo():
    if os.geteuid() != 0:
        sys.exit("You must have root privileges to use this script.")

