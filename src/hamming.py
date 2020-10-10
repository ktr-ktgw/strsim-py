

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise Exeption("error: different length")
    else:
        distance = 0
        for i, c in enumerate(s1):
            if c != s2[i]: distance += 1
        return distance
