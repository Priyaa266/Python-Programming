num_keys=int(input("Enter the  numberr of keys in dictionary:"))
my_list={}
keys=[]
for i in range(num_keys):
    key=input("Eter the key:")
    values=input("ENter the letters for keys{key}").split()
    my_list[key]=values
    keys.append(key)
def generate_combo(index,current):
    if index==len(keys):
        print(''.join(current))
        return
    for words in my_list[keys[index]]:
        generate_combo(index+1,current+[words])
print("/n.All combinations of letters")
generate_combo(0,[])
