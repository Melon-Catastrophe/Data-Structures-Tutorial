from collections import deque

# We are assuming that all tickets have the same priority to simplify the problem.
tickets = deque()
tickets.append("Flickering Monitor")
tickets.append("Slow Computer")
tickets.append("Webcam not working")
tickets.append("Sound not working")
tickets.append("Microphone not working")

while len(tickets) > 0:
    print("New Ticket:", tickets[0])
    completed = input("Did you complete the ticket? (y/n): ")
    if completed == 'y':
        tickets.popleft()
    print("")   # Printing a new line to separate tickets.

print("All tickets completed!")