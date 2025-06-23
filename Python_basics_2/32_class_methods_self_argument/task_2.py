class Family:
    name = 'Common'
    money = 100_000
    house = False


    def info(self):
        print(f"Family name: {self.name}\n"
              f"Family funds: {self.money}\n"
              f"Having a house: {self.house}\n")


    def earn_money(self, amount):
        self.money += amount
        print(f"Money earned: {self.money}")


    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            house = True
            print(f"House purchased! Current money: {self.money}")
        else:
            print("Not enough money!")

family = Family()
family.info()