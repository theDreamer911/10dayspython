# class Product:
#     def __init__(self, price):
#         # self.set_price(price)
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     # @price.setter
#     # def price(self, value):
#     #     if value < 0:
#     #         raise ValueError('Price cannot be negative')
#     #     self.__price = value

#     # price = property(get_price, set_price)


# product = Product(10)
# # product.price(-1)
# product.price = 2
# print(product.price)


def noon_meal(
    opening, dessert): return f"Food: {opening.title()} {dessert.title()}"


print(noon_meal('Ice cream', 'Chocolate'))
print(noon_meal)


def the_meal(
    food, drink): return f"I have eat {food.title()} and {drink.title()}"


the_meal('Soup', 'Oxygen Water')
