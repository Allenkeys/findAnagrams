# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word, word1):
    # [assignment] Add your code here
    if(word.split().sort() == word1.split().sort() and len(word) == len(word1)):
        return True
    else:
        return False   

# print(find_anagrams('one'))

# aStr = 'mississippi'
# alist = []

# for letter in range(len(aStr)):
#     alist.append(aStr[letter])



# print(alist)
# print(alist.count('s'))

print(find_anagrams('listen', 'slite'))


