# shellcode

Because shellcode doesn't need to be complicated.

## Compiling shellcode 101

```
nasm -f <binary type> -o <output>.o <input>.asm
ld -o <binary> <object>.o
```

### Example

1. Compile the shellcode in `shellcode.asm`.

```console
$ nasm -f elf64 -o shellcode.o shellcode.asm   # creates the object file
$ ld -o shellcode shellcode.o                  # creates an executable to test shellcode
```

2. Examine the shellcode with `objdump`.

```console
$ objdump -M intel -d shellcode.o
shellcode.o:     file format elf64-x86-64

Disassembly of section .text:

0000000000000000 <_start>:
   0:   48 31 c0                xor    rax,rax
   3:   48 89 c2                mov    rdx,rax
   6:   48 89 c6                mov    rsi,rax
   9:   48 8d 3d 04 00 00 00    lea    rdi,[rip+0x4]        # 14 <msg>
  10:   04 3b                   add    al,0x3b
  12:   0f 05                   syscall

0000000000000014 <msg>:
  14:   2f                      (bad)
  15:   62                      (bad)
  16:   69                      .byte 0x69
  17:   6e                      outs   dx,BYTE PTR ds:[rsi]
  18:   2f                      (bad)
  19:   73 68                   jae    83 <msg+0x6f>
        ...
```

3. Use the `objdump` output to create shellcode in C string format.

## References
- [Github Gist: Compiling ASM](https://gist.github.com/yellowbyte/d91da3c3b0bc3ee6d1d1ac5327b1b4b2)
- [Linux Shellcode 101: From Hell to Shell](https://axcheron.github.io/linux-shellcode-101-from-hell-to-shell/)
