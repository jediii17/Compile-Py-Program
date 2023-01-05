from collections import deque

# Create a new deque
d = deque()

# Add elements to the deque
d.append(1)
d.appendleft(2)
d.extend([3, 4])
d.extendleft([5, 6])

print(d)  # deque([6, 5, 2, 1, 3, 4])


# sample 2

# Create a new deque with a max length of 3
d = deque(maxlen=3)

# Add elements to the deque
d.append(1)
d.appendleft(2)
d.append(3)
d.appendleft(4)

print(d)  # deque([4, 2, 1], maxlen=3)

# Remove elements from the deque
d.pop()
d.popleft()

print(d)  # deque([2], maxlen=3)
