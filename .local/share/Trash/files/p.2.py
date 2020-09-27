import argparse

def IsPrime(a):
	stop = a/2
	b = 3
	if a == 1:
		print ("yes")
		exit(0)
	elif a%2 == 0:
		print("no")
		exit(0)
	else:
		while b <= stop:
			if a % b == 0:
				print("no")
				exit(0)
			else: 
				b+= 2
		print("yes")

parser = argparse.ArgumentParser(description="Identify primaly numbers")
parser.add_argument('-n', help='The programm print "yes" is the number is primar and "no" in the opposite case', action = 'store', dest = 'a', type = int)
args = parser.parse_args()
awnser = IsPrime(args.a)


