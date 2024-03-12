phrase = input("Enter phrase: ")
def vowels(phrase):
    vowels = 'aeiouAEIOU'
    for i in range(len(phrase)):
        if phrase[i] in vowels:
            print(phrase[i],'found at',i)
    return vowels
vowels(phrase)