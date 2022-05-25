# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True

word = input("Enter a word: ")
def find_anagrams(word):
    # [assignment] Add your code here
    anagram = word[::-1]
    if word.title() == anagram.title():
        return True
    else:
        return False

print (find_anagrams(word))

