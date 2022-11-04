num_bids = int(input())


winner = ""
winning_bid = 0
for i in range(num_bids):
	name = input()
	bid = int(input())
  # > instead of >= to ensure that first bid wins if both are the same
	if bid > winning_bid:
		winner = name
		winning_bid = bid

print(winner)
