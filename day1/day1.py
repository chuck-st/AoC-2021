from day1_input import input

# def input():
#     for x in [199,200,208,210,200,207,240,269,260,263]:
#         yield x

def q1(ipt):
    count = 0
    last = 'a'
    for x in ipt:
        if last != 'a':
            if x > last:
                count += 1
        last = x
    return count

def q2(ipt):
    index = 0
    storage = []
    for x in ipt:
        storage.append([])
        storage[index].append(x)
        if index - 1 >= 0:
             storage[index - 1].append(x) 
        if index - 2 >= 0:
            storage[index - 2].append(x) 
        index += 1
    storage.pop()
    storage.pop()
    return [sum(x) for x in storage]

print(q1(q2(input())))
