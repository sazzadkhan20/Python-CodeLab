numbers = [24,10,50]
largestNum = numbers[0]

for i in range(3):
    if largestNum < numbers[i]:
        largestNum = numbers[i]
print("Largest Number : ",largestNum)

