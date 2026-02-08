from GameTemplate import Game
from json_readwrite import get_from_json, write_to_json
import time

class Stock:

    def __init__(self, filename="geemuzu.json"):
        self.filename = filename
        self.gamez = get_from_json(self.filename)
        self.cart = []

    def all_view_gaem(self):
        if not self.gamez:
            print("No games :/")
            return

        for gaem in self.gamez:
            print("-----------------------")
            print("Name:", gaem["name"])
            print("ESRB Rating:", gaem["ageRating"])
            print("Genre:", gaem["genre"])
            print("Price:", gaem["price"])
            print("Stock:", gaem["stock"])

    def customer_add_to_cart(self):
        if not self.gamez:
            print("There ain't nothin' you can buy, dawg")
            return
        name = input("What's the name of the Game you want to add to your cart?\n")
        for gaem in self.gamez:
            if gaem["name"] == name:
                if gaem["stock"] <= 0:
                    print(f"Game {gaem["name"]} is out of stock.")
                    time.sleep(2)
                    return
                if name in self.cart:
                    print("Item already in your cart.")
                    time.sleep(2)
                    return
                self.cart.append(name)
                return
        print("Game cannot be found.")
        time.sleep(2)

    def customer_view_cart(self):
        if len(self.cart) > 0:
                print("-----------------------")
                print("      In Cart:    ")
                for cartItem in self.cart:
                    print(cartItem)
        else:
            print("\nCart empty")
        time.sleep(2)

    def customer_purchase(self):
        print("Thank you for giving us money.")
        time.sleep(2)
        for cartItem in self.cart:
            for gaem in self.gamez:
                if gaem["name"] == cartItem:
                    gaem["stock"] = gaem["stock"] - 1
        write_to_json(self.filename, self.gamez)

    def employee_add_gaem(self):
        name = input("What's the Name of the Game: ")
        ageRating = int(input("Enter ESRB Age Rating: "))
        genre = input("Enter the Game Genre: ")
        price = int(input("Enter Price: "))
        stock = int(input("Enter Stock Count: "))

        newGaem = Game(name, ageRating, genre, price, stock)
        self.gamez.append(newGaem.__dict__)


        write_to_json(self.filename, self.gamez)
        # print("Bluey vs Mr Beast 2 - Electric Squid Game")
        # print("Guest starring: Big Fugg - Ooga Booga")

    def employee_update_gaem(self):
        name = input("What's the Name of the (new)Game?")
        for gaem in self.gamez:
            if gaem["name"] == name:
                gaem["ageRating"] = int(input("Enter ESRB Age Rating: "))
                gaem["genre"] = input("Enter the Game Genre: ")
                gaem["price"] = int(input("Enter Price: "))
                gaem["stock"] = int(input("New Copies: "))
                write_to_json(self.filename, self.gamez)
                print("Game information changed.")
                return
        print("Game not found.")

    def employee_delete_gaem(self):
        name = input("Enter the name of the game to remove: ")
        for gaem in self.gamez:
            if gaem["name"] == name:
                self.gamez.remove(gaem)
                write_to_json(self.filename, self.gamez)
                print("Game deleted.")
                return

        print("Game cannot be found.")