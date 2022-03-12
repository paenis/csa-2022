## Run Server Run

gzip stream from netcat but its really finicky for some reason (maybe endianness)
```bash
user@localhost:~$ ncat services.cyberprotection.agency 13777 &>file.out

user@localhost:~$ cat file.out | xxd
00000000: 1f8b 0800 a252 2c62 02ff 73f3 7174 b752  .....R,b..s.qt.R
00000010: c80d 732b a848 0a4d f6b5 7076 4a32 364f  ..s+.H.M..pvJ26O
00000020: cb0d 0200 1a5f 45fe 1800 0000 0a4e 6361  ....._E......Nca
00000030: 743a 2042 726f 6b65 6e20 7069 7065 2e0a  t: Broken pipe..

user@localhost:~$ binwalk -e file.out

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             gzip compressed data, maximum compression, last modified: 2022-03-12 07:58:26

user@localhost:~$ cd _file.out.extracted/

user@localhost:~/_file.out.extracted$ cat 0
FLAG: mVFpxbUcM8CBb37fmR
```
