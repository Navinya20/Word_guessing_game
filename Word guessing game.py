import random

def play_game():
    name = input("What is your name? ")
    print("Good Luck ! ", name)

    words = ['rainbow', 'computer', 'science', 'programming',
              'python', 'mathematics', 'player', 'condition',
              'reverse', 'water', 'board', 'geeks']

    word = random.choice(words)
    word_length = len(word)
    guesses = ''
    turns = 12

    while turns > 0:
        failed = 0
        print("\nThe word is: ", end=" ")
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        if failed == 0:
            print("\nYou Win")
            print("The word is: ", word)
            break
        print("\nYou have", turns, "more guesses")
        guess = input("guess a character: ")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            if turns == 0:
                print("You Loose")

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()

play_game()
