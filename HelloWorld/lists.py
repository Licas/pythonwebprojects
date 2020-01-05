simple_list = [1,444,23,51,239,-1]

max = simple_list[0]
for item in simple_list:
    if item > max:
        max = item

print(f"Max is: {max}")

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0].append(123)
matrix[1].insert(2,456)
matrix[1].remove(5)

eight_is_there = matrix[2].index(8)
print("8 idx is ",eight_is_there)
popped =matrix[2].pop()
print("popped",popped)
matrix[2].clear()
print(matrix)

another_list = [2,35,6,6,20,39]
copyOf = another_list.copy()
print(f"Count of 6: {another_list.count(6)}")
copyOf.sort()
print("Sorted: ", copyOf)
copyOf.reverse()
print("Sorted and reversed: ", copyOf)