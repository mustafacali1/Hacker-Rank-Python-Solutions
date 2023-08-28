class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add(self, item: Item):
        self.items.append(item)
    
    def total(self) -> int:
        total_price = sum(item.price for item in self.items)
        return total_price
    
    def __len__(self):
        return len(self.items)


n = int(input().strip())  
items = []
for _ in range(n):
    name, price = input().strip().split()
    items.append(Item(name, int(price)))

q = int(input().strip())  
cart = ShoppingCart()
for _ in range(q):
    method = input().strip()
    if method == "total":
        print(cart.total())
    elif method.startswith("add"):
        _, item_name = method.split()
        for item in items:
            if item.name == item_name:
                cart.add(item)
                break
    elif method == "len":
        print(len(cart))
