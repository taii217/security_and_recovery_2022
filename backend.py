def readFile(namefile):
    with open (namefile,'r') as readfile:
        d = readfile.read().splitlines()
    return d

def writeFile(namefile, data):
    file1 = open(namefile, "w")
    for line in data:
        file1.write(f'{line}\n')