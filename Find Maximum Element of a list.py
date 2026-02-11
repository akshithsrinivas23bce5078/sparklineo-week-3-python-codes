listes = []
number = int(input("Enter the no of elements:"))
for i in range(number):
    elements = int(input("Enter the elements:"))
    listes.append(elements)
#Method 1(Using max function)
max1 = max(listes)
print("The maximum element of the above list is:", max1)
#Method 2(Using detailed method)
maximum = listes[0]
for i in listes:
    if i > maximum:
        maximum = i
print("The maximum element of the above list is:", maximum)

print("Both methods help to find maximum element in a list!!! So we can use either method to solve the problem.")
