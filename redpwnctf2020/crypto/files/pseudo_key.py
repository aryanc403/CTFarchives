#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def decrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x - y) % 26]
    return ctxt

ctxt = "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"
pseudo_key = "iigesssaemk"
pseudo_key = "".join(num_to_chr[chr_to_num[x]//2] for x in pseudo_key)

def recover(msk):
    key = "".join( num_to_chr[(chr_to_num[x]+13)%26] if msk&(1<<i) else x for i,x in enumerate(pseudo_key))
    print(decrypt(ctxt,key),key)

flag=0

for msk in range(1<<len(pseudo_key)):
    if msk&flag:
        continue
    recover(msk)

print(pseudo_key)