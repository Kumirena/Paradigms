# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания.
# Можно использовать любой алгоритм сортировки.


# Bubble sort
def sort_lists_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers



# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле.
#

  def sort_lists_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers

