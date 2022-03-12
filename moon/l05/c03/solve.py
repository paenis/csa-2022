#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

import string, zipfile

chars = string.digits


def extract_zip(filename, password):
    with zipfile.ZipFile(filename) as zFile:
        try:
            password_encoded = bytes(password.encode("utf-8"))
            zFile.extractall("/tmp", pwd=password_encoded)
            print("[+] Password Found: " + password + "\n")
            return password
        except:
            pass


stop = False

for i in chars:
    if not stop:
        for j in chars:
            if not stop:
                for k in chars:
                    pw = extract_zip("/tmp/alien-zip-2092.zip", i + k + j)
                    if pw is not None:
                        print(pw)
                        stop = True
                        break
