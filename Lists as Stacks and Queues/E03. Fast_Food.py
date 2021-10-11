from collections import deque

qty_food = int(input())
qty_orders = deque(map(int, input().split()))

print(max(qty_orders))

while qty_orders:
    current_order = qty_orders[0]
    if current_order > qty_food:
        break
    else:
        qty_food -= current_order
        qty_orders.popleft()
if qty_orders:
    print(f'Orders left: {" ".join(map(str, qty_orders))}')
else:
    print('Orders complete')

