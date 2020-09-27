import argparse

def IsPrime(a):
	stop = a / 2
	b = 3
	if a < 0:
		print("This number isn't natural. Please, choose a number bigger than 0.")
		exit(0)
	elif a == 1:
		print ("yes")
		exit(0)
	elif a % 2 == 0:
		print("no")
		exit(0)
	else:
		while b <= stop:
			if a % b == 0:
				print("no")
				exit(0)
			else: 
				b += 2
		print("yes")

parser = argparse.ArgumentParser(description="Identify prime numbers.")
parser.add_argument('-n', help='The programm prints "yes" if the number is prime and "no" in the opposite case', action = 'store', dest = 'a', type = int)
args = parser.parse_args()
awnser = IsPrime(args.a)
