class RECTANGLE:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
            return self.length * self.breadth
    def perimeter(self):
            return 2*(self.length + self.breadth)
len1=int(input("enter the length1:"))
br1=int(input("enter the breadth1"))
rec1=RECTANGLE(len1,br1)
print("Area of rectangle 1:",rec1.area())
print("Perimeter of rectangle 1:",rec1.perimeter())
len2 = int(input("enter the length2:"))
br2 = int(input("enter the breadth2"))
rec2 = RECTANGLE(len2,br2)
print("Area of rectangle 2:", rec2.area())
print("Perimeter of rectangle 2:", rec2.perimeter())
area1=rec1.area()
area2 = rec2.area()
if area1 > area2:
    print("Area of rectangle 1 is higher")
elif area1 == area2:
    print("Area is equal")
else:
    print("Area of rectangle 2 is higher")




