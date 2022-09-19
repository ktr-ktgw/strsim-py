from math import floor
from collections import defaultdict


def jaro_similarity(s1: str, s2: str) -> float:
    if s1 == s2:
        return 1.0
    max_dist = floor(max(len(s1),len(s2))/2) -1
    
    # m is the number of matching characters
    m = 0
    match_s1 = defaultdict(lambda: False)
    match_s2 = defaultdict(lambda: False)
    for i in range(len(s1)):
        for j in range(max(0, i - max_dist), min(len(s2), i + max_dist + 1)):
            if s1[i] == s2[j]:
                match_s1[i] = True
                match_s2[j] = True
                m += 1
                break
    
    if m == 0:
        return 0.0
    
    # t is half the number of transpositions
    t = 0
    pos = 0
    for i in range(len(s1)): 
        if match_s1[i]:
            while not match_s2[pos]:
                pos += 1
            if s1[i] != s2[pos]:
                pos += 1
                t += 1
    t //= 2
    return (m/len(s1) + m/len(s2) + (m-t+1)/m) / 3.0
