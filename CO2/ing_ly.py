word= input("Enter a word:")
if word.endswith("ing"):
    word = word + "ly"
else:
    word=word + "ing"
print("modified word is :",word)