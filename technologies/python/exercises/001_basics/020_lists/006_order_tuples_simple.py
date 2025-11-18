# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# Define a function called 'last' that takes a single argument 'n' and returns the last element of 'n'
def last(n):
    return n[-1]

# Define a function called 'sort_list_last' that takes a list of tuples 'tuples' as input
def order_tuple(tuple_to_order: list):
    # Sort the list of tuples 'tuples' using the 'last' function as the key for sorting
    return sorted(tuple_to_order, key=last)

tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(order_tuple(tuple_to_order=tuple))
