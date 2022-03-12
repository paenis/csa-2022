## Shutter Speed

steghide/seek with no password
```bash
user@localhost:~$ stegseek masai-mara-01.jpg
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "flag.rar".
[i] Extracting to "masai-mara-01.jpg.out".

user@localhost:~$ mv masai-mara-01.jpg.out extracted.rar

user@localhost:~$ 7z e extracted.rar

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
...

Everything is Ok

Size:       35
Compressed: 107
```

flag extracted:
```bash
user@localhost:~$ cat flag.txt
Welcome
The flag is hjkslPi8tyh!
```
