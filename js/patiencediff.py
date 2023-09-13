# implement split(a, b) where a and b are lists of strings
# it returns a tuple of 4 elements: 
# common_prefix, common_suffix, remaining_a, remaining_b

# ["cat", "dog", "elephant"]
# ["cat", "giraffe", "tiger", "dog", "elephant"]

# returns

# ["cat"]
# ["dog", "elephant"]
# []
# ["giraffe", "tiger"]


# such that: 
# a == common_prefix + remaining_a + common_suffix
# b == common_prefix + remaining_b + common_suffix
# and len(common_prefix + common_suffix) is maximized


def split(a,b):

    idx1 = 0

    for idx1 in range(min(len(a), len(b))):
        if a[idx1] != b[idx1]:
            break
    else:
        idx1 += 1

    #this is the gap between the common prefix and the common suffix
    common_prefix = a[:idx1]


    a = a[idx1:]
    a.reverse()
    b = b[idx1:]
    b.reverse()

    idx2 = 0

    for idx2 in range(min(len(a), len(b))):
        if a[idx2] != b[idx2]:
            break
    else:
        idx2 += 1

    common_suffix = a[:idx2]
    common_suffix.reverse()

    remaining_a = a[idx2:]
    remaining_a.reverse()
    remaining_b = b[idx2:]
    remaining_b.reverse()


    return (common_prefix, common_suffix, remaining_a, remaining_b)



print(split(["cat", "dog", "elephant"], ["cat", "giraffe", "tiger", "dog", "elephant"]))

 

# implement pair_unique(a, b) where a and b are lists of string
# it returns None or a tuple of 2 indices which denote the positions within a and b of an element 
# which is common in both a and b, as well as unique in both a and b (meaning it only appears once, in both) 








#implement diff(a, b) which produces a diff like the following: