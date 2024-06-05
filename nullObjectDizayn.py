class Customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class NullCustomer(Customer):
    def __init__(self):
        super().__init__("No Name Available")

    def get_name(self):
        return "No Name Available"

def get_customer(customer_id):
   # Simulation of data from the Customer Id-Name database
    databaseIdNameDict = {
    0: "Alice",
    1: "Bob",
    2: "Charlie",
    3: "David",
    4: "Eva",
    5: "Frank",
    6: "Grace",
    7: "Hannah",
    8: "Isaac",
    9: "Julia",
    10: "Kevin"}
    # If the customer is not found, NullCustomer is returned  
    if customer_id not in databaseIdNameDict:
        return NullCustomer()
    else:
        return Customer(databaseIdNameDict[customer_id])

# Use
customer = get_customer(14) #Returns an instance of the NullCustomer class

print(customer.get_name())

customer = get_customer(5)  #Returns an instance of the Customer class

print(customer.get_name())
