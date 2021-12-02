from day2_input import input

# def input():
#     for x in ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']:
#         yield x

def q1(ipt):
    position = {
        'horizontal': 0,
        'depth': 0
        }
    for direction in ipt:
        x, y = direction.split()
        y = int(y)
        if x == 'forward':
            position['horizontal'] += y
        if x == 'down':
            position['depth'] += y
        if x == 'up':
            position['depth'] -= y
    
    return position

def q2(ipt):
    position = {
        'aim': 0,
        'depth': 0,
        'horizontal': 0,
        }
    for direction in ipt:
        x, y = direction.split()
        y = int(y)
        if x == 'forward':
            position['horizontal'] += y
            position['depth'] += ( y * position['aim'])
        if x == 'down':
            position['aim'] += y
        if x == 'up':
            position['aim'] -= y
    
    return position

hold = q2(input())
print(hold)
tot = hold['horizontal'] * hold['depth']
print(tot)
