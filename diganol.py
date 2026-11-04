lim=int(input("enter the limit:"))
for row in range(1,lim+1):
	for space in range(1,row):
		print("",end="")
		print("",end=" ")
	print("*")
lim=int(input("enter the limit:"))
for row in range(1,lim+1):
	for space in range(row,lim):
		print("",end="")
		print("",end=" ")
	print("*")
