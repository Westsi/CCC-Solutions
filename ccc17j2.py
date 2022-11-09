n = int(input())
k = int(input())
sum = n
r = n
for i in range(k):
	r = 10 * r
	sum = sum + r

print(sum)
