class Store:
    def __init__(self):
        self.products = {'A': {'name': 'Pen', 'price': 10}, 'B': {'name': 'Bud', 'price': 15}, 'C': {'name': 'Eraser', 'price': 20}}

    def display_menu(self):
        print("\nProduct Menu:")
        for code, product_info in self.products.items():
            print(f"{code}: {product_info['name']} - ₹{product_info['price']}")

    def generate_bill(self, quantities):
        total_amount = 0
        print("\nBill:")
        for code, quantity in quantities.items():
            if code in self.products:
                product_info = self.products[code]
                item_total = quantity * product_info['price']
                total_amount += item_total
                print(f"{product_info['name']} ({quantity} units) - ₹{item_total}")
        print("\nTotal Amount: ₹{:.2f}".format(total_amount))   #searched how to...

store = Store()
store.display_menu()
quantities = {}
for code in store.products:
    quantity = int(input(f"Enter quantity for {store.products[code]['name']} ({code}): "))
    quantities[code] = quantity

store.generate_bill(quantities)
