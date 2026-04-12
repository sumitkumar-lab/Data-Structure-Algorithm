a = [1, 2, 3]
b = a
b.append(4)
print(a)   # What prints? WHY?

print(id(a))
print(id(b))
print(a is b)
b = [10,20,30]
print(id(a))
print(id(b))

c = [1, 2, 3]
d = c[:]
d.append(4)
print(c)   # What prints? WHY?
print(d)

d[0]=5
print(d)


c = [[1, 2], [3, 4]]
d = c[:]
d[0].append(99)
print(c)
"""
c[:] copied the outer list — made new sticky notes. 
But those new sticky notes still point to the same inner lists. So modifying d[0] still affects c[0]
"""

# print(d)


import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(10, 1)

model = SimpleNet()
x = [1, "hello", model]  # model is just an object like anything else
print(id(x[1]))
print(id(x[2]))  # model itself
print(id(model))  # same — list stored the address, not a copy



def make_batch(data, batch=[]):
    batch.append(data)
    return batch

print(make_batch("sample1"))
print(make_batch("sample2"))
batch = make_batch("sample1")
print(id(batch[0]))

batch = make_batch("sample2")
print(id(batch[0]))
print(id(batch[1]))