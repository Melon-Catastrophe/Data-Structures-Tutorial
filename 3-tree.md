# Tree

## Introduction | What is a Tree?

A *tree* is a collection of objects called *nodes* that point to the other objects, or nodes, of the tree. These nodes will usually point to more than one other node. See the following diagram below for clarification.

![Tree 1-1](C:\Users\k4nme\OneDrive\College\Classes\Fall 2021\CSE 212 Programming with Data Structures\Final Project\Data-Structures-Tutorial\Picture Files\Tree\tree_1-1 types.png)

![Tree 1-2](C:\Users\k4nme\OneDrive\College\Classes\Fall 2021\CSE 212 Programming with Data Structures\Final Project\Data-Structures-Tutorial\Picture Files\Tree\tree_1-2.png)

As you can see from the diagram above, trees can take on many different sizes. Let's learn about the different parts of a tree.

A node that points to other nodes is a *parent* node. The nodes that a parent node points to is called a *child* node. The beginning of a tree is the *root* node, and the end nodes, or the nodes that do not point to any other nodes, are *leaf* nodes. See the diagram below for more clarification.

![Tree 1-1](C:\Users\k4nme\OneDrive\College\Classes\Fall 2021\CSE 212 Programming with Data Structures\Final Project\Data-Structures-Tutorial\Picture Files\Tree\tree_1-1.png)

## Binary Search Trees

A *binary search tree*, or BST as I will call it in this lesson, is a tree that follows particular rules to help make retrieving data faster. Any collection of data that can be organized in a less-than/greater-than manner can receive greater performance from being organized into a tree than from being in a dynamic array. 

Each node in a Binary Search Tree can point to a maximum of two other nodes **and there are no duplicates.** The location of a node stored in a BST is based on how greater than or less than its value is to the value of the parent node. A node with a value greater than the parent node is stored in the right leaf, and a node with a value less than the parent node is stored in the left leaf.

For example, say we have a tree containing only a root node with a value of 5. If we would like to insert the value 2, it would be inserted in the left leaf, and the value 7 would be inserted into the right leaf.

![Tree 2-1](C:\Users\k4nme\OneDrive\College\Classes\Fall 2021\CSE 212 Programming with Data Structures\Final Project\Data-Structures-Tutorial\Picture Files\Tree\tree_2-1.png)

### Balanced and Unbalanced Binary Search Trees

A Binary Search Tree can be unbalanced. If parent nodes only point to leaves to their right, then we do not get any performance increase over a dynamic array. Compare the two visuals below. 

![Image of Balanced Tree](C:\Users\k4nme\OneDrive\College\Classes\Fall 2021\CSE 212 Programming with Data Structures\Final Project\Data-Structures-Tutorial\Picture Files\Tree\tree_2-3.png)

Can you guess which one has better performance?

If our tree is unbalanced, it can become necessary to restructure the elements in the tree to make it more balanced. There are many algorithms out there that can do this, but that is outside of the scope of this tutorial. The point is, the starting root node and the order that you insert into a standard binary search tree determine a binary search tree's performance as well as how sorted it is.

### Performance

The performance for retrieving elements in a binary search tree is O(log(n)). This is due to the group we have to sort through becoming smaller each time we iterate through. Inserting an element is also O(log(n)), but reorganizing an ordered tree can cost O(n) performance. 

### Binary Trees in Python

Trees are not a standard data structure in Python, so if we want to use trees, we have to either use a class that has that feature or make our own class for a binary search tree.

I am providing a BST class in [Tree Class Python File](tree_class.py) available for you to download for use in the problems below. Using this class, we are able to insert items into a BST and print them out (and also use the tree container with the *in* keyword in Python).

## Problem 1: Sorting Usernames

Using the Binary Search Tree, add usernames in an unsorted way, then use Python's `print` function to print the usernames sorted. Add them in such a way that the tree is balanced and contains 7 elements.

*Note: there is no way implemented in the class to determine if the tree is balanced. The programmer will need to evaluate that for himself. Consult the solution for a comparison.*

[Problem 1 Solution](Python Files/3-tree/tree_1_sol.py)

## Problem 2: Time Comparison

Each data type has a different algorithmic efficiency, and therefore, it will take different amounts of time to add a large number of elements to different collection types. The prompt for this problem is to record the amount of time it takes to execute a particular action on a tree and another data type.

Choose another data type besides trees. Generate a tree and the other data type with *x* number of integers. Create and implement a function to measure the time it takes to determine if a random integer exists within the two data types *x* number of times. Repeat this to gather enough data to determine algorithmic efficiency by graphing.

For example, if I chose sets, then I would make a function that makes a set with *x* number of random integers. I chose large enough *x* variables to give meaningful data. One may want to fill a table similar to the one below:

|  *x*   | Execution Time (set) | Execution Time (Tree) |
| :----: | :------------------: | :-------------------: |
| 1,000  |          ?           |           ?           |
| 5,000  |          ?           |           ?           |
| 10,000 |          ?           |           ?           |
| 15,000 |          ?           |           ?           |

After printing the time taken to perform the computations, one may use a graphing calculator to graph *x* on the x-axis and the Execution times on the y-axis. This will plot a graph revealing the type of efficiency the datatype has. You may use the [Desmos](desmos.com) website to graph this.

*Note: To find the time it takes to perform a computation, one may use the `time` library. `time.time()` will return the current time as a time object. To find computation time, one may subtract different time variables to find the time a computation took in seconds.*

[Problem 2 Solution](Python Files/3-tree/tree_2_sol.py)
