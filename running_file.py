#!/usr/bin/env python3

from CLI import cli
from core_functions import sudo

def main ():
    sudo()
    cli()

if __name__ == '__main__':
    main()
