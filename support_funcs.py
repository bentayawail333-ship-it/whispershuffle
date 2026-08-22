from itertools import cycle


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