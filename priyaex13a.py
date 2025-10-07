def linear_search(roll_list, target):
    for i in range(len(roll_list)):
        if roll_list[i] == target:
            return i
    return -1

def binary_search(roll_list, target):
    low = 0
    high = len(roll_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if roll_list[mid] == target:
            return mid
        elif roll_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = int(input("Enter the number of registered students: "))

registered_students = []
for i in range(n):
    roll = int(input(f"Enter roll number {i+1}: "))
    registered_students.append(roll)

roll_number = int(input("\nEnter the roll number to verify: "))

index_linear = linear_search(registered_students, roll_number)

sorted_list = sorted(registered_students)
index_binary = binary_search(sorted_list, roll_number)

print("\n--- Search Results ---")
if index_linear != -1:
    print(f"Using Linear Search: Found at position {index_linear + 1}")
else:
    print("Using Linear Search: Not Found")

if index_binary != -1:
    print(f"Using Binary Search: Found in sorted list at position {index_binary + 1}")
else:
    print("Using Binary Search tree Not found")
