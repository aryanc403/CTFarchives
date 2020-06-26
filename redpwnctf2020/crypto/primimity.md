# Primimity
Points: 450
## Category
Crypto
## Problem Statement
People claim that RSA with two 1024-bit primes is secure. But I trust no one. That's why I use three 1024-bit primes.\
I even created my own prime generator to be extra cautious!
Attachment : "file"
## Solution
Again RSA.\
This time N, e, and cipher text of flag along with random prime generator used to generate 3 prime factors of N was given to us.\
I first looked at [factordb](http://www.factordb.com/) for prime factors but it didnt helped.\

Later doing close inspection of source code I found only one prime factor is random. Author forgot to reinitialize `i` using `getRandomNBitInteger(1024)`. No of prime factors between `r` and `p` is atmax 512.\
<details>
<summary>Random no generator used to generate factors.</summary>
```py
def prime_gen():
    i = getRandomNBitInteger(1024)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    p = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    q = find_next_prime(i)
    d = getRandomNBitInteger(8)
    for _ in range(d):
        i = find_next_prime(i)
    r = find_next_prime(i)
    return (p,q,r)
```
</details>
With some approximations one can conclude that absolute difference between prime factors is around D=1000,000.\
Finding prime factors is now easy. Just find cuberoot of N and then all numbers between cbrt(N)-D and cbrt(N)+D.\

Files - [primimity_factors.py](files/primimity_factors.py) and [rsa_decrypt.py](files/rsa_decrypt.py)
## Flag
```
flag{pr1m3_pr0x1m1ty_c4n_b3_v3ry_d4ng3r0u5}
```
