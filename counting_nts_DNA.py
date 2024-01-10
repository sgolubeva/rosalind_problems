# counting DNA nucleotides problem from rosalind

# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s
#  of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s


def nt_counter(sequence: str):

    """Takes a DNA sequence as a string and counts number of each nucleotide"""

    seq_upper = sequence.upper()
    nucleotides = ("A", "C", "G", "T")
    a = 0
    c = 0
    g = 0
    t = 0 
    if any(c not in 'ACGT' for c in seq_upper):
        print('sequence passed is not a DNA sequence')
    else:
        a = sequence.count('A')
        c = sequence.count('C')
        g = sequence.count('G')
        t = sequence.count('T')
    return a, c, g, t

if __name__ == "__main__":
     # tests for nt_counter
    assert nt_counter('AAAA') == (4, 0, 0, 0)

    assert nt_counter('AAAAB') == (0,0,0,0)

    assert nt_counter('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC') == (20, 12, 17, 21)
    print('passed all tests')



