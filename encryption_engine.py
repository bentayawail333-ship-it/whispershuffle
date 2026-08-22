from tqdm import tqdm
from support_funcs import *

class EncryptionEngine:
    def __init__(self,rails:int,offset:int,direction:str):
        self.rails = rails
        self.offset = offset
        self.direction = direction

    def encrypt(self,message) -> str :
        if isinstance(message, str):
            message = message.encode("utf-8")

        message = "".join(f"{byte:08b}" for byte in message)
        if len(message) <= self.rails or self.rails <= 1:
            raw = bytearray(int(message[i:i + 8], 2) for i in range(0, len(message), 8))
            return raw.hex()
        rails = [[] for _ in range(self.rails)]
        it = get_path(self.rails)
        if self.offset % (2 * (self.rails - 1)) != 0:
            skipper(it, self.rails, self.offset, self.direction)

        for letter in tqdm(message, desc="Progress:", unit="bit", mininterval=0.1) :
            rails[next(it)].append(letter)
        encrypted_bits = "".join("".join(rail) for rail in rails)[::-1]
        encrypted_message = bytearray(int(encrypted_bits[i:i + 8], 2) for i in range(0, len(encrypted_bits), 8))
        return encrypted_message.hex()

    def decrypt(self,message) -> str :
        type_message = message
        if isinstance(message, str):
            message = bytes.fromhex(message)

        message = "".join(f"{byte:08b}" for byte in message)

        if len(message) <= self.rails or self.rails <= 1:
            decrypted_bits = bytearray(int(message[i:i + 8], 2) for i in range(0, len(message), 8))
            decrypted_message = decrypted_bits.decode("utf-8")
            return decrypted_message

        message = message[::-1]
        rails = [[] for _ in range(self.rails)]
        it = get_path(self.rails)
        rail_indexes = [index for index in range(self.rails)]
        letters_in_rail = {index: 0 for index in rail_indexes}
        if self.offset % (2 * (self.rails - 1)) != 0:
            skipper(it, self.rails, self.offset, self.direction)

        for letter in message:
            letters_in_rail[next(it)] += 1

        temp_index = 0
        for index, number in letters_in_rail.items():
            rails[index] = list(message[temp_index:temp_index + number])
            temp_index += number

        it = get_path(self.rails)
        if self.offset % (2 * (self.rails - 1)) != 0:
            skipper(it, self.rails, self.offset, self.direction)

        decrypted_bits_list = []
        rail_pointers = [0] * self.rails

        for _ in tqdm(range(len(message)), desc="Progress:", unit="bit", mininterval=0.1):
            rail_indx : int = next(it)
            decrypted_bits_list.append(rails[rail_indx][rail_pointers[rail_indx]])
            rail_pointers[rail_indx] += 1

        decrypted_bits = "".join(decrypted_bits_list)
        decrypted_message = bytearray(int(decrypted_bits[i:i + 8], 2) for i in range(0, len(decrypted_bits), 8))
        if isinstance(type_message, str):
            decrypted_message = decrypted_message.decode("utf-8")
            return decrypted_message
        else:
            return decrypted_message.hex()