def cities():
    names = []
    city = input("Enter city name: ")
    while True:
        names.append(city)
        city = input("Enter city name: ")
        if city == "":
            break
        else:
            continue
    print(names)
cities()
# ACRONYM
def string():
    string = input("Enter String: ").split()
    acronym = []
    for item in string:
        acronym.append(item[0])
    print("The Acronym Is: ",".".join(acronym))
string()
# REVERSE WORDS OF STRING
def string():
    str = input("Enter String: ")
    words = str.split()
    words = words[-1::-1]
    print(" ".join(words))
string()

def cities():
    names = []
    str = input("Enter name of city: ")
    while True:
        names.append(str)
        str = input("Enter name of city: ")
        if str == "":
            break
        else:
            continue
    print(names)
cities()

def string(p):
    result = ""
    for words in p.split(" "):
        result = result + " "
        for i in words:
            if i == words[0] or i == words[-1]:
                result = result + i.upper()
            else:
                result = result + "_"
    return result
words = input("Enter any phrase: ")
print(string(words))

def string():
    str = input("Enter string: ").split()
    acronym = []
    for item in str:
        acronym.append(item[0])
    print("The Actonym is: ",".".join(acronym).upper())
string()


def sorting(n):
    size = len(n)
    for j in range(0,size):
        for i in range(0,size-1):
            if n[i] > n[i+1]:
                temp = n[i+1]
                n[i+1]= n[i]
                n[i] = temp
    return n
l = []
for i in range(5):
    data = int(input("Enter Data: "))
    l.append(data)
print("Entering list",l)
print("Sorting List",sorting(l))


def string():
    str = input("Enter String: ")
    word = str.split()
    word = word[-1::-1]
    print(" ".join(word))
string()
# SORTING!!!
def sorting(n):
    size = len(n)
    for j in range(0,size):
        for i in range(0,size-1):
            if n[i] > n[i+1]:
                temp = n[i+1]
                n[i+1] = n[i]
                n[i] = temp
    return n
l = []
for i in range(5):
    data = input("Enter Data for list: ")
    l.append(data)
print("Entering list",l)
print("Sorting list",sorting(l))