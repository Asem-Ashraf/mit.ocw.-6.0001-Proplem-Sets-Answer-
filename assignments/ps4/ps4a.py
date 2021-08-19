# Problem Set 4A
# Name: asem
# Collaborators: none
# Time Spent: 2:00

def get_permutations(sequence:list, word, comlist):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    for i in range(len(sequence)):
        new_sequence = sequence[:]
        del new_sequence[i]
        newword = word[:]
        newword.append(sequence[i])
        if len(sequence) == 1:
            comlist.append(''.join(newword))
            return comlist
        comlist= get_permutations(new_sequence,newword,comlist)
    return comlist

if __name__ == '__main__':
    #EXAMPLE
    example_input = "abciuغات"
    print('Input:', example_input)
    sequence=[]
    sequence[:0]=example_input
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    list=get_permutations(sequence,[],[])
    print('Actual Output:', list)
    for i in list:
        for c in list:
            if i == c:
                if list.index(i)!=list.index(c):
                    print('re')
