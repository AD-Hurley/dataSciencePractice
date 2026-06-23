
WordData={}

with open("poem.txt") as f:
    for line in f:
        tokens = line.split()
        for token in tokens:
            if token in WordData:
                WordData[token] += 1
            else:
                WordData[token] = 1

print(WordData)

wordFreq=list(WordData.values())
maxFreq=max(wordFreq)
print(maxFreq)

for word in WordData:
    if WordData[word] == maxFreq:
        print(word+" appears "+str(maxFreq)+" times\n")
