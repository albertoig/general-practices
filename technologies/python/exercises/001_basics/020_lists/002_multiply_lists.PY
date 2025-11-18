def multiply_list(list_to_multiply: list) -> int:
    multiply_result = 0

    for item_to_multiply in list_to_multiply:
        if multiply_result == 0:
            multiply_result = item_to_multiply
        else: 
            multiply_result = multiply_result * item_to_multiply

    return multiply_result

items_to_multiply = [1, 2, 3, 4]
print(multiply_list(list_to_multiply=items_to_multiply))