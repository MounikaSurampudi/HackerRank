from collections import OrderedDict

Range = int(input())
data = OrderedDict()

for _ in range(Range):
    fields,values = input().rsplit(' ',1)
    values=int(values)

    data[fields] = data[fields]+values if fields in data else values

for i,j in data.items():
    print(i,j)
