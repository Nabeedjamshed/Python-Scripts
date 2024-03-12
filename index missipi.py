def index(word, letter):
	return [i for i in range(len(word)) if word[i] == letter]
print(index('mississippi','s'))
print(index('mississippi','i'))
print(index('mississippi','a'))
