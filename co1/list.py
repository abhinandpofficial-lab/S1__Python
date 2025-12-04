from anyio import value

number = [14,-5,3,6,-2,1,0]
PN = [i for i in number if i>0]
print("Positive numbers are:",PN)
N = int(input("Enter a number:"))
sq = [i ** 2 for i in range(1,N+1)]
print("square root of",N,"numbers are :",sq)
word="aeroplane"
vowels = [char for char in word if char.lower() in 'aeiou']
print("The word is:",word)
print("Vowels in word:",vowels)
print("The word is:",word)
OV = [ord(ch) for ch in word]
print("Ordinal Values are:",OV)



































































