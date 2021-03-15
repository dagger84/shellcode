#!/usr/bin/env python

import re
import sys
import subprocess as sp
import shlex
from binascii import hexlify

def main(binfile):
    ctr = 1
    maxlen = 15

    cmd = "objdump -M intel -d {}".format(binfile)
    cmd = shlex.split(cmd)

    proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = proc.communicate()
    print(out)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} file.o\n".format(sys.argv[0]))
        sys.exit(0)

    main(sys.argv[1]))
