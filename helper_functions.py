import pathlib,sys,os,tqdm
from itertools import cycle
from PIL import Image
from encryption_engine import EncryptionEngine


def error_handling(rails,offset,direction):
    try:
        rails=int(rails)
        offset=int(offset)
    except ValueError:
        raise ValueError("rails and offset parameters must be integers")

    if direction not in ["down","up"] :
        raise NotImplementedError("Direction must be up or down")

def get_path(r):
    path = []
    for i in range(r): path.append(i)
    n = r - 1
    for i in range(n - 1): n = n - 1; path.append(n)
    rail_path = cycle(path)
    it = iter(rail_path)
    return it

def skipper(it,r,offset,direction):
    for _ in range(offset):
        next(it)
    if direction == "down" or (direction == "up" and offset % (r - 1) == 0):
        pass
    if direction == "up" and offset % (r - 1) != 0:
        for _ in range(2 * (r - (offset + 1))):
            next(it)


def encrypt_file(file,rails,offset,direction):
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)

    with open(file,"r") as f:
        message=f.read()
    encrypted_substance= encrypt(message,rails,offset,direction)
    name=file.replace(".txt","_e.txt")
    with open(name,"w") as f:
        f.write(encrypted_substance)

def decrypt_file(file,rails,offset,direction):
    if not os.path.isfile(file):
        print("file not found"); sys.exit(1)

    with open(file,"r") as f:
        message=f.read()
    decrypted_substance= decrypt(message,rails,offset,direction)
    if file.endswith("_e.txt"):
        name=file.replace("_e.txt","_d.txt")
    else:
        name=file.replace(".txt","_d.txt")
    with open(name,"w") as f:
        f.write(decrypted_substance)


def glitch_(file,rails,offset,direction):
    try:
        image=Image.open(file)
    except FileNotFoundError:
        print("file not found")
    else:
        image_bytes=image.tobytes()
        shuffled=encrypt(image_bytes,rails,offset,direction)
        glitched=bytes.fromhex(shuffled)
        glitched=Image.frombytes(image.mode,image.size,glitched).rotate(180)
        name=pathlib.Path(file).stem
        glitched.save(f"glitched-{name}.png")



def unglitch(file,rails,offset,direction):
    try:
        image=Image.open(file).rotate(180)
    except FileNotFoundError:
        print("file not found")
    else:
        image_bytes=image.tobytes()
        shuffled=decrypt(image_bytes,rails,offset,direction)
        glitched=bytes.fromhex(shuffled)
        glitched=Image.frombytes(image.mode,image.size,glitched)#.rotate(180)
        name=pathlib.Path(file).stem
        glitched.save(f"unglitched-{name}.png")

#encrypt:
# tqdm(message, desc="Progress:", unit="bit", mininterval=0.1)
#decrypt:
#tqdm(range(len(message)), desc="Progress:", unit="bit", mininterval=0.1)
