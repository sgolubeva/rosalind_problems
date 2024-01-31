# Given two strings s
#  and t
# , t
#  is a substring of s
#  if t
#  is contained as a contiguous collection of symbols in s
#  (as a result, t
#  must be no longer than s
# ).

# The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
#  of s
#  is denoted by s[i]
# .

# A substring of s
#  can be represented as s[j:k]
# , where j
#  and k
#  represent the starting and ending positions of the substring in s
# ; for example, if s
#  = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]
#  = "UGCU".

# The location of a substring s[j:k]
#  is its beginning position j
# ; note that t
#  will have multiple locations in s
#  if it occurs more than once as a substring of s
#  (see the Sample below).

# Given: Two DNA strings s
#  and t
#  (each of length at most 1 kbp).

# Return: All locations of t
#  as a substring of s

def find_motif(s,t):
    mot_pos = []
    for i in range(len(s)-len(t)+1):
        motif = s[i:len(t)+i]
        print(f'{motif}')
        if motif == t:
            mot_pos.append(i+1)
    return mot_pos

if __name__ == "__main__":
    #res = find_motif('GATATATGCATATACTT', 'ATAT')
    #res1 = find_motif('AAAAAAAAA', 'AA')
    #res1 = find_motif('AUGCUUCAGAAAGGUCUUACG', 'U')
    res1 = find_motif('ATGATCTAGCTACCGATTAGCTACATAGCTACGTTTTTAGCTACTAGCTACGAAACTAGCTACTAGCTACCATTAGCTACTCTAGCTACAATTGTTGGGGTAGCTACTAGCTACTAGCTACCCCTAGCTACTACATATAGCTACGGCGATAGCTACCGGTAGCTACCCAATAGCTACCTAGCTACTAGCTACGTAGCTACTTAGCTACGGATTTAGCTACATAGCTACTCCTCATAGCTACTACCTTAGCTACCCTAGCTACTATAGCTACTTAGCTACTAGCTACAGGAGGGTTAGCTACATTAGCTACCTAGCTACGTCACGCTTAGCTACCATGTGTAGCTACGTAGCTACTAGCTACAAGCATAGCTACATTGGGCCTTTAGCTACTCTAGCTACTAGCTACAATAGCTACATTAGCTACTATAGCTACGTTAGCTACCGTAGCTACATGTAGCTACTAGCTACTAGCTACACTAGCTACGTAGCTACTATGTTTAGCTACTTAGCTACTAGCTACGTTCAGTAGCTACTAGCTACTAGCTACAGATAGCTACGTAGCTACCAGGTAGCTACAATTAGCTACGCGAGTAGCTACGATAGCTACCCACTAGCTACCTAGCTACGCTAGCTACATACCCGTAGCTACCGGTGGTAGCTACTAGCTACACCCTATAGCTACTAGCTACGCCGAATAGCTACTAGCTACAACCTACTAGCTACCGATTGGCACTAGCTACCATAGCTACGTGACTTAGCTACCTAGCTACTAGCTACTAGCTACTAGGCTAGCTACCTTAGCTACTTCTAGCTACTAGCTACAGCCTAGCTACTAGCTACATCGGATAGCTACCGGATAGCTACGTGTAGCTACTCTATAGCTACTAGCTACTAGCTACGATGGTAGCTACTTAGCTACTAGCTACTAGCTACCATTAGCTACTAGCTACGTTAGCTACCGCTAGCTACCAGCTAGCTAC', 'TAGCTACTA')
    print(res1)