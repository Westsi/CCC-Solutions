# Secret instructions

inp = input()
last_direction = ""
pl = []
while inp != "99999":
	sum = int(inp[0]) + int(inp[1])
	if sum == 0:
		direction = last_direction
	elif sum % 2 == 0:
		direction = "right"
	else:
		direction = "left"

	pl.append(direction + " " + inp[2:len(inp)])
	last_direction = direction
	inp = input()

for line in pl:
	print(line)
