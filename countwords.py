intro=input("Enter your introduction:")
charCount=0
wordCount=1
for i in intro:
    charCount+=1
    if(i==" "):
        wordCount+=1

print(charCount)
print(wordCount)
