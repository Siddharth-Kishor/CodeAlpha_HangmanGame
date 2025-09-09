import random

words = ["superior", "judgement", "resilience", "whimsical", "benevolent"]
states = {6 : r'''  +---+
  |   |
      |
      |
      |
      |
=========''', 5 : r'''  +---+
  |   |
  O   |
      |
      |
      |
=========''', 4 : r'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 3 : r'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 2 : r'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 1 : r'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 0 : r'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''}
win = r"""
                                    $$\      $$\ $$$$$$\ $$\   $$\ $$\ 
                                    $$ | $\  $$ |\_$$  _|$$$\  $$ |$$ |
$$\   $$\  $$$$$$\  $$\   $$\       $$ |$$$\ $$ |  $$ |  $$$$\ $$ |$$ |
$$ |  $$ |$$  __$$\ $$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ |$$ |
$$ |  $$ |$$ /  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ |\__|
$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ |    
\$$$$$$$ |\$$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ |$$\ 
 \____$$ | \______/  \______/       \__/     \__|\______|\__|  \__|\__|
$$\   $$ |                                                             
\$$$$$$  |                                                             
 \______/                                                              
 """
lose = r"""
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████  ▐██▌ 
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀  ▐██▌ 
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███    ▐██▌ 
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄  ▓██▒ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒ ▒▄▄  
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ░▀▀▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░  ░ 
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░       ░ 
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░ ░    
 ░ ░                                                                 
 """


def game():
    lives = 6
    current = random.randrange(0, len(words))
    word = words[current]
    letters = set(word)
    guesses = random.sample(list(letters), lives)
    print('*' * 100)
    while lives > 0:
        print(states[lives])
        print(f"Lives Left : {lives}")
        print("Current Word : ", end = '')
        for i in word:
            if i not in guesses:
                print(i.upper(), end = ' ')
            else:
                print('_', end = ' ')
        print()
        guess = input("Enter your Guess : ")
        if guess in guesses:
            print("Correct Guess!")
            guesses.remove(guess)
            if len(guesses) == 0:
                break
        else:
            print("Wrong Guess!")
            lives -= 1
        print('*' * 100)
    if (lives > 0):
        print('*' * 100)
        print("The Word was", word.upper(), "(You guessed it!)")
        print(f"\n{win}\n")
    else:
        print(states[lives])
        print("The Word was", word.upper(), "(You couldn't guess it.)")
        print(f"\n{lose}\n")
    
def main():
    print('*' * 100)
    print("\n\t\t\t\t   Welcome to Hangman! \n\t\t\tYou have 6 lives to guess the current word!\n")
    game()
    print("Game Ended.")

if __name__ == "__main__":
    main()