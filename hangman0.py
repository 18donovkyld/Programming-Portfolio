import math
import random

def get_words():
    words = []

    with open("words.txt") as file:
        words = file.readlines()

    for i in range(len(words)):
        words[i] = words[i][:len(words[i])-1]

    return words

def pick_word(words):
    i = random.randrange(len(words))
    return words[i]
    
def new_game(words): 
    letters = []
    word = pick_word(words)
    word_current = ''
    guesses = 6
    
    for i in range(len(word)):
        word_current += '_'
    
    return [letters, word, word_current, guesses]
    
def is_word_guessed(game):
    if game[2] == game[1]:
        return True
    return False
    
def is_game_over(game):
    if game[3] == 0:
        return True
    if is_word_guessed(game):
        return True
    return False
    
def guess_letter(game, letter):
    success = False
    for i in range(len(game[1])):
        if letter == game[1][i]:
            print "equals"
            game[2] = game[2][:i] + letter + game[2][i+1:]
            success = True

    if not success:
        game[3] -= 1
        game[0].append(letter)

    return game
    
def display_picture(game):
    if game[3] == 6:
        print """
__________
|   |
|   
|  
|   
|_________
		"""
    if game[3] == 5:
        print """
__________
|   |
|   O
|    
|   
|_________
		"""
    if game[3] == 4:
        print """
__________
|   |
|   O
|   |
|   
|_________
		"""
    if game[3] == 3:
        print """
__________
|   |
|   O
|  /|
|   
|_________
		"""
    if game[3] == 2:
        print """
__________
|   |
|   O
|  /|\\
|   
|_________
		 """
    if game[3] == 1:
        print """
__________
|   |
|   O
|  /|\\
|  / 
|_________
		"""
    if game[3] == 0:
        print """
__________
|   |
|   O
|  /|\\
|  / \\
|_________
        """
    
def display_word(game):
    pass
    
def display_guessed_letters(game):
    bank = 'Guessed Letters:'
    for i in game[0]:
        bank += ' ' + i
    print bank
    
def display_status(game):
    display_picture(game)
    display_guessed_letters(game)
    print "You have %s guesses left\n%s" % (game[3], game[2])


def main():
    words = get_words() #get long list of words
    keep_playing = 'y'
    while keep_playing == 'y':
        game = new_game(words) #get a list with the game data  list, string, int
        display_status(game)
        while not is_game_over(game):
            guess = raw_input("next guess? ")
            guess = guess.strip()
            if len(guess) > 0:
                guess = guess.lower()
                game = guess_letter(game, guess[0])
            display_status(game)

        if is_word_guessed(game):
            print "You win!"
        else:
            print "The word is:", game[1]
            print "You died."

        print "Would you like to play again? y/n: "
        keep_playing = raw_input()
    print "Good bye."
    return

if __name__ == "__main__":
    main()