def count_long_string(s: str) -> int:
    substring = set()
    left = 0
    max_count = 0

    for right in range(len(s)):
        while s[right] in substring:
            substring.remove(s[left])
            left += 1

        substring.add(s[right])
        max_count = max(max_count, right - left + 1)
        print(f'substring: {substring} right: {right} left:{left} max_count: {max_count}')
    return max_count

print(count_long_string('pwwkew'))
