# coding test algorithm

## Data Structure

1. Stack/Queue
> it's better to use `deque` on efficient 

- FIFO, Rotate problem

### insert
```javascript
from collections import deque

# append(): pushing data (right-side)
dq = deque()
dq.append(1)
dq.append(2)
print(dq) # result = deque([1,2])

# appendleft(): pushing data (left-side)
dq.appendleft(3)
print(dq) # result = deque([3,1,2])

# extend(): iterate the param -> append()
dq.extend([4,5,6])
print(dq) # result = deque([3,1,2,4,5,6])

# extendleft(): iterate the param -> appendleft()
dq.extend([7,8,9])
print(dq) # result = deque([9,8,7,3,1,2,4,5,6])
```

### remove
```
# remove(): delete by value
print(dq) # result = deque([1,2,3])
dq.remove(2) 
print(dq) # result = deque([1,3])

# pop() : delete from the back
dq = [1,2,3]
dq.pop() # [1,2]

# popleft() : delete from the front
dq = [1,2,3]
dq.popleft() # [2,3]
```

### rotate
```
dq = [1,2,3,4,5]

dq.rotate(1) # [5,1,2,3,4] positive: moving back element to the front 

dq.rotate(-1) # [1,2,3,4,5] negative:  moving front element to the back

```
