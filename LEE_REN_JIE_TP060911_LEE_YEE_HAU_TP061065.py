# LEE REN JIE
# TP060911
# LEE YEE HAU
# TP061065

'''
Functionalities of Admin

i. Login to Access System.
ii. Add Cars to be rented out.
iii. Modify Car Details
iv. Display All records of
a. Cars Rented Out
b. Cars available for Rent
c. Customer Bookings
d. Customer Payment for a specific time duration
v. Search Specific record of
a. Customer Booking
b. Customer Payment
vi. Return a Rented Car.
vii. Exit

Functionalities of All Customers (Registered / Not-Registered)
i. View all cars available for rent.
ii. New customer Register to Access other Details
iii. Exit

Functionalities of Registered Customer
i. Login to Access System
ii. Modify Personal Details.
iii. View Personal Rental History.
iv. View Detail of Cars to be Rented Out.
v. Select and Book a car for a specific duration.
vi. Do payment to confirm Booking.
vii. Exit
'''
#python assignment demo
import sys
from datetime import date
def main_menu():
    print(date.today())
    print("\n[1]Login to Access System")
    print("[2]New Customer Register")
    print("[3]View All Cars available for rent")
    print("[4]Exit\n")

    option = int(input("Please Enter Your Option :"))
    


    while True:
        if option == 1:
            ask_identity()
            break

        elif option == 2:
            new_register()
            break

        elif option == 3:
            view_car_available()
            break
    
        elif option == 4:
            sys.exit()
    
        else:
            option = int(input("Please Enter Your Option :"))


#login as an admin
def login_admin():
    # might need to global both variable but assignment dont allow
    id_num = input("Please Enter Your ID :")
    password1 = input("Please Enter Your Password :")

    admin_checkdata()

#login as a customer
def login_customer():
    #might need to global both variable but assignment dont allow
    id_num = input("Please Enter Your ID :")
    password2 = input("Please Enter Your Password :")

    customer_checkdata()

#check the id of the admin and provide feature for admin
def admin_checkdata():
    #create an empty list
    data = []
    #loop through each individual data inside the txt and append into our list as an element
    file_data = open("data.txt","r+")
    data = file_data.readlines()

    if id_num and password in data:
        print("Welcome !")
        print("[1]Add cars to be rented out")
        print("[2]Modify Car details")
        print("[3]Display All records")
        print("[4]Search Specified Record")
        print("[5]Return a rented Car")
        print("[6]Return to Main Menu")
        option2 = int(input("Enter Your Option :"))
        while True:
            if option2 == 1:
                break

            elif option2 == 2:
                break

            elif option2 == 3:
                break
    
            elif option2 == 4:
                break
            
            elif option2 == 5:
                break

            elif option2 == 6:
                break

    
            else:
                option2 = int(input("Please Enter Your Option :"))




    elif id_num and password not in data:
        print("Error id or password detected")
        ask_identity()
    
    else:
        print("Couldn't identify info, returning to Main menu...")
        main_menu()

#check customer data and give customer feature
def customer_checkdata():
    #create an empty list
    data = []
    #loop through each individual data inside the txt and append into our list as an element
    file_data = open("data.txt","r+")
    data = file_data.readlines()
    if id_num and password in data:
        print("Welcome !")
        print()

    elif id_num and password not in data:
        print("Error id or password detected")
        ask_identity()
    
    else:
        print("Couldn't identify info, returning to Main menu...")
        main_menu()

#check the identity of the user
def ask_identity():
    print("\n[1]Registered Customer")
    print("[2]Admin")
    print("Type Anything else to return to Main Menu")

    identity = int(input("Please Enter Your Option :"))
    if identity == 1:
        login_customer()
    elif identity == 2:
        login_admin()
            
    else:
        main_menu()

#function to register as a new user
def new_register():
    f = open("customer.txt")
    new_data = f.readlines()
    data_name = input("Your Name :")
    data_age = input("Your Age :")
    new_data.append(data_name)
    new_data.append(data_age)
    f.writelines(new_data)
    f.close()
    main_menu()

def view_car_available():
    car = open("cars_available.txt")
    car_data = car.readlines()
    for i in car_data:
        print(i)


main_menu()