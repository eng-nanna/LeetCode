'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_freq = {}
        for x in ransomNote:
            rans_freq[x] = rans_freq.get(x,0) + 1
            
        mag_freq = {}
        for x in magazine:
            mag_freq[x] = mag_freq.get(x,0) + 1
            
        for chr in ransomNote:
            if chr in magazine and rans_freq[chr] <= mag_freq[chr]:
                continue
            else:
                return False
        return True