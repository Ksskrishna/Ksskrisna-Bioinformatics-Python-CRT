'''
write a py prog to create a customer service by adding a customer into the queue and once the customer is served he has to be rmeoved from the queue
'''
class Customer():
    def __init__(self):
        self.customer = []       
        self.served_customers = []  
    
    def cutomer_list(self, custo):
        self.customer.append(custo)
        print("customers list: ", custo)

    def served(self, cust):
        if cust in self.customer:
            self.served_customers.append(cust)
            print("served customer:", cust)
        else:
            print(f"Customer {cust} not in list")
    
    def remove(self):
        if self.served_customers:
            removed = self.served_customers.pop(0)
            print(f"Removed served customer: {removed}")
        else:
            print("No customers to be removed as they are not served")

customer = Customer()
customer.cutomer_list('customer A')
customer.cutomer_list('customer B')
customer.cutomer_list('customer C')
customer.served('customer A')
customer.served('customer B')

customer.remove()
customer.remove()

        
