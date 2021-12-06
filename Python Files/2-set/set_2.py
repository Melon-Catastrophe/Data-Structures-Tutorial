def intersect(set1, set2):
    intersect_set = set()
    
    for item in set1:
        if item in set2:
            intersect_set.add(item)

    return intersect_set


# Test Cases Below
print('\n')

# Test 1
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}
print("Problem 1:", intersect(set1, set2))  # Should return set()

# Test 2
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Problem 1:", intersect(set1, set2))  # {3}

# Test 3
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5}
print("Problem 1:", intersect(set1, set2))  # {1, 2, 3, 4, 5}

# Test 4
set1 = {"apple", "banana", "orange"}
set2 = {"kiwi", "banana", "orange", "melon", "grapefruit", "lemon"}
print("Problem 1:", intersect(set1, set2))  # {"banana", "orange"}

print("\n")