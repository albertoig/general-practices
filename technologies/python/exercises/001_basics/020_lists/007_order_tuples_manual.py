# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def order_tuple(tuple_to_order: list):
    for i in range(1, len(tuple_to_order)):
        current = tuple_to_order[i]
        j = i - 1
        
        while j >= 0 and tuple_to_order[j][-1] > current[-1]:
            print(f'tuple: {tuple_to_order[j]} current: {current}')
            tuple_to_order[j+1] = tuple_to_order[j]
            j -= 1

        tuple_to_order[j+1] = current

    return tuple_to_order

tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(order_tuple(tuple_to_order=tuple))
