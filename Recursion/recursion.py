s = 'abcde'


def reverse(s):
    if len(s) == 1:
        return s[0]
    return reverse(s[1:len(s)]) + s[0]


# print(reverse(s))
a = [1, 2, 3, 4, 5]


def sum(a):
    if len(a) == 1:
        return a[0]
    return a[0] + sum(a[1:len(a)])

# print(sum(a))


s = 'axbxcxd'


def countx(s):
    # base case
    if len(s) == 1:
        if s[0] == 'x':
            return 1
        else:
            return 0

    if s[0] == 'x':
        return 1 + countx(s[1:len(s)])
    else:
        return countx(s[1:len(s)])


# print(countx(s))

def staircase(n):
    # basecase
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n-1) + staircase(n-2) + staircase(n-3)


n = 12
# print(staircase(n))


def anagram(s):
    # Base case: if the string is only one character,​
    #return an array containing just a single-character string:
    if len(s) == 1:
        return s[0]
    collection = []
    # Find all anagrams of the substring from the second character until
    # the end. For example, if the string is "abcd", the substring is "bcd",
    substrings = anagram(s[1:len(s)])

    for x in substrings:
        #loop from 0 to one index past the end of the string:
        for i in range(0,len(x)+1):
            copy = list(x)
            #Insert the first character of our string into the copy list and append to the collection  
            copy.insert(i,s[0])
            collection.append(copy)
    return collection


s = 'ab'
result = anagram(s)
for x in result:
    print(x)
