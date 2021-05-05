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
#python assignment demo
import sys
from time import sleep
from datetime import date

#Main menu, Ask identity of end user, either Customer or Admin
def main_menu():
    print(date.today())
    print('''
    -------Who are you?-------\n
    [1]Customer
    [2]Admin
    [3]Exit]\n
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

#--------------------------------------ADMIN DATA OPERATIONS----------------------------------------
# Read data
admin_data = open("admin.txt", "r")
lines = admin_data.readlines()
admin_id = []
admin_pass = []

for admin in lines:
    admin_list = admin.split(" ")
    admin_id.append(admin_list[0])
    admin_pass.append(admin_list[1].replace("\n", ""))

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
car_details = []

for car in lines:
    car_list = car.split(",")
    car_id.append(car_list[0])
    car_name.append(car_list[1])
    car_available.append(car_list[2])
    booking_customer.append(car_list[3])
    booking_payment.append(car_list[4])
    booking_duration.append(car_list[5])
    car_details.append(car_list[6].replace("\n", ""))

def customer_menu():
    print('''
    -------Welcome!-------\n
    [1]Login as a Customer
    [2]Register as a new Customer
    [3]View All Cars Available for rent
    [4]Back to Main Menu\n
    ''')

    option2 = input("Please Enter Your Option :")

    if option2 == "1":
        login_customer()
    elif option2 == "2":
        new_customer()
    elif option2 == "3":
        view_car_available()
    else:
        main_menu()

#i.	Login to Access System 
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


#ii.	New customer Register to Access other Details (RJ)
def new_customer():
    f = open("customer.txt", "a+")
    customer_data = f.readlines()
    #input
    #need add auto id
    new_ctm_id = input("New Customer ID(eg: ctm1):")
    new_ctm_pass = input("Your Password:")
    new_ctm_name = input("Your Name:")
    #append to car_data list
    customer_data.append(new_ctm_id + ",")
    customer_data.append(new_ctm_pass + ",")
    customer_data.append(new_ctm_name + ",")
    customer_data.append("none,none,none\n")
    f.writelines(customer_data)
    f.close()
    x=input('''
    Register is successful !
    >>>Press Enter to Go to Customer Menu
    ''')
    customer_menu()

#i.	View all cars available for rent + Display all records of b. Cars available for Rent
def view_car_available():
    for i in range(len(car_data)):
        if car_available[i] == "yes":
            print("Car ID: " + car_id[i])
            print("Car Name: " + car_name[i])
            print("--Car Details--\n" +car_details[i]+"\n")
    x=input('''
    Records are shown above
    >>>Press Enter to return to Main Menu
    ''')
    main_menu()
           
#after login as a customer, menu
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

#Functionality of Admin
#i. Login to Access System.
def login_admin():
    id_num1 = input("Please Enter Your ID :")
    password1 = input("Please Enter Your Password :")
    
    for i in range(len(admin_id)):
        if id_num1 == admin_id[i]:
            if password1 == admin_pass[i]:
                admin_menu()


    x=input('''
    Error ID or Password detected
    returning back to main menu . . .
    ''')
    main_menu()

def admin_menu():
    print('''
    \n-------What would you like to do?-------\n
    [1]Add Cars to be rented out
    [2]Modify Car details 
    [3]Return a rented car\n

    Display All records of:
    [4]Cars rented out
    [5]Cars available for rent
    [6]Customer Bookings
    [7]Customer Payment for a specific time duration\n

    Search Specific record of:
    [8]Customer Booking
    [9]Customer Payment
    [10]Exit\n
    ''')
    
    #prompt user for input
    option3 = input("Please Enter Your Option :")

    if option3 == "1":
        new_car()
    elif option3 =="2":
        modify_car_detail()
    
    elif option3 =="3":
        return_rented_car()

    elif option3 =="4":
        all_rented_car()

    elif option3 =="5":
        view_car_available()

    elif option3 =="6":
        all_customer_booking()

    elif option3 =="7":
        payment_specific_time()

    elif option3 =="8":
        specific_booking()

    elif option3 =="9":
        specific_payment()
        
    elif option3 =="10":
        sys.exit()
    
    else:
        admin_menu()

#ii.	Add Cars to be rented out. (RJ)
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
    car_data.append("none,none,none,")
    car_data.append(new_car_details  + "\n")
    f.writelines(car_data)
    f.close()

    x=input('''
    Done !
    >>>Press Enter to return to Admin Menu
    ''')

    admin_menu()


#iii.	Modify Car Details done checked*
#color: + horsepower: [6] and car id [0]
def modify_car_detail():
    id_input = input("To modify the car detail,\nPlease insert the car ID of the car:")
    
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            print("This is the current car detail !\n")
            print(car_id[i])
            print(car_details[i].replace(" ","\n"))
            new_detail = input("\nWhat is the new color and horsepower of the car? eg:(color:** horsepower:**)\n")
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
            x=input('''
            Done !
            >>>Press Enter to return to Admin Menu
            ''')
            admin_menu()
    

   
    print('''
    Car Detail failed to modify due to incorrect input . . .
    >>>Returning to Admin Menu . . .
    ''')
    #adding sleep to make it looks more realistic, just like a loading page 
    sleep(3)
    admin_menu()


#vi. Return a Rented Car.done checked*
def return_rented_car():
    id_input = input("Please Enter the Car ID of the rented car :")

    
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            if car_available[i].replace(" ","") == "no":
                print("\nPlease Check the details of the respective customer of the rented car\n")
                #add on display of ex: "Customer name:"
                print("Customer Name: ", booking_customer[i])
                print("Booking duration (Nth days) : ", booking_duration[i])
                print("Total Payment: ", booking_payment[i])

                random_input = input("\n[1]Back to Admin Menu \nOr press anything to continue . . .")
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
                x=input('''
                Done !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()
            else:
                x=input('''
                Done !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()
    print('''
    Incorrect Data entered . . .
    >>> Returning back to Admin Menu . . .
    ''')
    sleep(3)
    admin_menu()

#display all records of a. Cars Rented Out done checked*(none value printed)
def all_rented_car():
    for i in range(len(car_id)):
        if car_available[i].replace(" ","") == "no":
            print("car id: " + car_id[i])
            print("car name: " + car_name[i])
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("---Car details---\n" + car_details[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()

#Display all records of c. Customer Bookings done check
def all_customer_booking():
    for i in range(len(car_id)):
        if car_available[i].replace(" ","") == "no":
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("car id of booked car: " + car_id[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()
            
#all records of d. Customer Payment for a specific time duration
def payment_specific_time():
    specific_time = input("\nPlease Enter a specific time to view all payments : ")
    for i in range(len(car_id)):
        if booking_duration[i].replace(" ","") == specific_time:
            print("All Payments in the " + specific_time + "th Day\n")
            print("Customer Name: "+ booking_customer[i])
            print("Total payment: " + booking_payment[i] +"\n")
    
    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()

#v. Search Specific record of
#a. Customer Booking
def specific_booking():
    print("---Please Enter the following specific criteria---")
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Booking is shown below--")
    for i in range(len(car_id)): #0 1 2 3
        if booking_customer[i].replace(" ","") == criteria_customer:
            if car_id[i].replace(" ","") == criteria_id:
                print("Customer Name: " + booking_customer[i])
                print("Booked Car: " + car_name[i])
                print("Booked Car ID: " + car_id[i])
                print("Booking Duration: " + booking_duration[i] + "\n")

    x=input('''
    Records of Specific Criteria are shown above !
    >>>Press Enter to return to Admin Menu
    ''')
    
    admin_menu()

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