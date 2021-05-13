import sys
from datetime import date
#----------------------------------CAR DATA OPERATIONS-------------------------------------------------------
# Read data
cars_data = open("car.txt", "r")
lines = cars_data.readlines()
car_id = []
car_name = []
car_available = []
booking_customer = []
booking_payment = []
booking_duration = []
payment_month = []#new update
payment_day = []
car_details = []

for car in lines:
    car_list = car.split(",")
    car_id.append(car_list[0])
    car_name.append(car_list[1])
    car_available.append(car_list[2])
    booking_customer.append(car_list[3])
    booking_payment.append(car_list[4])
    booking_duration.append(car_list[5])
    payment_month.append(car_list[6])
    payment_day.append(car_list[7])
    car_details.append(car_list[8].replace("\n", ""))

# print(car_list)
# print(car_id)
# print(car_name)
# print(car_available)
# print(booking_customer)
# print(booking_payment)
# print(booking_duration)
# print(car_details[6].replace(" ","\n"))

# Create data  #update later
def new_car():
    f = open("car.txt", "a+")
    car_data = f.readlines()
    #input
    new_car_id = input("New Car ID(eg: car1):")
    new_car_name = input("New Car's Name:")
    is_car_available = "yes"
    new_car_details = input("Car details(eg: color:red horsepower:130):")
    #append to car_data list
    car_data.append(new_car_id + ",")
    car_data.append(new_car_name + ",")
    car_data.append(is_car_available + ",")
    car_data.append("none,none,none,none,none")#add none if changed
    car_data.append(new_car_details  + "\n")
    f.writelines(car_data)
    f.close()

# new_car()

#----------------------------------CUSTOMER DATA OPERATIONS-------------------------------------------------
# Read data
customer_data = open("customer.txt", "r")
lines = customer_data.readlines()
customer_id = []
customer_pass = []
customer_name = []
car_name = []
customer_payment = []
customer_duration = []

for customer in lines:
    customer_list = customer.split(",")
    customer_id.append(customer_list[0])
    customer_pass.append(customer_list[1])
    customer_name.append(customer_list[2])
    car_name.append(customer_list[3])
    customer_payment.append(customer_list[4])
    customer_duration.append(customer_list[5].replace("\n", ""))

# print(customer_id)
# print(customer_pass)
# print(customer_name)
# print(car_name)
# print(customer_payment)
# print(customer_duration)

# ------------------------Main Menu--------------------------------------
def main_menu():
    print(date.today())
    print('''
    -------Who are you?-------\n
    [1]Customer
    [2]Admin
    [3]Exit\n
    ''')

    option = input("Please Enter Your Option :")

    while True:
        if option == "1":
            customer_menu()
            break
        elif option == "2":
            # login_admin()
            break
        elif option == "3":
            sys.exit()

        else:
            option = input("Please Enter Your Option :")

def customer_menu():
    print('''
    -------Welcome!-------\n
    [1]Login as a Customer
    [2]Register as a new Customer
    [3]View All Cars Available for rent
    [4]Back to Main Menu\n
    ''')

    option2 = input("Please Enter Your Option :")

    while True:
        if option2 == "1":
            login_customer()
        elif option2 == "2":
            new_customer()
        elif option2 == "3":
            view_car_available()
        elif option2 =="4":
            main_menu()
        else:
            option2 = input("Please Enter Your Option :")


# i.	Login to Access System as a customer
def login_customer():

    id_num2 = input("Please Enter Your ID :")
    password2 = input("Please Enter Your Password :")

    for i in range(len(customer_id)):
        if id_num2 == customer_id[i]:
            if password2 == customer_pass[i]:
                registered_customer_menu()

    print('''Error Id or Password detected
    >>> returning back to Customer Menu . . .''')
    customer_menu()


# ii.	New customer Register to Access other Details (RJ)
def new_customer():
    f = open("customer.txt", "a+")
    customer_data = f.readlines()
    # input
    # need add auto id
    new_ctm_id = input("New Customer ID(eg: ctm1): ")
    new_ctm_pass = input("Your Password: ")
    new_ctm_name = input("Your Name: ")
    # append to car_data list
    customer_data.append(new_ctm_id + ",")
    customer_data.append(new_ctm_pass + ",")
    customer_data.append(new_ctm_name + ",")
    customer_data.append("none,none,none\n")
    f.writelines(customer_data)
    f.close()
    x = input('''
    Register is successful !
    >>>Press Enter to Go to Customer Menu
    ''')
    customer_menu()

# i.	View all cars available for rent + Display all records of b. Cars available for Rent
def view_car_available():
    print("\n---All Records of Cars Available for Rent---")
    for i in range(len(car_id)):
        if car_available[i] == "yes":
            print("Car ID: " + car_id[i])
            print("Car Name: " + car_name[i])
            print("--Car Details--\n" + car_details[i]+"\n")
    x = input('''
    Records are shown above
    >>>Press Enter to return to Main Menu
    ''')
    main_menu()

# after the login as a customer, registered customer menu interface
def registered_customer_menu():
    print('''
    [1]Modify Personal Details
    [2]View Personal Rental History
    [3]View Details of Cars to be rented out
    [3]Select and Book a car for a specific duration
    [4]Do Payment to comfirm booking
    [5]Return to Main Menu
    [6]Exit\n
    ''')

    option3 = input("Please Enter Your Option :")
    #while True:
        #if option3 == "1":

        #elif option3 == "2":

        #elif option3 == "3":

        #elif option3 == "4":

        #elif option3 == "5":
            #main_menu()

        #elif option 3 == "6":
            #sys.exit()
        #else:
            #option3 = input("Please Enter Your Option :")






main_menu()
'''
Functionalities of All Customers (Registered / Not-Registered)
i. View all cars available for rent. **
ii. New customer Register to Access other Details **
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
