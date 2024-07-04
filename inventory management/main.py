print("You can become 2 types of users: admin or a regular user")
print("Admins can add, update, delete products and see all the products")
print("Regular users can see all the products and buy them")

class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

# Predefined users
users = [
    User('admin', 'admin_password', True),
    User('user1', 'user1_password'),
    User('user2', 'user2_password')
]

def login(username, password):
    for user in users:
        if user.username == username and user.password == password:
            return user
    return None

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

products = [
    Product(1, 'Laptop', 1200, 10),
    Product(2, 'Mouse', 20, 50),
    Product(3, 'Keyboard', 50, 30)
]

def add_product(name, price, quantity):
    new_id = len(products) + 1
    new_product = Product(new_id, name, price, quantity)
    products.append(new_product)
    return new_product
