class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
       self.assortment = []
       self.product_list = []
       self.income = 0

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if self.assortment == []:
           self.assortment.append({'type' : product.type, 'name' : product.name, 'price' : product.price*1.3, 'amount' : amount})
           self.product_list.append({'type' : product.type, 'name' : product.name, 'price' : product.price*1.3})
        else:
           if {'type' : product.type, 'name' : product.name, 'price' : product.price*1.3} in self.product_list:
              self.assortment[self.product_list.index({'type' : product.type, 'name' : product.name, 'price' : product.price*1.3})]['amount'] += amount
           else:
              self.assortment.append({'type': product.type, 'name': product.name, 'price': product.price * 1.3,'amount': amount})
              self.product_list.append({'type': product.type, 'name': product.name, 'price': product.price * 1.3})
        return self.assortment[self.product_list.index({'type' : product.type, 'name' : product.name, 'price' : product.price*1.3})]

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type != "name" and identifier_type != "type":
            raise ValueError("Invalid identifier")
        for i in range(len(self.assortment)):
            if identifier_type == 'type' and self.assortment[i]['type'] == identifier or identifier_type == 'name' and self.assortment[i]['name'] == identifier:
                self.assortment[i]['price'] = self.assortment[i]['price']*(1-percent/100)
        return self.assortment

    def sell(self, product_name, amount):
        if product_name not in [self.assortment[i]['name'] for i in range(len(self.assortment))]:
            raise ValueError("There are no product in Store")
        for i in range(len(self.assortment)):
            if self.assortment[i]['name'] == product_name:
                self.assortment[i]['amount'] = self.assortment[i]['amount'] - amount
                self.income = self.income + amount * self.assortment[i]['price']
        return self.assortment

    def get_income(self):
        return self.income / 1.3 * 0.3  #if it is profit of Store (without original cost of goods)

    def get_all_products(self):
        return self.assortment

    def get_product_info(self, product_name):
        if product_name not in [self.assortment[i]['name'] for i in range(len(self.assortment))]:
            raise ValueError("There are no product in Store")
        for i in range(len(self.assortment)):
            if self.assortment[i]['name'] == product_name:
                product_info = (product_name, self.assortment[i]['amount'])
        return product_info





p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Sport', 'Football T-Shirt', 100)

s = ProductStore()

print(s.add(p, 10))
print(s.add(p2, 300))
print(s.add(p3, 50))
s.sell('Ramen', 10)
print(s.get_all_products())
print(s.get_product_info('Football T-Shirt'))
assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.get_income())
s.sell('Football T-Shirt', 20)
print(s.get_income())
print(s.get_product_info('Football T-Shirt'))
print(s.set_discount('Sport', 50, 'type'))
print(s.get_all_products())

