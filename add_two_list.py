list_a = [1, 2, 4, 5]
list_b = [5, 7, 2, 5]

answer_list = []

for i in range(0, max(len(list_a), len(list_b))):
    answer_list.append(list_a[i] + list_b[i])

print(answer_list)



