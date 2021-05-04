from time import sleep
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

# print(admin_id)
# print(admin_pass)


# Create data
def new_register():# havent add
    f = open("admin.txt", "a+")
    new_data = f.readlines()
    data_name = input("Your ID :")
    data_age = input("Your Pass :")
    new_data.append(data_name + " ")
    new_data.append(data_age + "\n")
    f.writelines(new_data)
    f.close()
# new_register()

# How to rewrite the file data from input


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

# print(car_list)
# print(car_id)
# print(car_name)
# print(car_available)
# print(booking_customer)
# print(booking_payment)
# print(booking_duration)
# print(car_details[6].replace(" ","\n"))

# Create data
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

#create data
def new_customer():#
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


def login_admin():
    id_num1 = input("Please Enter Your ID :")
    password1 = input("Please Enter Your Password :")
    
    for i in range(len(admin_id)):
        if id_num1 == admin_id[i]:
            if password1 == admin_pass[i]:
                admin_menu()


    print('''
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
        view_car_available()

    elif option3 =="5":
        all_customer_booking()

    elif option3 =="6":
        pass

    elif option3 =="7":
        pass

    elif option3 =="8":
        pass

    elif option3 =="9":
        pass
        
    elif option3 =="10":
        sys.exit()
    
    else:
        admin_menu()





#old
def return_rented_car():
    id_input = input("Please Enter the Car ID of the rented car :")
    name_input = input("Please Enter the name of the customer of the rented car:")

    for i in range(len(car_id)):
        if id_input == car_id[i]:
            if name_input.lower() == booking_customer[i]:
                car_available[i] = "no"
                cars_data = open("car.txt", "w")
                for l in range(len(car_id)):
                    cars_data.write(car_id[l]+", ")
                    cars_data.write(car_name[l]+", ")
                    cars_data.write(car_available[l]+", ")
                    cars_data.write(booking_customer[l]+", ")
                    cars_data.write(booking_payment[l]+", ")
                    cars_data.write(booking_duration[l]+", ")
                    cars_data.write(car_details[l]+"\n")

                cars_data.close()
                print('''
                Car successfully returned . . .
                Returning to Admin Menu
                ''')
                admin_menu()
    print('''
    Incorrect Data entered . . .
    >>> Returning back to Admin Menu . . .
    ''')
    admin_menu()

#problem with car name priting none value
def all_rented_car():
    for i in range(len(car_id)):
        if car_available[i].replace(" ","") == "no":
            print("car id: " + car_id[i])
            print("car name: " + car_name[i])
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Total duration booked: " + booking_duration[i])
            print("---Car details---\n" + car_details[i]+"\n")

    x = input("Press Anything to return to admin menu . . .")
    admin_menu()

def all_customer_booking():
    for i in range(len(car_id)):
        if car_available[i].replace(" ","") == "no":
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Total duration booked: " + booking_duration[i])
            print("car id of booked car: " + car_id[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()

all_customer_booking()


