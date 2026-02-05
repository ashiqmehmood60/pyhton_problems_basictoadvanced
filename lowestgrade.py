n = int(input("Enter number of students: "))
arr = []
sec = []
i=0
for _ in range(n):
    name = input("enter the name :")
    grades = float(input(" enter grade :"))
    arr.append([name, grades])
print("Student details are :", arr)
arr.sort(key=lambda x: x[1])
print(arr)
for i in range(n-1):
    if (arr[i][1]!=arr[i+1][1]):
        if(i+1<n):
            sec_grade=arr[i+1][1]
            for j in range(n):
                if(arr[j][1]==sec_grade):
                    sec.append(arr[j][0])
            break
        
    else:
        i+=1
sec.sort()
result = '\n'.join(sec)
print( result)

