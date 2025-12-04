cy=int(input("enter a current year:"))
fy=int(input("Enter a future year:"))
for i in range(cy,fy+1):
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i)






