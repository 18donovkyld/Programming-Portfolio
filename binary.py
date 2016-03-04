import random
import time

def main():
	minNum = 0
	maxNum = 0

	while True:
		minNum = int(raw_input("Enter minimum: "))
		maxNum = int(raw_input("Enter maximum: "))

		if maxNum <= minNum:
			print "Max must be more"
		elif minNum < 1:
			print "Min must be greater than 0"
		elif minNum > 1000:
			print "Min must be less than 1001"
		elif maxNum < 1:
			print "Max must be greater than 0"
		elif maxNum > 1000:
			print "Max must be less than 1001"
		else:
			break

	guess = 0
	guessCount = 0
	while True:
		guessCount += 1
		guess = int(minNum + (maxNum-minNum)/2)
		answer = raw_input("Is %s (> = <) ? " % guess)

		if answer == ">":
			maxNum = guess-1
		elif answer == "<":
			minNum = guess+1
		else:
			break

		if (minNum == maxNum):
			guess = minNum
			break

	print "Your number is %s!" % guess
	print "It took %s guesses!" % guessCount




if __name__ == "__main__":
	main()