a = int(input())
stop = a/2
b = 3
if a == 1:
	print ("yes")
elif a%2 == 0:
	print("no")
else:
	while b<= stop:
		if a%b ==0:
			print("no")
			break
		else:
			print ("yes")
