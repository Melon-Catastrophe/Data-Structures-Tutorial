# Sets

### Introduction | What is a Set?

A set is an unordered, unstructured list of elements that allows no duplicates. The elements inside of a set do not have an order. *There are also no indexes within a set. Either an element is contained within a set or it is not. **The "index" of each element being stored is dependent upon the value of each element through something called *hashing* (more on that later).** This allows for O(1) performance for adding and removing elements, as well as checking if an element is contained within a set. 

### Understanding Sets

This may be a little difficult to comprehend, so let's look at some diagrams representing sets. In the following images, we will be building a set starting with an array (or a *list*, as it is called in Python). We will imagine indexes to increase comprehension, but sets do not actually contain a real index.

![Set 1-1](Picture%20Files/Set/set_1-1.png)

The above diagram represents a set with a size of 10. The above can be good for storing numbers from 0 to 9. Now let's fill it with a few values.

![Set 1-2](Picture%20Files/Set/set_1-2.png)

In the diagram above, the rule for determining what index to put something in is dependent upon the value of the number that we are storing. This can be described as index(n) = n. **If we tried to store another 2 in, then it wouldn't be allowed.**

Naturally, we would want to store numbers in ranges other than 0 to 9, so let's change the rule to index(n) = n % 10.

![Set 1-3](Picture%20Files/Set/set_1-3.png)

So far, not much has changed. All the elements are stored in the same manner. However, now we can store more number than integers 0 to 9. Let's add a couple.

![Set 1-4](Picture%20Files/Set/set_1-4.png)

The result of the calculation 1234 % 10 is equal to 4, resulting in storing the number 1234 into the 4 spot. We can now store numbers that are quite large. Notice that they way a set stores these numbers naturally does not allow for a duplicate. If we try to store a duplicate 2, we cannot, since a 2 already occupies this space. 

You may notice a dilemma in this design, though. Only 10 numbers can be stored in this example. This is where *chaining* comes in.

Chaining is a way to store multiple values in a similar space so that you can store different values that would occupy the same index. As long as the numbers do not match, you can store a number that would normally occupy the same space as another. See the diagram below to understand how it works.

![Set 1-5](Picture%20Files/Set/set_1-5.png)

With chaining, we can store more variables than we normally could. One disadvantage of chaining in sets is that it can get unbalanced. If one index is chained a substantial amount more than others, then the set is unbalanced and can ruin our O(1) performance. When using the set data type, it is typically optimized to reduce this issue.

### Hashing

We can also store non-integer data types with a technique called *hashing*. Hashing allows us to convert some (but not all) objects to a unique integer value. This allows objects like strings to be converted to an integer, allowing us to store  it into a set. When we fetch hashed data from a set, a hashing algorithm decodes the hash so that we can view the original object. 

In Python, we are able to hash using the `hash()` method. We can also define a hash for objects of our own classes by using `__hash__()` to hash member data of the object, but that is outside the scope of this tutorial. 

![Set 2-1](Picture%20Files/Set/set_2-1.png)

Assuming the object represented above is an object that we define the hash for, it can be hashed and stored into a set.

### Using Sets in Python

To make an empty set in Python, we can use the set data type. To make a set that starts with data already inside of it, we use the curly braces.

```python
empty_set = set()
full_set = {"apple", 1, 8, 2}
number_set = {1, 2, 3, 4, 5}
```

Notice that when we print `full_set` or `number_set`, it might not print in order. Items in sets are not stored in order; they are stored in hash order. 

To add an element to the set, we can use `.add()`. To remove an element from a set (if it exists), we can use `.remove()`. We can use the `in` keyword to test if a particular element is contained in a set. To check the number of items in a set, `len()` is used.

```python
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add("apple")
my_set.remove(3)
print("Is 3 in my_set?:", 3 in my_set)
print("Values in my_set:", my_set)
print("Length of my_set is", len(my_set))
```

The print statements above will print out something similar to the following:

```
Is 3 in my_set?: False
Values in my_set: {'apple', 1, 2}
Length of my_set is 3
```

### Benefits and Detriments of Using a Set



## Problem 1: Checking for Duplicates

In this problem, we will use sets to help us write a function named `has_duplicates()` to check for duplicates within a group of data. The function should expect a list of data as a parameter and return True if there is a duplicate or False if there are no duplicates.

Since sets cannot contain duplicate values, we can simply add each value in a list into a set and compare the length of the list against the length of the set. If the two lengths are different, then there are duplicate values. 

First, we need to define a variable of type 'set' within the `has_duplicates()` function. We will call it `data_set`. The input list will be defined as `data_list`.

```python
def has_duplicates(data_list):
    data_set = set()
```

Next, each item should be added to a set so that we can compare the length of the two variables later on.

```python
for item in data_list:
    data_set.add(item)
```

Finally, we can compare the lengths of the two variables and return the appropriate values.

```python
  if len(data_set) == len(data_list):
        return False
    else:
        return True
```

[Solution to Problem 1](Python%20Files/2-set/set_1.py)

## Problem 2: Finding Values in Two Sets

This problem focuses on something called an intersection. An *intersection* is a common mathematical operation that, in programming terms, returns the values that are a part of both sets. 

![Intersection](C:\Users\k4nme\OneDrive\College\Classes\Fall 2021\CSE 212 Programming with Data Structures\Final Project\Data-Structures-Tutorial\Picture Files\Set\intersection.png)

In this problem, write a function `intersect()` that returns a set that contains the intersection of two parameters, `set1` and `set2`. 

You can use the following test cases to test your code:

```python
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
```

[Solution to Problem 2](Python%20Files/2-set/set_2.py)

Click [Next](3-tree.md) to go to the tutorial on Trees.

[Next](3-tree.md)

