from getpass import getpass

print("This is a word guessing game!")
print("It consists of two players: Player 1 (P1) and Player 2 (P2)")
print("The first player will choose the word")
print("The second player will attempt to guess the word\n")

# How this code is meant to be used:
'''This is a random word game. But, as you may have noticed,
    the answer pops up on the shell. This is because this game
    is for making a functional word game for two players to play.
    Player 1 will run this code, read the directions, and enter
    a word. The code will do the figuring out for them. Player 1
    then reads what my code has done (saying the length of the word)
    and then inputs Player 2's guess. If player 2 gets the word wrong,
    player 2 is presented with the option of a hint. Player 1 types
    the choice in then presents the hints.'''


def random_word():  # randomWord game function
    continue_game = ""  # Used to decide whether to loop the game or not
    while continue_game != "no":
        secret_word = ""  # word P1 chooses
        while int(len(secret_word)) <= 5:
            # Make the word 6 letters or longer
            secret_word = getpass("P1, input your secret word!: ")
            if int(len(secret_word)) <= 5:
                print("Pl, your word is too easy! "
                      "Make it longer! (Length of 6 or above)")
            else:
                print("Nice choice, P1!")

        # Setting some variables
        secret_word = secret_word.lower()
        word_len = int(len(secret_word))  # Used for the length of the word
        guess = ""
        guess_count = 0
        #  The longer the word, the better the hint
        divide = int(word_len // 1.5)

        while guess != secret_word:
            print("P1 --> P2: The length of the word is", word_len)
            guess = input("P1 --> P2: P2, enter your guess: ")
            guess = guess.lower()
            guess_count += 1

            if guess != secret_word:
                print("P1 --> P2: Your guess was wrong")
                hint = input("P1 --> P2: Would you like a hint? "
                             "Yes or no? (Yes/No): ")
                hint = hint.lower()
                if hint == "yes":
                    if guess in secret_word:
                        print("P1 --> P2: The word you inputted is "
                              "in the secret word. Congrats!")
                    else:
                        print("P1 --> P2: The word you inputted is "
                              "NOT in the secret word")

                    print("P1 --> P2: The word starts "
                          "with the letters ", secret_word[:2])
                    print("P1 --> P2: The word ends "
                          "with the letters", secret_word[divide:])
                else:
                    print("P1: Ok, guess again")
            else:
                print("Good guess...")  # Player 2 has won
        print("Congratulations Player 2, "
              "you guessed Player 1's word!")
        continue_game = input("P1 and P2, "
                              "would you like to play again? Yes or No?: ")
        continue_game = continue_game.lower()
    # Basically what I'm doing is making a game where player 1 decides a word
    # for player 2. Player 2 has to guess the word.
    # They have the option to ask for hints or keep trying to guess it.


if __name__ == "__main__":
    '''This is a function, which allows other people to 
    input this in their own code and utilise it or 
    manipulate it easily to their code.'''
    random_word()
