print("Insert the number corresponding to the action you want to perform:")
print("\n1. Insert a new task")
print("2. Remove a task")
print("3. Show all the task")
print("4. Close the program")

scelta=0
tasks=[]
i=0;
while (scelta!=4):
    scelta=int(input("Your choice: "))
    if(scelta==1):
        strng=input("Insert task: ")
        tasks.append(strng)
    elif(scelta==2):
        if(len(tasks)==0):
            printf("No tasks")
        strng=input("Insert task tha has to be deleted: ")
        tasks.remove(strng)
    elif(scelta==3):
        if(len(tasks)==0):
            print("No task")
        else:
            print(tasks)
    elif(scelta==4):
        print("Program ended")