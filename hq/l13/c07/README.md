## Seashells

https://google.com/search?q=how+to+run+shellcode+in+c

http://ref.x86asm.net/coder32.html

http://www.yolinux.com/TUTORIALS/GDB-Commands.html

```bash
apt-get install gcc-multilib
gcc -g main.c -o main -fno-stack-protector -z execstack -no-pie -m32
```

segfaults on call 0x2