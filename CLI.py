import os,sys,argparse
from helper_functions import error_handling

def cli():
    if os.geteuid() != 0:
        sys.exit("You must have root privileges to use this script.")
    parser = argparse.ArgumentParser(
        description="ByteShatter - Multi-Engine Glitch-Art & Byte-lvl-cryptography tool",
        usage="whispershuffle2 <mode> [arguments]"
    )
    subparsers = parser.add_subparsers(dest="mode", required=True, help="choose the engine :)")
    classic=subparsers.add_parser("classic", help="used to encrypt decrypt simple strings")
    classic_args=classic.add_mutually_exclusive_group(required=True)
    classic_args.add_argument('-e',"--encrypt",nargs=4,metavar="",help='message,rails,offset,direction')
    classic_args.add_argument('-d',"--decrypt",nargs=4,metavar="",help='message,rails,offset,direction')
    shatter=subparsers.add_parser("shatter", help="used for bit lvl manipulation to encrypt and decrypt txt files")
    shatter_args=shatter.add_mutually_exclusive_group(required=True)
    shatter_args.add_argument('-ef',"--encrypt_file",nargs=4,metavar="",help='file,rails,offset,direction')
    shatter_args.add_argument('-df',"--decrypt_file",nargs=4,metavar="",help='file,rails,offset,direction')
    glitch=subparsers.add_parser("glitch", help="used for glitching jpeg or png files")
    glitch_args=glitch.add_mutually_exclusive_group(required=True)
    glitch_args.add_argument('-g',"--glitch",nargs=4,metavar="",help='img_file,rails,offset,direction')
    glitch_args.add_argument('-ug',"--unglitch",nargs=4,metavar="",help='img_file,rails,offset,direction')
    arguments = parser.parse_args()

    if arguments.mode == "classic":
        args= arguments.encrypt or arguments.decrypt
        error_handling(args[1],args[2],args[3])
        message,rails,offset,direction=args[0],int(args[1]),int(args[2]),args[3]
        if arguments.encrypt:
            print("encrypting ...")
            print(f"result: '{encrypt(message,rails,offset,direction)}'")
        elif arguments.decrypt:
            print("decrypting ...")
            print(f"result: '{decrypt(message,rails,offset,direction)}'")
    if arguments.mode=="shatter":
        args= arguments.encrypt_file or arguments.decrypt_file
        error_handling(args[1],args[2],args[3])
        file, rails, offset, direction = args[0], int(args[1]), int(args[2]), args[3]
        file_type = pathlib.Path(file).suffix
        if file_type.lower() == ".txt":
            pass
        else:
            raise NotImplementedError("File type not supported in this version")
        if arguments.encrypt_file:
            print("encrypting file ...")
            encrypt_file(file,rails,offset,direction)
            print("ready check ur directory ur using this tool in to find ur encrypted file should be obvious XD")
        elif arguments.decrypt_file:
            print("decrypting file ...")
            decrypt_file(file,rails,offset,direction)
            print("decrypted file is ready in ur directory")
    if arguments.mode=="glitch":
        args= arguments.glitch or arguments.unglitch
        error_handling(args[1], args[2], args[3])
        image, rails, offset, direction = args[0], int(args[1]), int(args[2]), args[3]
        file_type = pathlib.Path(image).suffix
        if file_type.lower() in [".jpeg",".png",".jpg"]:
            pass
        else:
            raise NotImplementedError("File type not supported in this version")
        if arguments.glitch:
            print("creating glitched image ...")
            glitch_(image,rails,offset,direction)
            print("ready in ur directory")
        elif arguments.unglitch:
            print("reversing image to its previous form ...")
            unglitch(image,rails,offset,direction)
            print("ready in ur directory")