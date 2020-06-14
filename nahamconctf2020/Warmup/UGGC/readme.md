# UGGC
Points: 30
## Category
Warmup
## Problem Statement
```
Become the admin!
Connect here:
http://jh2i.com:50018
```
![Login page](login.jpg)
## Solution
Check 1. admin login was blocked.\
![Admin Login Blocked](admin_login.jpg)\
I tried random logins. Even tried SQL injection similar to [picoCTF2019 Irish-Name-Repo 3](https://2019game.picoctf.com/problems)\
Later when I revisited I found still logged in as last tried username.\
Then I looked at cookies of website.\
Later realised its a caeser cipher.\
Set cookie to "nqzva" for "admin" username.
![cookies](cookies.jpg)
## Flag
```
flag{H4cK_aLL_7H3_C0okI3s}
```
![Flag](flag.jpg)
