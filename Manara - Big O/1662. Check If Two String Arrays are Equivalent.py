'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
'''

def arrayStringsAreEqual(word1, word2):
    '''w1 = ""
    w2 = ""
    for x in word1:
        w1 += x
    for y in word2:
        w2 += y
    
    return w1 == w2'''

    return "".join(word1) == "".join(word2)
