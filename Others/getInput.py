word = input("enter a word: ")

re = word [::-1]

if word == re:
    print(word +" is palindrome")
else:
    print(word +" is NOT palindrome")
