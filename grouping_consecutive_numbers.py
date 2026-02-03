"""
This is a list of number problem.
Here we finds groupes between consecutive numbers
"""


def group_consecutive(numbers):
    if not numbers:
        return[]
    numbers = sorted(set(numbers))

    result=[]
    start=numbers[0]
    end=numbers[0]

    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else :
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = end = num
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    return result

numbers = [10, 11, 12, 15, 17, 18, 19, 20, 22]
print("\nInput numbers:", numbers)
print("Grouped ranges:", group_consecutive(numbers))