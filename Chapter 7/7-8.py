sandwich_orders = ['tuna', 'chicken', 'beef','yoyo','yoyo' 'veggie','yoyo']
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich ")
    finished_sandwiches.append(order)
print("finished sandwiches:")
for sandwich in finished_sandwiches:
    print (sandwich)