# The game of pig 
			
	import random
import time

def run(playerNumber, points):
	print

	pointsEarned = 0

	print "Player %s's turn! (%s points)" % (playerNumber, points)

	while True:
		roll = random.randrange(1, 7)

		print "You rolled a %s!" % roll

		if roll == 1:
			pointsEarned = 0
			break
		else:
			pointsEarned += roll

		answer = raw_input("Keep rolling? (y/n) ")
		if answer == "n":
			break

	raw_input("You won %s points! " % pointsEarned)

	return pointsEarned

def main():
	random.seed(time.time())

	points = [0, 0]

	playerNumber = 1

	while True:
		points[playerNumber-1] += run(playerNumber, points[playerNumber-1])

		if points[playerNumber-1] >= 100:
			print "\nPlayer %s wins!\n" % playerNumber
			break

		if playerNumber == 1:
			playerNumber = 2
		else:
			playerNumber = 1

if __name__ == "__main__":
	main()
	