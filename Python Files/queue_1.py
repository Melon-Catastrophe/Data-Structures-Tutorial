from collections import deque

# Making a queue of people. The order of the line is Nathan, Barbara, and Joe.
people_q = deque()
people_q.append("Nathan")
people_q.append("Barbara")
people_q.append("Joe")

# We will allow the first people in line to get an item before we run out of items.
num_items = 2
while num_items > 0 and len(people_q) > 0:
    winner = people_q.popleft()
    print(winner, "gets a limited item!")
    num_items -= 1

while len(people_q) > 0:
    loser = people_q.popleft()
    print(loser, "does not get a limited item...")
    