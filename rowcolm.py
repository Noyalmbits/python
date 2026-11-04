lim=int(input("enter the limit:"))
for row in range(1,lim+1):
	for space in range(1,row):
		print("",end="")
	for colm in range(1,row+1):
		print("*",end=" ")
	print()
