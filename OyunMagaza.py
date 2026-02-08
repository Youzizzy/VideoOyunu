from StockTemplate import Stock
from UserTemplate import User

depo = Stock()

user_table  = {
    "Doga": {
        "role" : "employee",
        "password" : "1107"
    },

    "Ecümen" : {
        "role" : "employee",
        "password" : "1207"
    },

    "1": {
        "role" : "customer",
        "password" : "1"
    },
    "Ananas_123": {
        "role" : "customer",
        "password" : "1234"
    },

    "kkkaan": {
        "role" : "customer",
        "password" : "cus2"
    },

     "zeynep.w": {
        "role" : "customer",
        "password" : "cus3"
     }
}

def login_sequence():
    while True:
        uN = input("Username: ")
        pW = input("Password: ")
        
        if uN in user_table:
            user_data = user_table[uN]

            user = User(
                uN,
                user_data["role"],
                user_data["password"]
            )

            if user.check_password(pW):
                print(f"\nWelcome {uN}!")
                return user_data["role"]
            else:
                print("Wrong password or username.")
        else:
            print("User not found.")

def update_list():
    print()

def employee_menu():
    while True:
        print("\n---  Employee Operations ---")
        print("1. Add New Game")
        print("2. View the Games")
        print("3. Update Game Info")
        print("4. Delete Game")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            depo.employee_add_gaem()
        elif choice == "2":
            depo.all_view_gaem()
        elif choice == "3":
            depo.employee_update_gaem()
        elif choice == "4":
            depo.employee_delete_gaem()
        elif choice == "5":
            print("You logged out.")
            return
        else:
            print("Invalid choice.")

def customer_menu():
    while True:
        depo.all_view_gaem()
        print("\n---  Customer Operations ---")
        print("1. Add Game to Cart")
        print("2. View Cart")
        print("3. Finalize Purchase")
        print("4. Logout")
        choice = input("Choose operation:\n")
        if choice == "1":
            depo.customer_add_to_cart()
        elif choice == "2":
            depo.customer_view_cart()
        elif choice == "3":
            depo.customer_purchase()
        elif choice == "4":
            print("You logged out.")
            return
        else:
            print("Invalid choice.")

while True:
    loginRole = login_sequence()
    if loginRole == "employee":
        employee_menu()
    elif loginRole == "customer":
        customer_menu()








# sobe
# fuggler big fugg dogah boogah 
# adidas çin yeleği çin ve lezsbiyen