def count(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] +=1
        else:
            counts[x] =1
    return counts
