words=input("Enter words separated by space:").split()
ll=len(max(words, key=len))
print("Length of longest word:",ll)