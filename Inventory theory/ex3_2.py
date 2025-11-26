from operator import index

demands = {1: 500, 2: 300, 3: 200, 4: 500, 5: 700}

h = 1
K = 1000
c = 2

cache = [-1, -1, -1, -1, -1]
indexes = [-1, -1, -1, -1, -1]


def C(d):
    if cache[d-1] != -1:
        return cache[d-1]
    if d==1:
        alternatives = [cost_order_between_days(1, 6), cost_order_between_days(1, 5) + C(5),
                   cost_order_between_days(1, 4) + C(4), cost_order_between_days(1, 3) + C(3),
                   cost_order_between_days(1, 2) + C(2)]
        minimal_cost = min(alternatives)
        cache[d-1] = minimal_cost
        indexes[d-1] = alternatives.index(minimal_cost)
        return minimal_cost
    if d==2:
        alternatives = [cost_order_between_days(2, 6), cost_order_between_days(2, 5) + C(5),
                   cost_order_between_days(2, 4) + C(4), cost_order_between_days(2, 3) + C(3)]
        minimal_cost = min(alternatives)
        cache[d-1] = minimal_cost
        indexes[d-1] = alternatives.index(minimal_cost)
        return minimal_cost

    if d==3:
        alternatives = [cost_order_between_days(3, 6), cost_order_between_days(3, 5) + C(5),
                   cost_order_between_days(3, 4) + C(4)]
        minimal_cost = min(alternatives)
        cache[d-1] = minimal_cost
        indexes[d-1] = alternatives.index(minimal_cost)
        return minimal_cost
    if d==4:
        alternatives = [cost_order_between_days(4, 6), cost_order_between_days(4, 5) + C(5)]
        minimal_cost = min(alternatives)
        cache[d-1] = minimal_cost
        indexes[d-1] = alternatives.index(minimal_cost)
        return minimal_cost
    if d==5:
        minimal_cost = cost_order_between_days(5, 6)
        cache[d-1] = minimal_cost
        indexes[d-1] = 0
        return minimal_cost
    return -1

def cost_order_between_days(d1,d2):
    order_cost = K
    holding_cost = 0
    holding_factor = 0
    for i in range(d1, d2):
        order_cost += demands[i]*c
        holding_cost += holding_factor*demands[i]
        holding_factor += 1

    return order_cost + holding_cost


print(f"Minimal cost = {C(1)} kr")
print(indexes)
print(f"Current cost = {cost_order_between_days(1, 6)} kr")
