

class User:
    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = password
        self.is_admin = is_admin

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

def update_product(product_id, name, price, quantity):
    for product in products:
        if product.id == product_id:
            product.name = name
            product.price = price
            product.quantity = quantity
            return product
    return None

def delete_product(product_id):
    for i, product in enumerate(products):
        if product.id == product_id:
            del products[i]
            return True
    return False

def get_product_by_id(product_id):
    for product in products:
        if product.id == product_id:
            return product
    return None

def list_products():
    return products[:]

class Order:
    def __init__(self, id, user, products):
        self.id = id
        self.user = user
        self.products = products

orders = []
next_order_id = 1

def place_order(user, product_ids):
    global next_order_id
    products_ordered = [get_product_by_id(pid) for pid in product_ids if get_product_by_id(pid)]
    if products_ordered:
        new_order = Order(next_order_id, user, products_ordered)
        orders.append(new_order)
        next_order_id += 1
        return new_order
    return None

def list_orders():
    return orders[:]

def generate_inventory_report():
    report = []
    for product in products:
        report.append(f"Product: {product.name}, Quantity: {product.quantity}")
    return report

def main():
    print("Welcome to the Inventory Management System")
    print("Please login to continue.")

    logged_in_user = None
    while not logged_in_user:
        username = input("Username: ")
        password = input("Password: ")
        logged_in_user = login(username, password)
        if not logged_in_user:
            print("Invalid username or password. Please try again.")

    print(f"Logged in as {logged_in_user.username}")

    if logged_in_user.is_admin:
        print("You are logged in as an admin.")
    else:
        print("You are logged in as a regular user.")

    while True:
        print("\nMenu:")
        print("1. List Products")
        if logged_in_user.is_admin:
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
        print("5. Place Order")
        print("6. List Orders")
        print("7. Generate Inventory Report")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nProducts:")
            for product in list_products():
                print(f"{product.id}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

        elif choice == '2' and logged_in_user.is_admin:
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            new_product = add_product(name, price, quantity)
            print(f"Product added: {new_product.name}")

        elif choice == '3' and logged_in_user.is_admin:
            product_id = int(input("Enter product ID to update: "))
            product = get_product_by_id(product_id)
            if product:
                name = input("Enter updated product name: ")
                price = float(input("Enter updated product price: "))
                quantity = int(input("Enter updated product quantity: "))
                updated_product = update_product(product_id, name, price, quantity)
                if updated_product:
                    print(f"Product updated: {updated_product.name}")
                else:
                    print("Product not found.")
            else:
                print("Product not found.")

        elif choice == '4' and logged_in_user.is_admin:
            product_id = int(input("Enter product ID to delete: "))
            if delete_product(product_id):
                print("Product deleted.")
            else:
                print("Product not found.")

        elif choice == '5':
            product_ids = []
            while True:
                product_id = int(input("Enter product ID to order (0 to finish): "))
                if product_id == 0:
                    break
                product = get_product_by_id(product_id)
                if product:
                    product_ids.append(product_id)
                else:
                    print("Product not found.")

            if product_ids:
                placed_order = place_order(logged_in_user.username, product_ids)
                if placed_order:
                    print(f"Order placed with ID: {placed_order.id}")

        elif choice == '6':
            print("\nOrders:")
            for order in list_orders():
                print(f"Order ID: {order.id}, User: {order.user}, Products: {[p.name for p in order.products]}")

        elif choice == '7':
            print("\nInventory Report:")
            report = generate_inventory_report()
            for line in report:
                print(line)

        elif choice == '8':
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
