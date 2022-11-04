# get inputs
so = input()
st = input()

# make arrays to store int values of letters
soc = []
stc = []

# loop through letters in inputs, converting to int representing unicode char
for char in so:
	if char != " ":
		soc.append(ord(char))

for char in st:
	if char != " ":
		stc.append(ord(char))

# sort lists
soc.sort()
stc.sort()

# print results
if soc == stc:
	print("Is an anagram.")
else:
	print("Is not an anagram.")
