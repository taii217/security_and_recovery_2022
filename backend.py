import hashlib
import random
import sys

def readFile(namefile):
    with open (namefile,'r') as readfile:
        d = readfile.read().splitlines()
    return d

def writeFile(namefile, data):
    file1 = open(namefile, "w")
    for line in data:
        file1.write(f'{line}\n')


def hash(key):
    return hashlib.md5(bytes(key,'utf-8')).hexdigest()

def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None






