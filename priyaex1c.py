def get_combinations(lst,index,current):
    if current:
        print(current)
    for i in range(index,len(lst)):
        get_combinations(lst,i+1,current+[lst[i]])
elements=input("Enter the list elements seperated by space:").split()
print("All the possible combinations:")
get_combinations(elements,0,[])
