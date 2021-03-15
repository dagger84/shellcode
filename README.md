# shellcode

Because shellcode doesn't need to be complicated.

## Compiling shellcode 101

```bash
nasm -f <binary type> -o <output>.o <input>.asm
ld -o <binary> <object>.o
```

## References
- [Github Gist: Compiling ASM](https://gist.github.com/yellowbyte/d91da3c3b0bc3ee6d1d1ac5327b1b4b2)
- [Linux Shellcode 101: From Hell to Shell](https://axcheron.github.io/linux-shellcode-101-from-hell-to-shell/)
