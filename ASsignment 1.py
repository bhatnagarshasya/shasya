
with open("Assignment1.txt", 'r') as f:
    no_words = 0

    for line in f:
        words = line.split()
        no_words += len(words)
    
    def countOccurrence(a):
        k = {}
        for j in a:
            if j in k:
                k[j] +=1
        else:
            k[j] =1
        return k

#Q2 no of words excluding puctuation
print(no_words - len(countOccurrence(words)))