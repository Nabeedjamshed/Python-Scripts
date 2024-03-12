import random as rd

computer_choice = ['Nabeed', 'Talha', 'Awwab', 'Abyaz', 'Karim', 'Saad', 'Affan', 'Anus', 'Hamza']

choices = rd.choice(computer_choice) 
tries = len(choices) + 2
result = ["_"] * len(choices)

wrong_ans = ["Wrong guess! The hangman's head has been drawn.", 
             "Wrong guess! The hangman's body has been drawn.", 
             "Not quite! The hangman's first arm has been drawn.", 
             "Oh dear, another incorrect guess! The hangman's second arm has been drawn.", 
             "Incorrect guess! The hangman's first leg has been drawn.", 
             "Oops! The hangman's second leg has been drawn.", 
             "Game over! The hangman's been completely drawn. Better luck next time."]

def my_generator():
    for i in wrong_ans:
        yield i
gen = my_generator()
print()
print("***************Let's play Hangman Game! *********************")
print()

while True:
    start = input("Player 1: I've picked a word. Can you guess it? (Y/N): ")
    if start == "Y":
        print()
        print("Great! \n","Let's test your word-guessing skills")
        print()
        print(f"|| You have {tries + 3} chances ||")
        for j in range(tries):
            begin = input("Enter a letter: ")

            if begin in choices:
                occurrences = []
                for i, letter in enumerate(choices):
                    if letter == begin:
                        occurrences.append(i)
                # occurrences = [i for i, letter in enumerate(choices) if letter == begin]

                for k in occurrences:
                    result[k] = begin  
                print("".join(result))

                if "_" not in result:  
                    print("Congratulations, You Win!!!")
                    break

            else:
                print("Incorrect guess.")
                print(next(gen))
        else:
            print(wrong_ans[6])
        break
    elif start == "N":
        print("Thank You")
        break