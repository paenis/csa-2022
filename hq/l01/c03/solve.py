import string

nums = [[20, 8, 5], [19, 5, 3, 18, 5, 20], [23, 15, 18, 4], [9, 19], [23, 8, 5, 5, 12]]

msg = []
for group in nums:
	decoded = ''
	for num in group:
		char = string.ascii_lowercase[num-1] # index offset
		decoded += char
	
	msg.append(decoded)

msg = ' '.join(msg)
print(msg)