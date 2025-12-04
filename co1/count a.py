n=int(input("Enter the limit:"))
li=[]
c=0
for x in range(n):
    x=input("Enter a name:")
    li.append(x)
for i in li:
     for j in i:
        if 'a' in j.lower():
         c=c+1
print("The occurance of 'a' is:",c)