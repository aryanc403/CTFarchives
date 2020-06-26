# Login
Points: 148
## Category
web
## Problem Statement
I made a cool login page. I bet you can't get in!\
Site: login.2020.redpwnc.tf\
Attachment : "index.js"
## Solution
Close inspection of source reveals its a simple [sql injection](https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/)\
Vulnerability is this line.
```js
try {
        result = db.prepare(`SELECT * FROM users
            WHERE username = '${username}'
            AND password = '${password}';`).get();
    } catch (error) {
```
Username - `aryan`\
Password - `' OR 1==1;--'`
## Flag
```
flag{0bl1g4t0ry_5ql1}
```