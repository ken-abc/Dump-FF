
def ReadDump(DumpD):
    fd = b''
    with open(DumpD,'rb+') as ff:
        for i in range(16):
            for i in range(4):
                if i == 3:
                    ff.read(6)
                    fg = ff.read(4)
                    ff.read(6)
                    fd = fd + b'\xFF\xFF\xFF\xFF\xFF\xFF' + fg + b'\xFF\xFF\xFF\xFF\xFF\xFF'
                else:
                    fd = fd + ff.read(16)
        return fd

def WriteDump(fd,DumpP): 
    with open(DumpP,'wb+') as ff:
        ff.write(fd)
        print("write FFFdump is YES!")

def mainl():
    DumpD = '555.dump'
    DumpP = '555fff.dump'
    fd = ReadDump(DumpD)
    WriteDump(ReadDump(DumpD),DumpP)

if __name__ == '__main__':
    mainl()