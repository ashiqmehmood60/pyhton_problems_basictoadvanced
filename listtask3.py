# A program that eliminates duplicate entries from a list while preserving the original order.

n = int(input("Enter the number of inputs: "))
i = 0
task = {}
unique_tasks = {}
while i<n:
    task[i]= input("Enter the task: ")
    i += 1
for key in task:
    if task[key] not in unique_tasks.values():
        unique_tasks[len(unique_tasks)] = task[key]
else :
    print("No duplicates found.")
print("Updated tasks are: ", unique_tasks)
