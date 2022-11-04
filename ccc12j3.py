scale = int(input())

icon = [['*', 'x', '*'], [' ', 'x', 'x'], ['*', ' ', '*']]

for line in icon:
	for i in range(scale):
		o = ""
		o = o + (line[0]*scale)
		o = o + (line[1]*scale)
		o = o + (line[2]*scale)
		print(o)
		
