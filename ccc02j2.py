# AmeriCanadian

# consonant list
cons = "BCDFGHJKLMNPQRSTVWXZ"

# inf loop
while True:
  # get input
	word = input()
  # check for break kw
	if word == "quit!":
		break
   # check that less than 64 chars long
	if len(word) > 64:
		continue
   # process and print
	if len(word) > 4:
		wo = word[len(word) - 2:len(word)] == "or"
		tl = word[len(word) - 3]
		if wo and tl.upper() in cons:
			word = word[0:len(word) - 2] + "our"
	print(word)
