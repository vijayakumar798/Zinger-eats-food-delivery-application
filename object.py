class Order:
    def __init__(self, items, customer_name):
        self.items = items
        self.customer_name = customer_name

    def process_order(self):
       
        print(f"Order processed for {self.customer_name}: {self.items}")
