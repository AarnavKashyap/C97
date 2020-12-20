intro = input("introduce yourself")
wordCount = 1
characterCount = 0

for x in intro :
    characterCount += 1
    if(x == " "):
        wordCount += 1
        
print(wordCount)
print (characterCount)
