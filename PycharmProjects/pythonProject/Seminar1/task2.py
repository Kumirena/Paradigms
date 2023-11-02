# У вас есть список чисел, и ваша задача - отсортировать его по возрастанию.

#  декларативный стиль
lst = [3, 5, 4, 1, 2]
lst.sort()
print(lst)

#  императивный стиль
lst1 = [3, 5, 4, 1, 2]
for i in range(len(lst1)):
    for j in range(i+1, len(lst1)):
        if lst1[i] > lst1[j]:
            lst1[i], lst1[j] = lst1[j], lst1[i]

print(lst1)