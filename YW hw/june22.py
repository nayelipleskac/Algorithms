# June 22 HW
#Question 1

# class Bank:
#     def __init__(self):
#         self.balance = 0
#     def depositMoney(self, deposit):
#         self.balance += deposit
#     def withdrawMoney(self, withdrawal):
#         if withdrawal > self.balance:
#             print('error- withdraw up to ', self.balance)
#         else:
#             self.balance -= withdrawal

#     def checkBalance(self):
#         print('your balance is: ', self.balance)


# obj1 = Bank()
# obj1.checkBalance()
# obj1.depositMoney(200)
# obj1.checkBalance()
# obj1.withdrawMoney(300)
# obj1.checkBalance()

#Question 2
import time
class ShoppingCart:
    def __init__(self):
        self.cart = {}
    def addItem(self, item, quantity):
        if item in self.cart:
            self.cart[item] += quantity 
        else:
            self.cart[item] = quantity
    def removeItem(self, item, quantity):
        if item in self.cart:
            if quantity > self.cart[item]:
                print('error')
            elif quantity == self.cart[item]:
                self.cart.pop(item)
            else:
                self.cart[item] -= quantity
    def showCart(self):
        print('checking out...')
        time.sleep(2)
        print('here is your cart: ', self.cart)

obj1 = ShoppingCart()
obj1.addItem('apple', 20)
obj1.addItem('chips', 2)
obj1.addItem('milk', 4)
obj1.removeItem('apple', 4)
obj1.showCart()