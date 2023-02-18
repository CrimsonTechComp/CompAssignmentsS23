class Company:
    def __init__(self, name:str, sales="", products={}, employees=[]):
        self.name = name
        self.sales = sales
        self.products = products
        self.employees = employees

    def add_product(self, prod_name:str, prod_price:float):
        self.products[prod_name] = prod_price
        self.sales += str([prod_name, prod_price]) # site says sales is a string of a product,
                            # which I took to mean a datatype that inclues its name and price

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name:str, company:Company, role=1):
        self.name = name
        self.company = company
        self.role = role

def test():
    # better to have more test cases should be added for products and sales but left as is
    # for optional assignment
    gs = Company('GameStop')
    mario = Employee('Mario', gs)
    gs.add_employee(mario)
    gs.add_product("PS5",749.99)
    assert gs.name == 'GameStop'
    assert gs.employees
    assert mario != Employee('Mario', gs, 10)
    print("Success!")

if __name__ == "__main__":
    test()