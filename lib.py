
def st1():
	adjec1 = raw_input("Type an adjective: ")
	adjec2 = raw_input("Type another adjective: ")
	tybird = raw_input("Type a tyoe if bird: ")
	room = raw_input("Type a room in a house: ")
	pastverb = raw_input("Type a verb in past tense: ")
	verb = raw_input("Type a verb: ")
	relative = raw_input("Type a relatives name: ")
	noun = raw_input("Type a noun: ")
	liquid = raw_input("Type a liquid: ")
	verb2 = raw_input("Type a verb ending in -ing: ")
	pofbod = raw_input("Type a body part: ")
	plural = raw_input("Type a plural noun: ")
	verb3 = raw_input("Type a verb ending in -ing: ")
	noun2 = raw_input("Type a noun: ")	
	
	print ("It was a %s, cold November day. I woke up to the %s smell of %s roasting \
in the %s downstairs. I %s down the stairs to see if I could help %s the dinner. \
My mom said, 'See if %s needs a fresh %s. ' So I carried a tray of glasses full of %s \
into the %s room. When I got there, I couldnt believe my %s! There were %s \
%s on the %s!" % (adjec1, adjec2, tybird, room, pastverb, verb, relative, noun, \
	liquid, verb2, pofbod, plural, verb3, noun2))
	
play_again = 'y'
while play_again == 'y':	
	st1()
	print('Do you want to play again? y/n')
	play_again = raw_input()
	

    