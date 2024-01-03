def duplicate(l1):
    seen = set()
    for number in l1:
        if number in seen:
            return number
        seen.add(number)
    return None

l1 = [1, 2, 3, 3, 2, 1, 3]
result = duplicate(l1)
print(result)