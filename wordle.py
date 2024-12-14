import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[0m'

with open("/usr/share/dict/words") as f:
    words = f.read().splitlines()

def choose_five_letter_word():
    choosable_word : list = []
    for word in words:
        if len(word) == 5:
            choosable_word.append(word)
    return random.choice(choosable_word).upper()

def letter_in_right_pos(right_word, letter, placement):
    if right_word[placement] == letter:
        return 1
    if letter in right_word:
        return 0
    else:
        return -1

def is_valid_word(attempt):
    return attempt.lower() in words

def play_game():
    word : str = choose_five_letter_word()
    letter_list = list(word)
    i = 0
    while True:
        attempt : str = input("attempt[" + str(i) + "]: ")
        attempt = attempt.upper()

        if len(attempt) != 5:
            print("guess must be 5 letters, silly you...")
            continue
        # if (is_valid_word(attempt) == False):
        #     #print("not a valid word, dumdum...")
        #     continue
        if attempt == word:
            print(f"{GREEN}{attempt}{RESET}")
            return 
        result : str = ""
        for j, letters in enumerate(attempt):
            rightness : int = letter_in_right_pos(letter_list, letters, j)
            if rightness == 1:  # right placement
                result += (f"{GREEN}{letters}{RESET}")

            if rightness == 0:  # right letter, wrong placement
                result += (f"{YELLOW}{letters}{RESET}")

            if rightness == -1: # wrong letter
                result += (letters)
        print(result)
        i += 1
    

if __name__ == "__main__":
    play_game()
    playing = True
    while playing:
        reset = input("would you like to play again? (y/n)")
        reset = reset.lower()
        while True:
            if reset == 'y' or reset == 'n':
                break
        if reset == 'y':
            play_game()
        if reset == 'n':
            playing = False
            print("thanks for playing!")
