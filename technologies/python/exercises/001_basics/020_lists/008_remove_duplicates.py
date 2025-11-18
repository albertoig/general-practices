# Write a Python program to remove duplicates from a list.
def remove_duplicates(list_with_duplicates: list) -> list:
    list_no_duplicates = []

    for number in list_with_duplicates:
        if number not in list_no_duplicates:
            list_no_duplicates.append(number)
    
    return list_no_duplicates

duplicates = [10, 5 , 6, 10 , 6, 7]

print(f'\nList with duplicates {duplicates} \nList without duplicates: {remove_duplicates(duplicates)}')
