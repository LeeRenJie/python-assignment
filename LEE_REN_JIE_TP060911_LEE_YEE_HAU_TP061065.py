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
from datetime import date, timedelta

#Main menu, Ask identity of end user, either Customer or Admin
def main_menu():
    print(date.today())
    print('''
    -------Who are you?-------\n
    [1]Customer
    [2]Admin
    [3]Exit\n
    ''')

    option = input("Please Enter Your Option: ")

    while True:
        if option == "1":
            customer_menu()
            break
        elif option == "2":
            login_admin()
            break
        elif option == "3":
            quit()

        else:
            option = input("Please Enter Your Option: ")


# --------------------------------------ADMIN DATA OPERATIONS----------------------------------------
# Read data
def read_admin_data():
    admin_data = open("admin.txt", "r")
    lines = admin_data.readlines()

    admin_id = []
    admin_pass = []

    for admin in lines:
        admin_list = admin.split(" ")
        admin_id.append(admin_list[0])
        admin_pass.append(admin_list[1].replace("\n", ""))

    return admin_id, admin_pass


# ---------------------------------------CUSTOMER DATA OPERATIONS-------------------------------------------------
# Read data
def read_customer_data():
    customer_data = open("customer.txt", "r")
    lines = customer_data.readlines()

    customer_id = []
    customer_pass = []
    customer_name = []
    booked_car_name = []
    customer_payment = []
    customer_duration = []
    customer_card = []

    for customer in lines:
        customer_list = customer.split(",")
        customer_id.append(customer_list[0])
        customer_pass.append(customer_list[1])
        customer_name.append(customer_list[2])
        booked_car_name.append(customer_list[3])
        customer_payment.append(customer_list[4])
        customer_duration.append(customer_list[5])
        customer_card.append(customer_list[6].replace("\n", ""))

    return customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card


# ---------------------------------------CAR DATA OPERATIONS-------------------------------------------------------
# Read data
def read_car_data():
    car_data = open("car.txt", "r")
    lines = car_data.readlines()
    car_id = []
    car_name = []
    car_price = []
    car_available = []
    ctm_key = []
    booking_customer = []
    booking_payment = []
    booking_duration = []
    payment_year = []
    payment_month = []
    payment_day = []
    car_details = []

    for car in lines:
        car_list = car.split(",")
        car_id.append(car_list[0])
        car_name.append(car_list[1])
        car_price.append(car_list[2])
        car_available.append(car_list[3])
        ctm_key.append(car_list[4])
        booking_customer.append(car_list[5])
        booking_payment.append(car_list[6])
        booking_duration.append(car_list[7])
        payment_year.append(car_list[8])
        payment_month.append(car_list[9])
        payment_day.append(car_list[10])
        car_details.append(car_list[11].replace("\n", ""))

    return car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details


# --------------------------------------RENTAL HISTORY OPERATIONS----------------------------------------
# Read data
def read_history_data():
    history_data = open("history.txt", "r")
    lines = history_data.readlines()

    ctm_history_id = []
    car_history_id = []
    car_history_name = []
    rental_duration = []
    history_year = []
    history_month = []
    history_day = []
    price_paid = []

    for history in lines:
        history_list = history.split(",")
        ctm_history_id.append(history_list[0])
        car_history_id.append(history_list[1])
        car_history_name.append(history_list[2])
        rental_duration.append(history_list[3])
        history_year.append(history_list[4])
        history_month.append(history_list[5])
        history_day.append(history_list[6])
        price_paid.append(history_list[7].replace("\n", ""))

    return ctm_history_id, car_history_id, car_history_name, car_history_name, rental_duration, history_year, history_month, history_day, price_paid

#----------------------------------------CUSTOMER FUNCTIONS-------------------------------------
def customer_menu():
    print('''
    -------Welcome To The Customer Menu-------\n
    [1]Login as a Customer
    [2]Register as a new Customer
    [3]View All Cars Available for rent
    [4]Back to Main Menu\n
    ''')

    option2 = input("Please Enter Your Option: ")

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
            option2 = input("Please Enter Your Option: ")


# i.	View all cars available for rent + Display all records of b. Cars available for Rent
def view_car_available():
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\n---All Records of Cars Available for Rent---\n")
    for i in range(len(car_id)):
        if car_available[i] == "yes":
            print("Car ID: " + car_id[i])
            print("Car Name: " + car_name[i].title())
            print("--Car Details--\n" + (car_details[i].replace(" ","\n")).title()+"\n")
    x = input('''
    Records are shown above
    >>>Press Enter to return to Main Menu
    ''')
    main_menu()


# ii.	New customer Register to Access other Details
def new_customer():
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    f = open("customer.txt", "a+")
    customer_data = f.readlines()
    new_ctm_id = ("ctm"+str(len(customer_id)+1))
    new_ctm_name = input("Your Name: ")
    new_ctm_pass = input("Your Password: ")
    new_ctm_card = input("Your Credit Card Number: ")
    # append to car_data list
    customer_data.append(new_ctm_id + ",")
    customer_data.append(new_ctm_pass + ",")
    customer_data.append(new_ctm_name.lower() + ",")
    customer_data.append("none,none,none,")
    customer_data.append(new_ctm_card + "\n")
    f.writelines(customer_data)
    f.close()
    x = input(f'''
    Your New Customer ID is {new_ctm_id}\n
    Register is successful !
    >>>Press Enter to Go to Customer Menu
    ''')
    customer_menu()


# i.	Login to Access System as a customer
def login_customer():
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    ctm_id_input = input("Please Enter Your ID: ")
    for i in range(len(customer_id)):
        if customer_id[i] == ctm_id_input:
            ctm_password_input = input("Please Enter Your Password: ")
            if ctm_password_input == customer_pass[i]:
                registered_customer_menu(ctm_id_input)
            else:
                print('''\n
                Wrong Password Entered
                >>> returning back to Customer Menu . . .
                ''')
                customer_menu()
        if i == (len(customer_id)-1):
            print('''\n
            Customer Id Not Found
            >>> returning back to Customer Menu . . .
            ''')
            customer_menu()


# After the login as a customer, registered customer menu interface
def registered_customer_menu(ctm_id):
    print('''
    -------Registered Customer Menu-------\n
    What would you like to do?
    [1]Modify Personal Details
    [2]View Details of Cars for Rent, Book and Pay
    [3]View Personal Rental History
    [4]Return to Main Menu
    [5]Exit\n
    ''')

    option3 = input("Please Enter Your Option: ")
    while True:
        if option3 == "1":
            modify_customer_detail(ctm_id)

        elif option3 == "2":
            view_car_details(ctm_id)

        elif option3 == "3":
            rental_history(ctm_id)

        elif option3 == "4":
            main_menu()

        elif option3 == "5":
            quit()

        else:
            option3 = input("Please Enter Your Option: ")


# ii. Modify Personal Details.
def modify_customer_detail(ctm_id):
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    ctm_pass_input = input("\nTo modify your detail,\nPlease insert your password again: ")

    for i in range(len(customer_pass)):
        if ctm_pass_input == customer_pass[i]:
            print("This is your current detail!\n")
            print("ID: ", customer_id[i])
            print("Name: ", customer_name[i].title())
            print("Password: ", customer_pass[i])
            print("Card Number: ", customer_card[i])
            print('''
            What would you like to modify?
            *Note that the ID is auto generated and can't be changed
            [1]Name
            [2]Password
            [3]Card Number
            [4]Back To Menu
            ''')

            modify_option = input("Please Enter Your Option: ")

            while True:
                if modify_option == "1":
                    new_name = input("\nWhat would you like to be called:")
                    customer_name[i] = new_name.lower()
                    customer_data = open("customer.txt", "w")
                    for index in range(len(customer_id)):
                        customer_data.write(customer_id[index]+",")
                        customer_data.write(customer_pass[index]+",")
                        customer_data.write(customer_name[index]+ ",")
                        customer_data.write(booked_car_name[index]+",")
                        customer_data.write(customer_payment[index]+",")
                        customer_data.write(customer_duration[index]+",")
                        customer_data.write(customer_card[index]+"\n")
                    customer_data.close()
                    x = input('''
                    Done !
                    >>>Press Enter to return to Customer Menu
                    ''')
                    registered_customer_menu(ctm_id)

                elif modify_option == "2":
                    new_password = input("\nWhat is your new password:")
                    customer_pass[i] = new_password
                    customer_data = open("customer.txt", "w")
                    for index in range(len(customer_id)):
                        customer_data.write(customer_id[index]+",")
                        customer_data.write(customer_pass[index]+",")
                        customer_data.write(customer_name[index]+ ",")
                        customer_data.write(booked_car_name[index]+",")
                        customer_data.write(customer_payment[index]+",")
                        customer_data.write(customer_duration[index]+",")
                        customer_data.write(customer_card[index]+"\n")
                    customer_data.close()
                    x = input('''
                    Done !
                    >>>Press Enter to return to Customer Menu
                    ''')
                    registered_customer_menu(ctm_id)

                elif modify_option == "3":
                    new_card = input("\nWhat is your new card number(16 numbers):")
                    customer_card[i] = new_card
                    customer_data = open("customer.txt", "w")
                    for index in range(len(customer_id)):
                        customer_data.write(customer_id[index]+",")
                        customer_data.write(customer_pass[index]+",")
                        customer_data.write(customer_name[index]+ ",")
                        customer_data.write(booked_car_name[index]+",")
                        customer_data.write(customer_payment[index]+",")
                        customer_data.write(customer_duration[index]+",")
                        customer_data.write(customer_card[index]+"\n")
                    customer_data.close()
                    x = input('''
                    Done !
                    >>>Press Enter to return to Customer Menu
                    ''')
                    registered_customer_menu(ctm_id)

                elif modify_option == "4":
                    registered_customer_menu(ctm_id)

                else:
                    modify_option = input("Please Enter Your Option :")


# iii. View Personal Rental History.
def rental_history(ctm_id):
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    ctm_history_id, car_history_id, car_history_name, car_history_name, rental_duration, history_year, history_month, history_day, price_paid = read_history_data()

    for i in range(len(customer_id)):
        if customer_id[i] == ctm_id:
            print("Your ID: ", customer_id[i])
            print("Your Name: ", customer_name[i])
            print("\n-------------Rental History-------------")
            for index in range(len(ctm_history_id)):
                if ctm_history_id[index] == ctm_id:
                    print("Car ID: ", car_history_id[index])
                    print("Car Name: ", car_history_name[index].title())
                    print("Rental Cost: RM", price_paid[index])
                    print(f"Duration: {rental_duration[index]} days")
                    print(f"Rented On: {history_day[index]}-{history_month[index]}-{history_year[index]}\n")
            x = input('''
            Rental history is shown above
            >>>Press Enter to return to Main Menu
            ''')
            registered_customer_menu(ctm_id)


# iv. View Detail of Cars to be Rented Out.
def view_car_details(ctm_id):
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()

    #check if customer already has a rented car
    for i in range(len(customer_id)):
        if customer_id[i] == ctm_id:
            if booked_car_name[i] != "none":
                x = input('''
                    Error: You have already rented a car
                    >>> if you have returned the car, please notify an admin to update your data or return the rented car.

                    >>> Press Enter to return to menu
                    ''')
                registered_customer_menu(ctm_id)

    print("\n---All Details of Cars Available for Rent---")
    for i in range(len(car_id)):
        if car_available[i] == "yes":
            print("Car ID: " + car_id[i])
            print("Car Name: " + car_name[i].title())
            print("--Car Details--\n" + (car_details[i].replace(" ", "\n").title()).replace("Price:", "Price Per Day:RM")+"\n")
    print('''
    What would you like to do?
    [1]Book A Car to Rent
    [2]Return to Menu
    ''')
    ctm_option= input("Please Enter Your Option: ")
    while True:
        if ctm_option == "1":
            book_car(ctm_id)

        elif ctm_option == "2":
            registered_customer_menu(ctm_id)

        else:
            ctm_option= input("Please Enter Your Option: ")


# v. Select and Book a car for a specific duration.
def book_car(ctm_id):
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    book_car_id = input(
        "\nTo book a car,\nPlease insert the Car ID: ")
    for i in range(len(car_id)):
        if (book_car_id == car_id[i]):
            print("\nThis is the details of the car chosen:")
            print((car_details[i].replace(" ", "\n").title()).replace("Price:", "Price Per Day:RM"))
            print('''
            What would you like to do?
            [1]Proceed To Payment
            [2]Choose Another Car to Rent
            [3]View Details of Cars Available
            '''
            )
            booking_option= input("Please Enter Your Option: ")
            while True:
                if booking_option == "1":
                    book_payment(book_car_id,ctm_id)

                elif booking_option == "2":
                    book_car(ctm_id)

                elif booking_option == "3":
                    view_car_details(ctm_id)

                else:
                    booking_option= input("Please Enter Your Option: ")


# vi. Do payment to confirm Booking.
def book_payment(book_car_id,ctm_id):
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    try:
        ctm_booking_duration = int(input("How many days would you like to rent the car?: "))
    #validation to make sure customer enters a number
    except ValueError:
        print('''
            ERROR
            >>> Please enter a valid number
            ''')
        book_payment(book_car_id,ctm_id)
    for i in range(len(customer_id)):
        if ctm_id == customer_id[i]:
            for index in range(len(car_id)):
                if (book_car_id == car_id[index]):
                    print("\nYour Credit Card Number: ", customer_card[i])
                    total = (ctm_booking_duration) * int(car_price[index])
                    print(f"Car Name: {car_name[index].title()}")
                    print(f"Number of Days: {ctm_booking_duration}")
                    print(f"Total Payment: RM {total}")
                    print('''
                    What would you like to?
                    [1]Confirm Payment
                    [2]Change Number Of Days To Rent The Car
                    [3]Back To View Details Of Cars Available for Rent
                    '''
                    )
                    payment_option= input("Please Enter Your Option: ")
                    while True:
                        if payment_option == "1":
                            chosen_car = car_name[index]
                            update_data(book_car_id, ctm_id, str(ctm_booking_duration), str(total), chosen_car)
                            x = input(f'''
                            Payment Completed!
                            >>> RM{total} charged to card {customer_card[i]}

                            >>> Press Enter to return to menu
                            ''')
                            registered_customer_menu(ctm_id)

                        elif payment_option == "2":
                            book_payment(book_car_id, ctm_id)

                        elif payment_option == "3":
                            view_car_details(ctm_id)

                        else:
                            payment_option= input("Please Enter Your Option: ")


def update_data(book_car_id, ctm_id, ctm_booking_duration, total, chosen_car):
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()

    year = []
    month = []
    day = []

    date_list = str(date.today()).split("-")
    year.append(date_list[0])
    if date_list[1] == "10":
        month.append(str(date_list[1]))
    else:
        month.append(str(date_list[1].replace("0","")))
    day.append(date_list[2])

    #update history data
    f = open("history.txt", "a+")
    #read data and store into list
    history_data = f.readlines()
    # append to history_data list
    history_data.append(ctm_id + ",")
    history_data.append(book_car_id + ",")
    history_data.append(chosen_car + ",")
    history_data.append(ctm_booking_duration + ",")
    history_data.append(year[0] + ",")
    history_data.append(month[0] + ",")
    history_data.append(day[0] + ",")
    history_data.append(total + "\n")
    #write new data from list into txt file
    f.writelines(history_data)
    f.close()

    for i in range(len(customer_id)):
        if ctm_id == customer_id[i]:
            booked_car_name[i] = chosen_car
            customer_payment[i] = total
            customer_duration[i] = ctm_booking_duration
            #update customer data
            customer_data = open("customer.txt", "w")
            #Use loops to rewrite customer data in text file
            for index in range(len(customer_id)):
                customer_data.write(customer_id[index]+",")
                customer_data.write(customer_pass[index]+",")
                customer_data.write(customer_name[index]+ ",")
                customer_data.write(booked_car_name[index]+",")
                customer_data.write(customer_payment[index]+",")
                customer_data.write(customer_duration[index]+",")
                customer_data.write(customer_card[index]+"\n")
            customer_data.close()

    for i in range(len(car_id)):
            if book_car_id == car_id[i]:
                for index in range(len(customer_id)):
                    if ctm_id == customer_id[index]:
                        booking_customer[i] = customer_name[index]
                car_available[i] = "no"
                ctm_key[i] = ctm_id
                booking_payment[i] = total
                booking_duration[i] = ctm_booking_duration
                payment_year[i] = year[0]
                payment_month[i] = month[0]
                payment_day[i] = day[0]
                #update cars data
                cars_data = open("car.txt", "w")
                #Use loops to rewrite car data in text file
                for l in range(len(car_id)):
                    cars_data.write(car_id[l]+",")
                    cars_data.write(car_name[l]+",")
                    cars_data.write(car_price[l]+",")
                    cars_data.write(car_available[l]+",")
                    cars_data.write(ctm_key[l]+",")
                    cars_data.write(booking_customer[l]+",")
                    cars_data.write(booking_payment[l]+",")
                    cars_data.write(booking_duration[l]+",")
                    cars_data.write(payment_year[l]+",")
                    cars_data.write(payment_month[l]+",")
                    cars_data.write(payment_day[l]+",")
                    cars_data.write(car_details[l]+"\n")
                cars_data.close()

#-----------------------------------------Admin Functions---------------------------------------
#Functionality of Admin
#i. Login to Access System.
def login_admin():
    admin_id, admin_pass = read_admin_data()
    #Prompt user to input admin id and password
    id_num1 = input("\nPlease Enter Your Admin ID :")
    password1 = input("Please Enter Your Admin Password :")

    #Loop to authenticate admin id and password
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
    #Display Admin command line interface
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
            quit()

        #keep prompting user for input if they enter a wrong input
        else:
            option3 = input("Please Enter Your Option :")


# ii.	Add Cars to be rented out
def new_car():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    f = open("car.txt", "a+")
    #read data and store into list
    car_data = f.readlines()
    # prompt user for input of new car details
    new_car_id = ("car" + str(len(car_id)+1))
    new_car_name = input("New Car's Name: ")
    new_car_price = input("New Car's Price: ")
    is_car_available = "yes"
    new_car_details = input("Car details(eg: color:red horsepower:130 price:200):")
    # append to car_data list
    car_data.append(new_car_id + ",")
    car_data.append(new_car_name + ",")
    car_data.append(new_car_price + ",")
    car_data.append(is_car_available + ",")
    car_data.append("none,none,none,none,none,none,none,")
    car_data.append(new_car_details + "\n")
    #write new data into txt file
    f.writelines(car_data)
    f.close()

    x = input('''
    Done !
    >>>Press Enter to return to Admin Menu
    ''')

    admin_menu()


# iii.	Modify Car Details
def modify_car_detail():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    #Prompt user input of carID
    id_input = input(
        "To modify the car detail,\nPlease insert the car ID of the car:")

    #Loop through txt file with car ID to find the matched car
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            #Display current car details
            print("This is the current car detail !\n")
            print(car_id[i])
            print(car_details[i].replace(" ", "\n"))
            new_detail = input(
                "\nWhat is the new color, horsepower and price of the car? eg:(color:** horsepower:** price:**\n")
            car_details[i] = new_detail

            cars_data = open("car.txt", "w")

            #Use loops to rewrite car details in txt file
            for l in range(len(car_id)):
                cars_data.write(car_id[l]+",")
                cars_data.write(car_name[l]+",")
                cars_data.write(car_price[l]+",")
                cars_data.write(car_available[l]+",")
                cars_data.write(ctm_key[l]+",")
                cars_data.write(booking_customer[l]+",")
                cars_data.write(booking_payment[l]+",")
                cars_data.write(booking_duration[l]+",")
                cars_data.write(payment_year[l]+",")
                cars_data.write(payment_month[l]+",")
                cars_data.write(payment_day[l]+",")
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


# vi. Return a Rented Car.
def return_rented_car():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    #prompt input from user to enter car ID
    id_input = input("Please Enter the Car ID of the rented car :")
    #loop through txt file to find cars that are rented out
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            if car_available[i].replace(" ", "") == "no":
                print(
                    "\nPlease Check the details of the customer to return a rented car\n")
                #Display customer, booking and payment data
                print("Customer Name: ", booking_customer[i])
                print("Booking duration (Nth days) : ", booking_duration[i])
                print("Total Payment: ", booking_payment[i])

                #Give user the option to either return to admin menu(if customer details is wrong) or continue
                random_input = input(
                    "\n[1]Back to Admin Menu \nOr press anything to continue . . .")
                if random_input == "1":
                    admin_menu()

                #Clear previous customer data(payment/booking)
                car_available[i] = "yes"
                ctm_key[i] = "none"
                booking_customer[i] = "none"
                booking_duration[i] = "none"
                booking_payment[i] = "none"
                payment_year[i] = "none"
                payment_month[i] = "none"
                payment_day[i] = "none"

                cars_data = open("car.txt", "w")
                #Loop to overwrite the txt file with new data
                for l in range(len(car_id)):
                    cars_data.write(car_id[l]+",")
                    cars_data.write(car_name[l]+",")
                    cars_data.write(car_price[l]+",")
                    cars_data.write(car_available[l]+",")
                    cars_data.write(ctm_key[l]+ ",")
                    cars_data.write(booking_customer[l]+",")
                    cars_data.write(booking_payment[l]+",")
                    cars_data.write(booking_duration[l]+",")
                    cars_data.write(payment_year[l]+",")
                    cars_data.write(payment_month[l]+",")
                    cars_data.write(payment_day[l]+",")
                    cars_data.write(car_details[l]+"\n")

                cars_data.close()
                x = input('''
                Done !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()

    x = input('''
    Incorrect Data entered . . .
    >>> Press Enter to return to Admin Menu. . .
    ''')
    admin_menu()


# display all records of a. Cars Rented Out
def all_rented_car():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\n---All Records of Rented Cars---")
    #loop through txt file to find cars that are not available/rented out
    for i in range(len(car_id)):
        if car_available[i].replace(" ", "") == "no":
            #Display car data, customer and payment data
            print("car id: " + car_id[i])
            print("car name: " + car_name[i])
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("---Car details---\n" + car_details[i])
            #Take booking duration data from txt file and insert into variable as Integer
            add_num = int(booking_duration[i])
            add_num_new = timedelta(add_num)

            #Take payment date data from txt file and insert into variable as Integer
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])
            return_date = date(check_year,check_month,check_day) + add_num_new
            print("The date to return the car: " + str(return_date)+"\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


# Display all records of c. Customer Bookings
def all_customer_booking():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    #loop through txt file to find cars that are booked by customers
    for i in range(len(car_id)):
        if car_available[i].replace(" ", "") == "no":
            #Display customer and car data
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("Booked car's ID: " + car_id[i])
            #Take booking duration data from txt file and insert into variable as Integer
            add_num = int(booking_duration[i])
            add_num_new = timedelta(add_num)

            #Take payment date data from txt file and insert into variable as Integer
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])
            return_date = date(check_year,check_month,check_day) + add_num_new
            print("The date to return the car: " + str(return_date)+ "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


#all records of d. Customer Payment for a specific time duration
def payment_specific_time():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\nPlease Enter a specific time to view all specific payments in 2021: ")
    #prompt for input of year, month ,date
    try:
        start_year,start_month, start_day = int(input("Start Year:")), int(input("Start Month:")), int(input("Start Day:"))
        end_year,end_month, end_day = int(input("End Year:")), int(input("End month:")), int(input("End day:"))
    
    #Validate to ensure an integer is entered
    except ValueError:
        x = input('''
        >>>Value Error . . . Please enter a number
        Press enter to return to admin menu...
        ''')
        admin_menu()


    #fit the input into a variable with date datatype
    start_date = date(start_year,start_month,start_day)
    end_date = date(end_year,end_month,end_day)

    print("\n---All Payments between "  + str(start_date) + " and " + str(end_date) + "---")
    #loop through txt file to find match date
    for i in range(len(car_id)):
        if payment_month[i] != "none":
            #turn datatype of data from str into int
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])

            #fit integers into variable using date class imported to create a date datatype variable
            actual_date = date(check_year,check_month,check_day)

            #Use comparison to find data that its date is between the start and end date
            if start_date < actual_date < end_date:
                print("\nCustomer Name: " + booking_customer[i])
                print("Payment Date\nMonth:" + str(date(check_year,check_month,check_day)))
                print("Total payment: " + booking_payment[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


#v. Search Specific record of
#a. Customer Booking #add date to return car
def specific_booking():
    #fetch data from txt file using the get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("---Please Enter the following specific criteria---")
    #prompt for input on customer name and car ID
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Booking is shown below--")
    #loop to search for similar data comparing txt file & input with (==/is equals to) operator
    for i in range(len(car_id)):
        if booking_customer[i].replace(" ", "") == criteria_customer:
            if car_id[i].replace(" ", "") == criteria_id:
                #Display data obtained from txt file
                print("Customer Name: " + booking_customer[i])
                print("Booked Car: " + car_name[i])
                print("Booked Car ID: " + car_id[i])
                print("Booking Duration: " + booking_duration[i] + "days\n")

                #Take booking duration data from txt file and insert into variable as Integer
                add_num = int(booking_duration[i])
                add_num_new = timedelta(add_num)

                #Take payment date data from txt file and insert into variable as Integer
                check_year = int(payment_year[i])
                check_month = int(payment_month[i])
                check_day = int(payment_day[i])
                return_date = date(check_year,check_month,check_day) + add_num_new
                print("The date to return the car: " + str(return_date))

    x=input('''
    Records of Matched Criteria are shown above !
    >>>Press Enter to return to Admin Menu
    ''')


#v. Search Specific record of
#b. Customer Payement
def specific_payment():
    #fetch data from txt file using the get_data function
    print("---Please Enter the following specific criteria---")
    #prompt input of name data and carID data
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Booking is shown below--")
    #loop to search for similar data comparing txt file & input with (==/is equals to) operator
    for i in range(len(car_id)):
        if booking_customer[i].replace(" ","") == criteria_customer:
            if car_id[i].replace(" ","") == criteria_id:
                #display name and amount of payment of matched criteria
                print("Customer Name: " + booking_customer[i])
                print("Total payment: " + booking_payment[i])

                #Take payment date data from txt file and insert into variable as Integer (from str to int)
                check_year = int(payment_year[i])
                check_month = int(payment_month[i])
                check_day = int(payment_day[i])
                #convert to date datatype
                payment_date = date(check_year,check_month,check_day)
                #display the payment date
                print("Payment done on: " + str(payment_date)+"\n")

    x=input('''
    Records of Matched Criteria are shown above !
    >>>Press Enter to return to Admin Menu
    ''')
    admin_menu()


main_menu()
