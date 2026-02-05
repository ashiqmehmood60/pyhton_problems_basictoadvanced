n= int(input("enter the number of inputs : "))
i=0
task={}
while i<n:
    task[i]= input("enter the task : ")
    i+=1
p=int(input("enter the position to be deleted : "))
if p in task:
    task.pop(p)
else:
    print("invalid position")
    
print("updated tasks are : ",task)