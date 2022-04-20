import base64, string

with open('temp','r') as f:
	strings = [line.strip() for line in f.readlines()]

target = ''
for s in strings:
	print(decoded := base64.b64decode(s).decode())
	if all(char in string.hexdigits for char in decoded):
		print('found')
		target = decoded
		break

print(target.lower()) # wtf????