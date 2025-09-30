import random;

decimaal = 3

print(decimaal)

lengte = random.uniform(3, 8)
print(round(lengte, 1))

q_last = random.uniform(1, 10)
print(round(q_last, 1))

moment = (1/8) * q_last * lengte ** 2
print(round(moment, decimaal))