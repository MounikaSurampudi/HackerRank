from collections import deque

n = int(input())
output_deque = deque()

for i in range(n):
    input_val = input()
        
    if 'appendleft' in input_val:
        output_deque.appendleft(input_val.split()[1])
    elif 'append' in input_val:
        output_deque.append(input_val.split()[1])
    elif 'popleft' in input_val:
        output_deque.popleft()
    elif 'pop' in input_val:
        output_deque.pop()
        
print(' '.join(output_deque))
