def check_empty_list(list_to_check: list) -> bool:
    if not list_to_check:
        return True
    return False

empty_list = None
empty_list_2 = []
not_empty_list = [ 1 ]

print(f'\n List empty_list is empty? {check_empty_list(list_to_check=empty_list)}')
print(f'\n List empty_list_2 is empty? {check_empty_list(list_to_check=empty_list_2)}')
print(f'\n List not_empty_list is empty? {check_empty_list(list_to_check=not_empty_list)}')