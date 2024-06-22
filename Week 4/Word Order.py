from collections import OrderedDict

n = int(input())
ordered_input_dict = OrderedDict()

for i in range(n):
    val = input()
    if val not in ordered_input_dict.keys():
        ordered_input_dict[val] = 1
    else:
        ordered_input_dict[val] += 1
        
print(len(ordered_input_dict))
# print(' '.join(str(val) for val in ordered_input_dict.values()))
print(' '.join(map(str, ordered_input_dict.values())))
