class product:
    def __init__(self, name, description, price, size, color):
        self.name = name
        self.description = description
        self.price = price
        self.size = size
        self.color = color


    def change_price(self, new_price):
        self.price = self.price = new_price
        print("تم تغيير السعر الى : " + str(self.price))
        return self.price


    def change_description(self,new_description):
        self.description = new_description
        print("تم تغيير الوصف الى : " + str(self.description))
        return self.description


    def info(self):
        return f'Name: {self.name}, Item: {self.item}, Price: {self.price}, Size: {self.size}, Color: {self.color}'

shoes = product('Shoes', 'sport', 300, 43, 'black')
pants = product('Pants', 'jeans', 150, 35, 'blue')


print(shoes.price)
shoes.change_price(400)

print(pants.description)
pants.change_description('trouser')