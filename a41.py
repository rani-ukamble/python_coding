# Assignment 41:

# Write a python program that accepts a text and displays a string which contains the word with the largest frequency in the 
# text and the frequency itself separated by a space.

# Rules:
# 1. The word should have the largest frequency.
# 2. In case multiple words have the same frequency, then choose the word that has the maximum length.

# Assumptions:
# 1. The text has no special characters other than space.
# 2. The text would begin with a word and there will be only a single space between the words.
# Perform case insensitive string comparisons wherever necessary.

# Sample Input                                                                Expected Output

# "Work like you do not need money love like you have never                   like 3
# been hurt and dance like no one is watching"

# "Courage is not the absence of fear but rather the judgement that           fear 2
# something else is more important than fear"

from collections import Counter

def max_freq_word(s):
    s = s.split()
    word_freq = Counter(s)

    max_word = ""
    max_freq = 0
    for word, freq in word_freq.items():
        if (freq > max_freq) or (freq == max_freq and len(word)>len(max_word)):
            max_word = word
            max_freq = freq

    return max_word, max_freq



if __name__ == "__main__":
    s1 = input("Enter s1: ")
    word, freq = max_freq_word(s1)
    print(f"{word } {freq}")

