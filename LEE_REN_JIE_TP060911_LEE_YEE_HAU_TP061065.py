# LEE REN JIE
# TP060911
# LEE YEE HAU
# TP061065

'''
Functionalities of Admin

i. Login to Access System.
ii. Add Cars to be rented out. **
iii. Modify Car Details **
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
# python assignment demo
import sys
from datetime import date

#Main menu, Ask identity of end user, either Customer or Admin
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
            login_admin()
            break
        elif option == "3":
            sys.exit()

        else:
            option = input("Please Enter Your Option :")


# --------------------------------------ADMIN DATA OPERATIONS----------------------------------------
# Read data
admin_data = open("admin.txt", "r")
lines = admin_data.readlines()
admin_id = []
admin_pass = []

for admin in lines:
    admin_list = admin.split(" ")
    admin_id.append(admin_list[0])
    admin_pass.append(admin_list[1].replace("\n", ""))

# ----------------------------------CUSTOMER DATA OPERATIONS-------------------------------------------------
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

# ----------------------------------CAR DATA OPERATIONS-------------------------------------------------------
# Read data
cars_data = open("car.txt", "r")
lines = cars_data.readlines()
car_id = []
car_name = []
car_available = []
booking_customer = []
booking_payment = []
booking_duration = []
payment_year = [] #new update
payment_month = []#new update
payment_day = []#new update
car_details = []

for car in lines:
    car_list = car.split(",")
    car_id.append(car_list[0])
    car_name.append(car_list[1])
    car_available.append(car_list[2])
    booking_customer.append(car_list[3])
    booking_payment.append(car_list[4])
    booking_duration.append(car_list[5])
    payment_year.append(car_list[6])
    payment_month.append(car_list[7])
    payment_day.append(car_list[8])
    car_details.append(car_list[9].replace("\n", ""))


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
    new_ctm_id = input("New Customer ID(eg: ctm1):")
    new_ctm_pass = input("Your Password:")
    new_ctm_name = input("Your Name:")
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

#Functionality of Admin
#i. Login to Access System.
def login_admin():
    id_num1 = input("\nPlease Enter Your Admin ID :")
    password1 = input("Please Enter Your Admin Password :")

    for i in range(len(admin_id)):
        if id_num1 == admin_id[i]:
            if password1 == admin_pass[i]:
                admin_menu()

    x = input('''
    Error ID or Password detected
    returning back to main menu . . .
    ''')
    main_menu()

# after the login as an admin, admin menu interface
def admin_menu():
    print('''
    \n-------What would you like to do?-------\n
    [1]Add Cars to be rented out
    [2]Modify Car details
    [3]Return a rented car

    Display All records of:
    [4]Cars rented out
    [5]Cars available for rent
    [6]Customer Bookings
    [7]Customer Payment for a specific Booking time duration\n

    Search Specific record of:
    [8]Customer Booking
    [9]Customer Payment

    [10]Back to Main Menu
    [11]Exit\n
    ''')

    # prompt user for input
    option3 = input("Please Enter Your Option :")
    while True:
        if option3 == "1":
            new_car()

        elif option3 == "2":
            modify_car_detail()

        elif option3 == "3":
            return_rented_car()

        elif option3 == "4":
            all_rented_car()

        elif option3 == "5":
            view_car_available()

        elif option3 == "6":
            all_customer_booking()

        elif option3 == "7":
            payment_specific_time()

        elif option3 =="8":
            specific_booking()

        elif option3 =="9":
            specific_payment()
        
        elif option3 =="10":
            main_menu()
        
        elif option3 == "11":
            sys.exit()

        else:
            option3 = input("Please Enter Your Option :")


# ii.	Add Cars to be rented out. (RJ)
def new_car():
    f = open("car.txt", "a+")
    car_data = f.readlines()
    # input
    new_car_id = input("New Car ID(eg: car1):")
    new_car_name = input("New Car's Name:")
    is_car_available = "yes"
    new_car_details = input("Car details(eg: color:red horsepower:130):")
    # append to car_data list
    car_data.append(new_car_id + ",")
    car_data.append(new_car_name + ",")
    car_data.append(is_car_available + ",")
    car_data.append("none,none,none,")
    car_data.append(new_car_details + "\n")
    f.writelines(car_data)
    f.close()

    x = input('''
    Done !
    >>>Press Enter to return to Admin Menu
    ''')

    admin_menu()


# iii.	Modify Car Details done checked*
# color: + horsepower: [6] and car id [0]
def modify_car_detail():
    id_input = input(
        "To modify the car detail,\nPlease insert the car ID of the car:")

    for i in range(len(car_id)):
        if id_input == car_id[i]:
            print("This is the current car detail !\n")
            print(car_id[i])
            print(car_details[i].replace(" ", "\n"))
            new_detail = input(
                "\nWhat is the new color and horsepower of the car? eg:(color:** horsepower:**)\n")
            car_details[i] = new_detail

            cars_data = open("car.txt", "w")

            for l in range(len(car_id)):
                cars_data.write(car_id[l]+",")
                cars_data.write(car_name[l]+",")
                cars_data.write(car_available[l]+",")
                cars_data.write(booking_customer[l]+",")
                cars_data.write(booking_payment[l]+",")
                cars_data.write(booking_duration[l]+",")
                cars_data.write(car_details[l]+"\n")
            cars_data.close()
            x = input('''
            Done !
            >>>Press Enter to return to Admin Menu
            ''')
            admin_menu()

    x = input('''
    Car Detail failed to modify due to incorrect input . . .
    >>>Returning to Admin Menu . . .
    ''')
    admin_menu()


# vi. Return a Rented Car.done checked*
def return_rented_car():
    id_input = input("Please Enter the Car ID of the rented car :")

    for i in range(len(car_id)):
        if id_input == car_id[i]:
            if car_available[i].replace(" ", "") == "no":
                print(
                    "\nPlease Check the details of the respective customer of the rented car\n")
                # add on display of ex: "Customer name:"
                print("Customer Name: ", booking_customer[i])
                print("Booking duration (Nth days) : ", booking_duration[i])
                print("Total Payment: ", booking_payment[i])

                random_input = input(
                    "\n[1]Back to Admin Menu \nOr press anything to continue . . .")
                if random_input == "1":
                    admin_menu()

                car_available[i] = "yes"
                booking_customer[i] = "none"
                booking_duration[i] = "none"
                booking_payment[i] = "none"

                cars_data = open("car.txt", "w")
                for l in range(len(car_id)):
                    cars_data.write(car_id[l]+",")
                    cars_data.write(car_name[l]+",")
                    cars_data.write(car_available[l]+",")
                    cars_data.write(booking_customer[l]+",")
                    cars_data.write(booking_payment[l]+",")
                    cars_data.write(booking_duration[l]+",")
                    cars_data.write(car_details[l]+"\n")

                cars_data.close()
                x = input('''
                Done !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()
            else:
                x = input('''
                Done !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()
    x = input('''
    Incorrect Data entered . . .
    >>> Returning back to Admin Menu . . .
    ''')
    admin_menu()


# display all records of a. Cars Rented Out done checked*(none value printed)
def all_rented_car():
    print("\n---All Records of Rented Cars---")
    for i in range(len(car_id)):
        if car_available[i].replace(" ", "") == "no":
            print("car id: " + car_id[i])
            print("car name: " + car_name[i])
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("---Car details---\n" + car_details[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


# Display all records of c. Customer Bookings done check
def all_customer_booking():
    for i in range(len(car_id)):
        if car_available[i].replace(" ", "") == "no":
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("car id of booked car: " + car_id[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()
            

#all records of d. Customer Payment for a specific *booking* time duration
def payment_specific_time():
    print("\nPlease Enter a specific time to view all specific payments in 2021: ")
    start_year,start_month, start_day = int(input("Start Year:")), int(input("Start Month:")), int(input("Start Day:"))
    end_year,end_month, end_day = int(input("End Year:")), int(input("End month:")), int(input("End day:"))

    #print("All Payments between "  + "th Day of booking\n")
    for i in range(len(car_id)):
        if payment_month[i] != "none":
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])

        
            if start_year < check_year < end_year:
                print("\nCustomer Name: " + booking_customer[i])
                print("Payment Date\nMonth:" + str(date(check_year,check_month,check_day)))
            elif start_year == check_year:
                if start_month < check_month:
                    print("\nCustomer Name: " + booking_customer[i])
                    print("Payment Date\nMonth:" + str(date(check_year,check_month,check_day)))
                    print("Total payment: " + booking_payment[i] + "\n") 
                elif start_month == check_month:
                    if start_day < check_day:
                        print("\nCustomer Name: " + booking_customer[i])
                        print("Payment Date\nMonth:" + str(date(check_year,check_month,check_day)))
                        print("Total payment: " + booking_payment[i] + "\n") 
            elif end_year == check_year:
                if end_month > check_month:
                    print("\nCustomer Name: " + booking_customer[i])
                    print("Payment Date\nMonth:" + str(date(check_year,check_month,check_day)))
                    print("Total payment: " + booking_payment[i] + "\n")
                elif end_month == check_month:
                    if end_day > check_day:
                        print("\nCustomer Name: " + booking_customer[i])
                        print("Payment Date\nMonth:" + str(date(check_year,check_month,check_day)))
                        print("Total payment: " + booking_payment[i] + "\n") 
    
    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


#v. Search Specific record of
#a. Customer Booking
def specific_booking():
    print("---Please Enter the following specific criteria---")
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Booking is shown below--")
    for i in range(len(car_id)):  # 0 1 2 3
        if booking_customer[i].replace(" ", "") == criteria_customer:
            if car_id[i].replace(" ", "") == criteria_id:
                print("Customer Name: " + booking_customer[i])
                print("Booked Car: " + car_name[i])
                print("Booked Car ID: " + car_id[i])
                print("Booking Duration: " + booking_duration[i] + "\n")

    x=input('''
    Records of Specific Criteria are shown above !
    >>>Press Enter to return to Admin Menu
    ''')


#v. Search Specific record of
#b. Customer Payement
def specific_payment():
    print("---Please Enter the following specific criteria---")
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Booking is shown below--")
    for i in range(len(car_id)): #0 1 2 3
        if booking_customer[i].replace(" ","") == criteria_customer:
            if car_id[i].replace(" ","") == criteria_id:
                print("Customer Name: " + booking_customer[i])
                print("Total payment: " + booking_payment[i]+"\n")
                
    x=input('''
    Records of Specific Criteria are shown above !
    >>>Press Enter to return to Admin Menu
    ''')
    admin_menu()


main_menu()
