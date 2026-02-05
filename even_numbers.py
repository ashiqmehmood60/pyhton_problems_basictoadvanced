n = int(input("Enter a number: "))
print("even numbers---")
for i in range(n):
    if i%2==0:
        print(i, sep = " , ", end = " ")
    else:
        print(end = " ")