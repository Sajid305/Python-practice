def count(s):
    counted = {}
    for car in s:
        counted[car] = s.count(car)
    return counted
print(count('shajid'))