start=int(input("enter the starting range:"))
end=int(input("enter the ending range:"))
for num in range(max(start,1000),min(end,9999)+1):
	digits=str(num)
	if all(int(digit)%2==0 for digit in digits):
		root=int(num**0.5)
		if(root*root==num):
			print(num)
