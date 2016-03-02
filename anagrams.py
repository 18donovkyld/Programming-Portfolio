# anagram program to find all the combinations of characters
# to help with scrabble

# recursion

def ana(beg, end):
	if len(end) == 1:
		return [beg+end]
		
	f = []
	for i in range(len(end)):
		f += [beg+end[i]]
		f+= ana(beg+end[i], end[:i] + end[i+1:]	
	return f	

def anagrams(letters):
	dictionary = []
	try:
		dictionary_file = open("american-english.txt", "rb")
	except:
		print "Dictionary file not found"
		dictionary = None
		
	for line in dictionary_file:
		dictionary.append(line.strip())
		
	# now find all the anagrams and filter out real words
	words = ana("", letters)
	print "Number of anagram: ", len(words)
	real_words = []		
	
	for word in words:
		if len(word) > 1 and word in dictionary:
			real_words.append(word)
			
	return real_words		
	

def main():
	tiles = raw_input("Enter Tiles")
	words =anagrams(tiles)
	
	for word in words:
		print word
		
		
main()		