num=int(input("Enter the number of elements:"))
tup_list=[]
for i in range(num):
    ele=input("Enter the elements:")
    tuple_ele=tuple(map(int,ele.split()))
    tup_list.append(tuple_ele)
result=list(map(sum,tup_list))
print("Sum of the elements: ",result)
