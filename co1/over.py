numbers = input("Enter numbers: ")
nums = numbers.split()
result = []

for n in nums:
    value = int(n)
    if value > 100:
        result.append("over")
    else:
        result.append(value)

print("Final list:", result)