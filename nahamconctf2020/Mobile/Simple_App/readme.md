# Simple App
Points: 50
## Category
Mobile
## Problem Statement
```
Here's a simple Android app. Can you get the flag?
Download the file below.
```
Attachment : "simple-app.apk"
## Solution
```
unzip simple-app.apk
grep -ir "flag{"
vim classes.dex
:?flag{
```
## Flag
```
flag{3asY_4ndr0id_r3vers1ng}
```
