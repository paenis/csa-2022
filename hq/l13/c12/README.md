## Trial by File

can figure out offset of flag malloc (?)

![image](https://user-images.githubusercontent.com/46578974/164866068-2a39c27b-e7a0-4210-a423-3ee910ceaa82.png)

password input is vulnerable to buffer overflow; overflowed bytes are multiplied by 0x1d (4 byte unsigned word, so mod result by 0xffffffff), added to the malloc pointer, and then called as a pointer

![image](https://user-images.githubusercontent.com/46578974/164866215-1be784ee-52c4-4e5a-8d3e-1813466b2648.png)

entering the correct password does nothing

![image](https://user-images.githubusercontent.com/46578974/164866748-5d313a7b-b7f5-40e3-9838-0fd73826ba5a.png)

process will also exit if ptrace is called on it (has workarounds)

![image](https://user-images.githubusercontent.com/46578974/164867075-b8eb15d0-81f6-4711-92e9-2694d1680b17.png)
