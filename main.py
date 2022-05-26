# Recieve user input for anagrams
subAnagram = input('Input subject of anagram: ')
anagram = input('Input anagram: ')

# Check if a word is an anagrams 

def find_anagrams(word, word1):
    # [assignment] Add your code here
    if(word.split().sort() == word1.split().sort() and len(word) == len(word1)):
        return True
    else:
        return False   

# Print a boolean result of find_anagrams
def declareAnagram():
    print(find_anagrams(subAnagram, anagram))

declareAnagram()     





# print(find_anagrams('one'))

# aStr = 'mississippi'
# alist = []

# for letter in range(len(aStr)):
#     alist.append(aStr[letter])



# print(alist)
# print(alist.count('s'))