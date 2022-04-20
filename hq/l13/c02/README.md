## Bypass

abusing a vulnerability in [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup) to bypass a login prompt (CVE-2016-4484)

given a host and port, connect with netcat or similar:
```bash
user@localhost:~$ ncat services.cyberprotection.agency 13880
Password:
>
```

we're given a password prompt, which can be bypassed by simply holding enter until we see `Welcome <uninitialized>.`

type `?` or `help` to see commands, and we can run the `flag` command for the flag: `ZhSX9onhPC7y1LTqhE`
