s = input("ENTER PHRASE: ")
x = "aeiouAEIOU"
y = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
count1 = 0
count2 = 0
for i in s:
    if i in x:
        print(i,"its a vowel")
        count1 = count1+1
    elif i in y:
        print(i,"its a consonant")
        count2 = count2+1
print("Total no of vowels in a phrase is",count1)
print("Total no of consonant in a phrase is",count2)

print("Total alphabets",count1+count2)