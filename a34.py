# Assignment 34:

# Write a python function, encrypt_sentence() which accepts a message and encrypts it based on rules given below and 
# returns the encrypted message.
# Words at odd position -> Reverse It
# Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order 
# should not change

# Note:
# 1. Assume that the sentence would begin with a word and there will be only a single space between the words.
# 2. Perform case sensitive string operations wherever necessary.
# Also write the pytest test cases to test the program.

# Sample Input 
# the sun rises in the east 

# Expected Output
# eht snu sesir ni eht stea


def encrypt_sentence(s):
    vowels = "aeiouAEIOU"
    words = s.split()
    for i in range(len(words)):
        if i%2==0:
            words[i] = words[i][::-1]
        else:
            consonants = [char for char in words[i] if char not in vowels]
            vowels_in_word = [char for char in words[i] if char in vowels]
            words[i] = ''.join(consonants + vowels_in_word)

    return ' '.join(words)
      



if __name__ == "__main__":
    s = "the sun rises in the east"
    ans = encrypt_sentence(s)
    print(ans)