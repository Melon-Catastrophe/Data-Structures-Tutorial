# Queues

## Introduction | What is a Queue?

Imagine you are standing in line to purchase movie theater tickets. There are two people in front of you and three people behind. You notice that the first people to enter the line are the first people to leave the line. This convention is called First In, First Out (FIFO). Queues are orderly. 

When making a queue, there are a few rules that must be followed. When adding an item to the queue, it must be added to the back. When removing an item from the queue, it must be removed from the front. We also cannot normally retrieve an item in the middle of the queue. Unlike dynamic arrays, the items in the queue are typically not accessed by index (see rant below).  

In a queue, one can only add to the back of a queue and can only remove from the front of the queue. This is to follow the rules set for queues. These rules allow us to remove an item from the front of a queue in O(1) time.

### Performance of a Queue 

The performance for adding a value to the back of a queue and removing from the front of the queue is O(1). Classes used to make queues in Python automatically keep track of the size of the queue. This enables the size of a queue to be recalled in O(1) time. Typically, accessing an item in the middle of a queue is impossible, but in Python, it can be accomplished in O(n) time, although *accessing a queue item by index is extremely discouraged*. 

In addition, one can add and remove from the left of a queue in O(1) time, whereas adding and removing an item from a Python list (or a dynamic array) occurs in O(n) time.

### Queues in Python

To make a queue in python, one should always use the *deque* class. This offers a huge performance increase over using dynamic arrays with a custom class. 

To use *deque*, we first need to import it from the *collections* class. We can then declare a queue by calling deque on a list.

~~~python
from collections import deque
q = deque(["option1", "option2", "option3"])
~~~

When learning how to use queues with the deque class, one must be careful when appending and removing elements. You can add and remove items on the left of the queue with `.appendleft()` and `.popleft()`. You can add and remove items on the right of the queue with `.append()` and `.pop()`. It is up to the programmer to decide if the left or right side of the queue represents the front, but in our case, we will be identifying the left side as the "front".

Let's see how you would use a queue with example code.

```python
q = deque()
q.append(1)
q.append(2)
q.append(3)

print(q)
```

This will print `deque([1, 2, 3])`. Let's now remove from the front of the queue.

```python
print("Front of queue item:", q.popleft())
print("Queue:", q)
```

When we run this code, we get:

```
Front of queue item: 1
Queue: deque([2, 3])
```

If we stick with popping on the left (or "front") of the queue and appending on the right (or "back") of the queue, then we can reliably use it as a queue. Sticking to these rules is what keeps our deque object acting as a queue object.

### Problem 1: Prioritizing First in Line

Imagine that *x* number of people preordered an item. There are only *y* number of items available for preorder. In this problem, the objective will be to use the `deque` class to make a queue of people and print out who in the queue gets an item based on the order of the queue. 

First, let's import the deque class and initialize a queue.

~~~python
from collections import deque

people_q = deque()
~~~

This is meant to be a queue of people, so we can add a few people to our queue. Let's also initialize an integer variable representing the number of items that we have available for preorder.

~~~python
people_q = deque()
people_q.append("Nathan")	# Nathan was first in line
people_q.append("Barbara")	# Barbara was second in line
people_q.append("Joe")		# Joe was third in line

num_items = 2
~~~

Now we need to identify how we will print out the people that get the items. The first `num_items` people in line get an item, and the rest of the people in the line will not get that item.

We can write a couple of simple while loops to accomplish this. Remember, if we use `.append()` to add someone to the end of the line, then we need to use `.popleft()` instead of `.pop()` to get someone from the beginning of the line.

```python
while num_items > 0 and len(people_q) > 0:
    winner = people_q.popleft()
    print(winner, "gets a limited item!")
    num_items -= 1

while len(people_q) > 0:
    loser = people_q.popleft()
    print(loser, "does not get a limited item...")
```

When we run this, the output we get is as follows:

~~~
Nathan gets a limited item!
Barbara gets a limited item!
Joe does not get a limited item...
~~~

[Solution to Problem 1](Python%20Files/1-queue/queue_1.py)

### Problem 2: Solving IT Tickets

Pretend that you are an IT Technician, and you are solving tickets in the order that they were received in. Write a program that, given a queue of tickets, will give the user with a ticket and ask if they solved the ticket. If they have, proceed to display the next ticket in the queue.

Instead of making a custom ticket object, just use a string that contains what the title of the ticket might be. For example, one item in a queue might be "Flickering Monitor".

[Solution to Problem 2](Python Files/1-queue/queue_2.py)



Feel free to read the rant below on accessing indexes in Python queues, or click [Next](2-set.md) to go to the next page.

[Next](2-set.md)

#### Rant About Indexes

As of Python 3.5, you can access an item within an instance of deque by index, but the performance is slowed to O(n). Since the whole objective of a First In, First Out Data Structure is to access items by the ends, if you need to access an item in the middle of a queue, it may be worthwhile to reconsider what datatype you should use.

Furthermore, not all programming languages support accessing queues by an index. Python is an oddity in this respect. If indexes are required, consider using an alternate data structure. 