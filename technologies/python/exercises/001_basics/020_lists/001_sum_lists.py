def sum_list_items(items: list) -> int:
    sum = 0

    for item in items:
        sum += item

    return sum



list_of_numbers = [2, 3, 5, 10]

print(sum_list_items(items=list_of_numbers))