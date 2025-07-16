i = int(input("Enter the number: "))
i2 = int(input("Enter the power in the range of 1 to 10: "))
if i2 == 1:
    print("The answer is",i)
elif i2 == 2:
    print(i*i)
elif i2 == 3:
    print(i*i*i)
elif i2 == 4:
    print(i*i*i*i)
elif i2 == 5:
    print(i*i*i*i*i)
elif i2 == 6:
    print(i*i*i*i*i*i)
elif i2 == 7:
    print(i*i*i*i*i*i*i)
elif i2 == 8:
    print(i*i*i*i*i*i*i*i)
elif i2 == 9:
    print(i*i*i*i*i*i*i*i*i)
elif i2 == 10:
    print(i*i*i*i*i*i*i*i*i*i)
elif i2 > 10:
    print("Sry this program cant go more than the power of ten")
else:
    print("INVALID INPUT!!")