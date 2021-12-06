def has_duplicates(data_list):
    data_set = set()

    for item in data_list:
        data_set.add(item)

    if len(data_set) == len(data_list):
        return False
    else:
        return True


# Test Cases
print("\n")

# Test 1
data = [1, 2, 3, 4, 5]
print("Test 1:", has_duplicates(data))   # Should return False

# Test 2
data = [1, 2, 3, 4, 4]
print("Test 2:", has_duplicates(data))   # Should return True

# Test 3
data = ["apple", "margarine", 52, 44, 63, -1, 0, 0] 
print("Test 3:", has_duplicates(data))  # Should return True

print("\n")