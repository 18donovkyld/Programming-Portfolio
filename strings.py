# Changing a word to pig latin

while True:
	word = raw_input("Enter a word to translate: ")

	vowels = "aeiouyAEIOUY"

	vpos = 0

	for i in range(len(word)):
		if word[i] in vowels: 
			vpos = i
			break

	print word[vpos:] + word[:vpos] + "ay"	
	
		