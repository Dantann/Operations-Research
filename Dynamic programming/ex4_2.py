import sympy
from sympy import Symbol, sqrt

p = 1.01
cost = Symbol('c')


def a(k):
    if k == 1:
        return 1
    else:
        return pow(cost, 2)/(pow(cost, 2) + p*pow(c(k-1), 2))

def c(k):
    if k > 1:
        return sqrt(pow(cost, 2) + p*pow(c(k-1), 2))
    elif k == 1:
        return cost

def u(k, x_k):
    return a(k)*x_k

def x(k, x_prev):
    return p*x_prev*(1-a(k))

constants = [c(k) for k in range(1, 12)]


cur_x = pow(10, 6)
cur_k = 12



money_spendings = []
party_account = [cur_x]

while cur_k > 0:
    money_spendings.append(u(cur_k, cur_x))
    cur_x = x(cur_k, cur_x)
    cur_k -= 1
    party_account.append(cur_x)


print(money_spendings) # Seems reasonable
print(party_account)


