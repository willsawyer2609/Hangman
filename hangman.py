# secret_word = list(input("Enter a word: ").lower())
secret_word = list("secret")
redacted = ["_"]*len(secret_word)

badguess = 0
letters = []
status = "in progess"

def hangman(secret_word, redacted, badguess, letters):
    """ Asks player to guess a letter of the word.

    parameters
    ----------
    secret_word (str): word for the player to guess.
    """
    empty = ["______ ", "| ", "| ", "| ", "| ", "|_____ "]
    stages = ["______ ", "|  | ", "|  0 ", "| /|\ ", "| / \ ", "|_____ "]
    print(f"Guess the word:{" ".join(redacted)}\n{"\n".join(stages[:badguess] + empty[badguess:])}\n")
    letter = input("Enter a letter: ").lower()
    if letter in letters:
        print(f"You already tried '{letter}'. Guess a different letter next time!\n\n")
        return redacted, badguess, letters
    elif letter in secret_word:
        for index, char in enumerate(secret_word):
            if char == letter:
                redacted[index] = secret_word[index]
        print(f"Good guess! '{letter}' is in the word.\n\n")
    else:
        badguess += 1
        print(f"Bad guess! '{letter}' is not in the word.\n\n")
    letters.append(letter)
    return redacted, badguess, letters

while status != "finished":
    redacted, badguess, letters = hangman(secret_word, redacted, badguess, letters)
    if redacted == secret_word:
        status = "finished"
        print(f"You win!\nThe word was {"".join(redacted)}!")
    if badguess == len(stages):
        status = "finished"
        print(f"Game over. The word was '{"".join(secret_word)}'.")
