class Shelter:
    count = 0 #class variable
    def __init__(self):
        self.total = {}
        Shelter.count += 1
    def add_animal(self, type, count):
        if type in self.total:
            self.total[type] += count 
        else:
            self.total[type] = count

    def remove_animal(self, type, count):
        if type in self.total:
            if count > self.total[type]:
                print('error')
            elif count == self.total[type]:
                self.total.pop(type)
            else:
                self.total[type] -= count
        else:
            print('animal not found')
       
    def view_shelter(self):
        print('the animals in the shelter are: ', self.total)

obj1 = Shelter()
obj1.add_animal('dog',23)
obj1.add_animal('dog', 1)
obj1.add_animal('cat', 4)

obj1.remove_animal('dog', 26)
obj1.view_shelter()

obj2 = Shelter()
obj3 = Shelter()
obj4 = Shelter()

print(Shelter.count)


# class Enemy:
    
#     def __init__(self,life):
#         print('boo')
#         self.life = life
#     def attack(self):
#         print('out')
#         self.life -= 1
#     def checkLife(self):
#         print(self.life)

# vampire = Enemy(10)
# chuckE = Enemy(2)
# ghost = Enemy(5)
# vampire.attack()
# vampire.attack()
# vampire.checkLife()