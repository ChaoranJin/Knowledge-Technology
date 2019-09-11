with open("/Users/charles/Desktop/Knowledge technology/project 1/2019S1-proj1-data/misspell.txt", "r") as file1:
    misspell = []
    lines = file1.readlines()
    for a in lines:
        misspell.append(a.strip("\n").strip('\r'))
file1.close()

with open("/Users/charles/Desktop/Knowledge technology/project 1/2019S1-proj1-data/correct.txt", "r") as file2:
    correct = []
    lines = file2.readlines()
    for b in lines:
        correct.append(b.strip("\n").strip('\r'))
file2.close

with open("/Users/charles/Desktop/Knowledge technology/project 1/2019S1-proj1-data/dict.txt", "r") as file3:
    dict = []
    lines = file3.readlines()
    for c in lines:
        dict.append(c.strip("\n").strip('\r'))
file3.close()


precisionTotal = 0
candidateTotal = 0

for n in range(len(misspell)):
    wordlist = list(misspell[n])
    maxValue = -100
    precision = 0
    value =[]
    for m in range(len(dict)):
        dictlist = list(dict[m])
        F = [([0] * (len(wordlist) + 1)) for i in range(len(dictlist) + 1)]
        for j in range(len(wordlist) + 1):
            F[0][j] = -j
        for i in range(len(dictlist) + 1):
            F[i][0] = -i
        for i in range(1, len(dictlist) + 1):
            for j in range(1, len(wordlist) + 1):
                if wordlist[j-1] == dictlist[i-1]:
                    F[i][j] = max(F[i - 1][j] - 1, F[i][j - 1] - 5, F[i - 1][j - 1] + 1)
                else:
                    F[i][j] = max(F[i - 1][j] - 1, F[i][j - 1] - 5, F[i - 1][j - 1] - 5)
        value.append(F[len(dictlist)][len(wordlist)])

    maxValue = max(value)
    candidate = []
    for a in range(len(value)):
        if value[a] == maxValue:
            candidate.append(dict[a])
    candidateTotal = candidateTotal + len(candidate)

    print (candidate, candidateTotal)

    for c in range(len(candidate)):
        if candidate[c] == correct[n]:
            precisionTotal = precisionTotal + 1

Recall = float(precisionTotal) / len(misspell)
Precison = float(precisionTotal) / candidateTotal

print ("Recall: ") + str(Recall)
print ("Precision: ") + str(Precison)