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
    print("\nWho are you?")
    print("\n[1]Customer")
    print("[2]Admin")
    print("[3]Exit]\n")

    option = input("Please Enter Your Option :")

    while True:
        if option == "1":
            customer_menu()
            break
        elif option == "2":
            login_admin()
            break
        elif option == "3":
            sys.exit()
        
        else:
            option = input("Please Enter Your Option :")

def customer_menu():
    print("Welcome !\n")
    print("[1]Login as a Customer")
    print("[2]Register as a new Customer")
    print("[3]View All Cars Available for rent")
    print("[4]Back to Main Menu\n")

    option2 = input("Please Enter Your Option :")

    if option2 == "1":
        login_customer()
    elif option2 == "2":
        new_register()
    elif option2 == "3":
        view_car_available()
    else:
        main_menu()

def login_customer():

    id_num2 = input("Please Enter Your ID :")
    password2 = input("Please Enter Your Password :")

    admin_data = open("customer.txt", "r")
    lines = admin_data.readlines()
    customer_id = []
    customer_pass = []

    for customer in lines:
        customer_list = customer.split(" ")
        customer_id.append(customer_list[0])
        customer_pass.append(customer_list[1].replace("\n", ""))
    admin_data.close()
    
    no = 0

    
    if id_num2 in customer_id:
        if password2 in customer_pass:
                no += 1

        else:
            continue
                
    else:
        continue
    if no > 0:
        registered_customer_menu()
    else:
        print("Error ID or Password detected\n")
        customer_menu()


#function to register as a new user
def new_register():
    f = open("customer.txt","a+")
    new_data = f.readlines()
    data_name = input("Your ID :")
    data_age = input("Your Password :")
    new_data.append(data_name +" ")
    new_data.append(data_age + "\n")
    f.writelines(new_data)
    f.close()
    customer_menu()


def view_car_available():
    car = open("cars_available.txt")
    car_data = car.readlines()
    for i in car_data:
        print(i)

def registered_customer_menu():
    print("[1]Modify Personal Details")
    print("[2]View Personal Rental History")
    print("[3]View Details of Cars to be rented out")
    print("[3]Select and Book a car for a specific duration")
    print("[4]Do Payment to comfirm booking")
    print("[5]Return to Main Menu")
    print("[6]Exit\n")


def login_admin():
    id_num1 = input("Please Enter Your ID :")
    password1 = input("Please Enter Your Password :")

    admin_data = open("admin.txt", "r")
    lines = admin_data.readlines()
    admin_id = []
    admin_pass = []

    for admin in lines:
        admin_list = admin.split(" ")
        admin_id.append(admin_list[0])
        admin_pass.append(admin_list[1].replace("\n", ""))
    admin_data.close()

    no = 0

    
    if id_num2 in customer_id:
        if password2 in customer_pass:
                no += 1

        else:
            continue
                
    else:
        continue
    if no > 0:
        admin_menu()
    else:
        print("Couldn't identify info, returning to Main menu...\n")
        main_menu()

def admin_menu():
    print("What would you like to do?\n")
    print("[1]Add Cars to be rented out")
    print("[2]Modify Car details") #color: + horsepower: [6] and car id [0]
    print("[3]Return a rented car\n")

    print("Display All records of:")
    print("[3]Cars rented out")
    print("[4]Cars available for rent")
    print("[5]Customer Bookings")
    print("[6]Customer Payment for a specific time duration\n")

    print("Search Specific record of:")
    print("[7]Customer Booking")
    print("[8]Customer Payment")
    print("[9]Exit\n")
    
    #prompt user for input
    option3 = input("Please Enter Your Option :")

    if option3 == "1":
        add_car()
    elif option3 =="2":
        modify_car_detail()
    
    elif option3 =="3":

    elif option3 =="4":

    elif option3 =="5":

    elif option3 =="6":

    elif option3 =="7":

    elif option3 =="8":

    elif option3 =="9":
        sys.exit()


def add_car():
    car_data = open("customer.txt", "r")
    lines = car_data.readlines()
    car_name = []
    

    for car in lines:
        car_list = car.split(" ")
        car_name.append(customer_list[1].replace)
    car_data.close()
    car_input = input("Please Enter the add the Name of Car to be rented out: ")
    new_data = car_name.append(car_input+"\n")
    car_data = open("customer.txt", "a+")
    car_data.writelines(new_data)
    car_data.close()

    admin_menu()
    
def modify_car_detail():
    id_input = input("To modify the car detail,\nPlease insert the car ID of the car:")
    cars_data = open("cars.txt", "r")
    lines = cars_data.readlines()
    cars_data.close()

    car_id = []
    car_name = []
    car_available = []
    booking_customer = []
    booking_payment = []
    booking_duration = []
    car_detail = []
    
    for data in lines:
        data_list = data.split(",")
        car_id.append(data_list[0])
        car_name.append(car_list[1])
        car_available.append(car_list[2])
        booking_customer.append(car_list[3])
        booking_payment.append(car_list[4])
        booking_duration.append(car_list[5])
        car_detail.append(data_list[6].replace("\n",""))
    
    
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            print("This is the current car detail !\n")
            print(car_id[i])
            print(car_detail[i].replace(" ","\n"))
            new_detail = input("\nWhat is the new color and horsepower of the car?\n")
            car_detail[i] = new_detail
            break

    

    cars_data = open("cars.txt", "w")
    for l in range(len(car_id)):

        cars_data.write(car_id[l])
        cars_data.write(car_name[l])
        cars_data.write(car_available[l])
        cars_data.write(booking_customer[l])
        cars_data.write(booking_payment[l])
        cars_data.write(booking_duration[l])
        cars_data.write(car_detail[l])
    cars_data.close()










    
    

    


















main_menu()