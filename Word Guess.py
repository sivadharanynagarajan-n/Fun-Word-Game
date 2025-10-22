import random
print("!Welcome To The Word Guess Game!")
print("Now You,re Word To Guess Is")
def game():
    bank = ["salvation", "colorful", "barrel", "determine", "cotton", "ridge", "fat", "category", "curve"]
    word = random.choice(bank)
    attempt = 10
    space = ['_'] * len(word)
    while attempt > 0:
        print("Current Word: ", ' '.join(space))
        guess = input("Yor're Guess: ")
        if guess in word:
            for i in range(0, len(word)):
                if word[i] == guess:
                    space[i] = guess
            print("Great Guess!")
            print()
        else:
            attempt -=1
            print("Sorry That Letter Is Not In This Word")
            print(f"You Have {attempt} Attempts Left!")
            print()
        if '_' not in space:
            print("Yes! The Word Is ", word)
            print("Congratlations! You Won The Game!")
            break
    print("Sorry! You're Attempts Are Over")
    next = input("Do You Want The Next Word, [Y]es or [N]o ? ")
    if next == 'Y' or next == 'y':
        print("You're Next Word Is")
        game()
    elif next == 'N' or next == 'n':
        print("Bye")
        return
    else:
        print("That Was Not a Valid Answer!")
        next = input("Press 'Y' if Yes Or 'N' for No: ")
        if next == 'Y' or next == 'y':
            print("You're Next Word Is")
            game()
        else:
            print("Bye")
            return
game()