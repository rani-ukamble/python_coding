# Assignment 37:

# Write python function,sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent 
# as SMS and returns the abbreviated sentence.
# Rules are as follows:
# a. Spaces are to be retained as is
# b. Each word should be encoded separately
#  If a word has only vowels then retain the word as is
#  If a word has a consonant (at least 1) then retain only those consonants

# Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
# Sample Input Expected Output
# I love Python==> I lv Pythn
# MSD says I love cricket and tennis too ==> MSD sys I lv crckt nd tnns t
# I will not repeat mistakes ==> I wll nt rpt mstks


def sms_encoding(s):
    vowels = "aeiouAEIOU"
    l = s.split()
    ans = []

    for word in l:
        # If the word contains only vowels, keep it as is
        if all(letter in vowels for letter in word ):
            ans.append(word)
        else:
            # Remove vowels if the word has consonants
            encode = ''.join([letter for letter in word if letter not in vowels])
            ans.append(encode)

    return ' '.join(ans)





def sms_encoding_detailed(s):
    vowels = "aeiouAEIOU"
    l = s.split()
    ans = []

    for word in l:
        # If the word contains only vowels, keep it as is
        isVowel = True
        for letter in word:
            if letter not in vowels:
                isVowel = False
                break
        if isVowel:
            ans.append(word) 
        else:
            encode = ""
            for letter in word:
                if letter not in vowels:
                    encode += letter
            ans.append(encode)
    return ' '.join(ans)



if __name__ == "__main__":
    s = "I love Python"
    print(sms_encoding(s))
    print(sms_encoding_detailed(s))

