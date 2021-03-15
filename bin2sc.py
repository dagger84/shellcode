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
    out = out.decode("utf-8")

    opcodes = []
    for line in out.split("\n"):
        # if line has as line number starting it, it is code
        match = re.match(r"\s+[0-9]+:", line)
        if match:
            opcodes_raw = line.split(":")[1].strip()
            opcode = ""
            for c in opcodes_raw:
                if c in set("0123456789abcdef"):
                    opcode += c
                elif c == " " and opcode != "":
                    opcodes.append(opcode)
                    opcode = ""
                else:
                    break

    # generate output
    print("\"", end = "")
    for i, op in enumerate(opcodes):
        print("\\x{}".format(op), end="")
        # add a closing quote after 16 characters and start a new line
        if i % 16 == 15:
            print("\"")
            print("\"", end = "")
    # add a closing quote if it wasn't already added in the for-loop
    if len(opcodes) % 16 != 15:
        print("\"")

    print()
    print("[i] shellcode length: {}".format(len(opcodes)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: {} file.o\n".format(sys.argv[0]))
        sys.exit(0)

    main(sys.argv[1])
