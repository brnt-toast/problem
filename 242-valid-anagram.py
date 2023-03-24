"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

def solution(s,t):
     if len(s) != len(t):
            return False

        sCounter, tCounter = {}, {}
        for i in range(len(t)):
            if s[i] not in sCounter:
                sCounter.setdefault(s[i],0)
            if t[i] not in tCounter:
                tCounter.setdefault(t[i],0)
            sCounter[s[i]] += 1
            tCounter[t[i]] += 1

        return sCounter == tCounter
