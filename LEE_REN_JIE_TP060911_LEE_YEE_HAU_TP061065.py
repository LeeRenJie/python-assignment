# LEE REN JIE
# TP060911
# LEE YEE HAU
# TP061065

# import date and timedelta from datetime module
from datetime import date, timedelta

# Main menu, Ask identity of end user, either Customer or Admin
def main_menu():
    # Display today's date
    print(date.today())
    # Display options for end users
    print('''
    -------Who are you?-------\n
    [1]Customer
    [2]Admin
    [3]Exit\n
    ''')

    # Receive input from end user
    option = input("Please Enter Your Option: ")

    # Call functions based on end user's input
    while True:
        if option == "1":
            customer_menu()
        elif option == "2":
            login_admin()
        # Exit program
        elif option == "3":
            quit()
        # Validate user's input if none of the option is entered
        else:
            option = input("Please Enter Your Option: ")


# --------------------------------------ADMIN DATA OPERATIONS----------------------------------------
# Read data for admin and return the data in lists
def read_admin_data():
    # Open admin text file in read mode
    admin_data = open("admin.txt", "r")
    # Read all lines in admin text file
    lines = admin_data.readlines()

    # Create empty list for each type of data in admin text file
    admin_id = []
    admin_pass = []

    # Append each type of data in their respective lists
    for admin in lines:
        admin_list = admin.split(" ")
        admin_id.append(admin_list[0])
        admin_pass.append(admin_list[1].replace("\n", ""))

    # Return lists to be used in other functions to access the data
    return admin_id, admin_pass


# ---------------------------------------CUSTOMER DATA OPERATIONS-------------------------------------------------
# Read data for customer and return the data in lists
def read_customer_data():
    # Open customer text file in read mode
    customer_data = open("customer.txt", "r")
    # Read all lines in customer text file
    lines = customer_data.readlines()

    # Create empty list for each type of data in customer text file
    customer_id = []
    customer_pass = []
    customer_name = []
    booked_car_name = []
    customer_payment = []
    customer_duration = []
    customer_card = []

    # Append each type of data in their respective lists
    for customer in lines:
        customer_list = customer.split(",")
        customer_id.append(customer_list[0])
        customer_pass.append(customer_list[1])
        customer_name.append(customer_list[2])
        booked_car_name.append(customer_list[3])
        customer_payment.append(customer_list[4])
        customer_duration.append(customer_list[5])
        customer_card.append(customer_list[6].replace("\n", ""))

    # Return lists to be used in other functions to access the data
    # Destructure number of lists returned from get_data function
    return customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card


# ---------------------------------------CAR DATA OPERATIONS-------------------------------------------------------
# Read data for car and return the data in lists
def read_car_data():
    # Open car text file in read mode
    car_data = open("car.txt", "r")
    # Read all lines in car text file
    lines = car_data.readlines()

    # Create empty list for each type of data in car text file
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

    # Append each type of data in their respective lists
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

    # Return lists to be used in other functions to access the data
    return car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details


# --------------------------------------RENTAL HISTORY OPERATIONS----------------------------------------
# Read data for rental history and return the data in lists
def read_history_data():
    # Open rental history text file in read mode
    history_data = open("history.txt", "r")
    # Read all lines in history text file
    lines = history_data.readlines()

    # Create empty list for each type of data in history text file
    ctm_history_id = []
    car_history_id = []
    car_history_name = []
    rental_duration = []
    history_year = []
    history_month = []
    history_day = []
    price_paid = []

    # Append each type of data in their respective lists
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

    # Return lists to be used in other functions to access the data
    return ctm_history_id, car_history_id, car_history_name, car_history_name, rental_duration, history_year, history_month, history_day, price_paid


#----------------------------------------CUSTOMER FUNCTIONS-------------------------------------
# Customer menu for non-registered customers
def customer_menu():
    # Display options for non-registered customers
    print('''
    -------Welcome To The Customer Menu-------\n
    [1]Log in as a Customer
    [2]Register as a New Customer
    [3]View All Cars Available for rent
    [4]Back to Main Menu\n
    ''')

    # Receive input from non-registered customers
    option2 = input("Please Enter Your Option: ")

    # Call functions based on input
    while True:
        if option2 == "1":
            login_customer()
        elif option2 == "2":
            new_customer()
        elif option2 == "3":
            view_car_available("1")
        elif option2 =="4":
            main_menu()
        # Validate user's input if none of the option is entered
        else:
            option2 = input("Please Enter Your Option: ")


# View all record of cars available for rent
# Receive a number as argument as this function is used by both non-registered customer and admin
def view_car_available(number):
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\n---All Records of Cars Available for Rent---\n")
    # Loop to display all cars available based on their data for "car_available"
    for i in range(len(car_id)):
        if car_available[i] == "yes":
            print("Car ID: " + car_id[i])
            print("Car Name: " + car_name[i].title())
            print("--Car Details--\n" + (car_details[i].replace(" ","\n")).title()+"\n")

    # Based on the number passed in by both customer menu or admin menu, different output is shown and returned to different menus
    if number == "1":
        x = input('''
        Records are shown above
        >>>Press Enter to return to Customer menu
        ''')
        customer_menu()

    elif number == "2":
        x = input('''
        Records are shown above
        >>>Press Enter to return to Admin Menu
        ''')
        admin_menu()


# New customer register with their name, password and credit card number to access other functions
def new_customer():
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()

    # Customer data file is opened in read and append mode to add in new customers in new line
    f = open("customer.txt", "a+")
    customer_data = f.readlines()
    # Automatically sets ID for customer to prevent duplication
    new_ctm_id = ("ctm"+str(len(customer_id)+1))
    # Receive new customer's data
    new_ctm_name = input("Your Name: ")
    new_ctm_pass = input("Your Password: ")
    #validation to make sure customer enters a number
    try:
        new_ctm_card = int(input("Your Credit Card Number: "))
        if (len(str(new_ctm_card)) != 16):
            print("Please enter only 16 numbers\n")
            new_customer()
    # Returns error if not an integer is entered
    except ValueError:
        print('''
            ERROR
            >>> Please enter a valid credit card number without characters or decimals
            ''')
        # Repeat execution of this function to ask for the right credit card number
        new_customer()
    # Append new data to car_data list
    customer_data.append(new_ctm_id + ",")
    customer_data.append(new_ctm_pass + ",")
    customer_data.append(new_ctm_name.lower() + ",")
    customer_data.append("none,none,none,")
    customer_data.append(str(new_ctm_card) + "\n")
    # Write new data into customer text file and close file
    f.writelines(customer_data)
    f.close()
    # Show customer their new ID and return back to menu
    x = input(f'''
    Your New Customer ID is {new_ctm_id}\n
    Register is successful!
    >>>Press Enter to return to Customer Menu
    ''')
    customer_menu()


# Login to Access more functions as a registered customer
def login_customer():
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    # Prompt customer for ID
    ctm_id_input = input("Please Enter Your ID: ")
    # Loop to check existing ID with customer inpuut
    for i in range(len(customer_id)):
        if customer_id[i] == ctm_id_input:
            # Prompt customer for password if ID found
            ctm_password_input = input("Please Enter Your Password: ")
            # If ID and password  are correct, customer will be authorized to use the registered customer menu
            if ctm_password_input == customer_pass[i]:
                # customer_id is passed in as argument to ensure the same customer is using the program unless logged out
                registered_customer_menu(ctm_id_input)
            # If password is wrong, customer will be directed back to the customer menu
            else:
                x = input('''\n
                Wrong Password Entered
                >>> Press enter to return back to Customer Menu . . .
                ''')
                customer_menu()
        # if the customer_id does not exist after looping, customer is directed back to customer menu
        elif i == (len(customer_id)-1):
            x = input('''\n
            Customer ID Not Found
            >>> Press enter to return back to Customer Menu . . .
            ''')
            customer_menu()


# After customer has login, registered customer menu interface is displayed
def registered_customer_menu(ctm_id):
    # Options displayed
    print('''
    -------Registered Customer Menu-------\n
    What would you like to do?
    [1]Modify Personal Details
    [2]View Details of Cars for Rent, Book a car and Pay
    [3]View Personal Rental History
    [4]Return to Main Menu
    [5]Exit\n
    ''')

    # Prompt User for their option
    option3 = input("Please Enter Your Option: ")
    while True:
        # Pass in customer ID (ctm_id) as argument for functions
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
        # Validate user's input if none of the option is entered
        else:
            option3 = input("Please Enter Your Option: ")


# Modify Personal Details for registered customer.
def modify_customer_detail(ctm_id):
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()

    # Loop through to check if the customer_id is same with the login ID and customer password is for that customer
    for i in range(len(customer_id)):
        if ctm_id == customer_id[i]:
            # Display customer current details
            print("\nThis is your current detail:")
            print("ID:", customer_id[i])
            print("Name:", customer_name[i].title())
            print("Password:", customer_pass[i])
            print("Card Number:", customer_card[i])
            # Prompt customer for the details they would like to modify
            print('''
            What would you like to modify?
            *Note that the ID is auto generated and can't be changed
            [1]Name
            [2]Password
            [3]Card Number
            [4]Back To Menu
            ''')

            modify_option = input("Please Enter Your Option: ")

            # Function to modify data in customer text file
            def change_customer_data():
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

            while True:
                # Ask for new details based on customer's previous option and call function to change data in text file
                if modify_option == "1":
                    new_name = input("\nWhat would you like to be called: ")
                    customer_name[i] = new_name.lower()
                    change_customer_data()

                elif modify_option == "2":
                    new_password = input("\nWhat is your new password: ")
                    customer_pass[i] = new_password
                    change_customer_data()

                elif modify_option == "3":
                    #validation to make sure customer enters a number
                    try:
                        new_card = int(input("\nWhat is your new card number(16 numbers): "))
                        if (len(str(new_card)) != 16):
                            print("Please enter only 16 numbers")
                            modify_customer_detail(ctm_id)
                        else:
                            customer_card[i] = str(new_card)
                            change_customer_data()
                    # Returns error if not an integer is entered
                    except ValueError:
                        print('''
                            ERROR
                            >>> Please enter a valid credit card number without characters or decimals
                            ''')
                        # Repeat execution of this function to ask for the right credit card number again
                        modify_customer_detail(ctm_id)

                elif modify_option == "4":
                    registered_customer_menu(ctm_id)
                # Validate user's input if none of the option is entered
                else:
                    modify_option = input("Please Enter Your Option: ")


# View Personal Rental History of customer.
def rental_history(ctm_id):
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    ctm_history_id, car_history_id, car_history_name, car_history_name, rental_duration, history_year, history_month, history_day, price_paid = read_history_data()
    # Loop through customer_id to find the specific customer based on their login ID passed as argument
    for i in range(len(customer_id)):
        if customer_id[i] == ctm_id:
            print("Your ID:", customer_id[i])
            print("Your Name:", customer_name[i])
            print("\n-------------Rental History-------------")
            # Loop through the history text file to search for customer ID that is the same with the login customer ID
            for index in range(len(ctm_history_id)):
                # Display rental history if customer ID is found in history text file
                if ctm_history_id[index] == ctm_id:
                    print("Car ID:", car_history_id[index])
                    print("Car Name:", car_history_name[index].title())
                    print("Rental Cost:RM", price_paid[index])
                    print(f"Duration: {rental_duration[index]} days")
                    print(f"Rented On: {history_day[index]}-{history_month[index]}-{history_year[index]}\n")
                # If no history found
                elif (ctm_history_id[index] != ctm_id) and (index == (len(ctm_history_id)-1)) :
                    x = input('''
                    No Rental history is found
                    >>>Press Enter to return to Main Menu
                    ''')
                    registered_customer_menu(ctm_id)
            # Customer is then directed to return to registered customer menu
            x = input('''
            Rental history is shown above
            >>>Press Enter to return to Main Menu
            ''')
            registered_customer_menu(ctm_id)


# View Detail of Cars to be Rented Out
def view_car_details(ctm_id):
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()

    # Check if customer already has a rented car to prevent complication
    for i in range(len(customer_id)):
        if customer_id[i] == ctm_id:
            # If the booked_car_name is not none, the customer has already rent a car
            if booked_car_name[i] != "none":
                # Directs customer to return to registered customer menu if data shows a car is rented
                x = input('''
                    Error: You have already rented a car
                    >>> if you have returned the car, please notify an admin to update your data or return the rented car.

                    >>> Press Enter to return to menu
                    ''')
                registered_customer_menu(ctm_id)

    # If customer has not rented a car, display details of available car
    print("\n---All Details of Cars Available for Rent---")
    for i in range(len(car_id)):
        if car_available[i] == "yes":
            print("Car ID: " + car_id[i])
            print("Car Name: " + car_name[i].title())
            print("--Car Details--\n" + (car_details[i].replace(" ", "\n").title()).replace("Price:", "Price Per Day:RM")+"\n")
    # Prompt to get customer's option
    print('''
    What would you like to do?
    [1]Book A Car to Rent
    [2]Return to Menu
    ''')
    ctm_option= input("Please Enter Your Option: ")
    while True:
        # Call functions based on customer option and pass in customer ID as argument.
        if ctm_option == "1":
            book_car(ctm_id)
        elif ctm_option == "2":
            registered_customer_menu(ctm_id)
        # Validate user's input if none of the option is entered
        else:
            ctm_option= input("Please Enter Your Option: ")


# Select and Book a car for a specific duration.
def book_car(ctm_id):
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    # Prompt user to input car ID that they are interested to rent
    book_car_id = input(
        "\nTo book a car,\nPlease insert the Car ID: ")
    # Loop through car text file to find the data for that specific car
    for i in range(len(car_id)):
        if (book_car_id == car_id[i] and car_available[i] == "yes"):
            # Display details of car
            print("\nThis is the details of the car chosen:")
            print((car_details[i].replace(" ", "\n").title()).replace("Price:", "Price Per Day:RM"))
            # Prompt customer for their option
            print('''
            What would you like to do?
            [1]Proceed To Payment
            [2]Choose Another Car to Rent
            [3]View Details of Cars Available
            '''
            )
            booking_option= input("Please Enter Your Option: ")
            # Call functions based on their option and pass in arguments that are needed
            while True:
                if booking_option == "1":
                    book_payment(book_car_id,ctm_id)

                elif booking_option == "2":
                    book_car(ctm_id)

                elif booking_option == "3":
                    view_car_details(ctm_id)
                # Validate user's input if none of the option is entered
                else:
                    booking_option= input("Please Enter Your Option: ")
        elif (car_available[i] == "no" and car_id[i] == book_car_id):
            print("\nCar is not available for rent or does not exist")

# Do payment to confirm booking.
def book_payment(book_car_id,ctm_id):
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    #validation to make sure customer enters a number
    try:
        ctm_booking_duration = int(input("How many days would you like to rent the car?: "))
    # Validate to ensure an integer is entered
    except ValueError:
        print('''
            ERROR
            >>> Please enter a valid or whole number
            ''')
        # Repeat execution of this function to ask for duration to rent again
        book_payment(book_car_id,ctm_id)
    # Loop through customer ID to find the specific customer
    for i in range(len(customer_id)):
        if ctm_id == customer_id[i]:
            # If customer ID found, loop through car ID to find the specific car the customer is interested
            for index in range(len(car_id)):
                if (book_car_id == car_id[index]):
                    # Display information for payment
                    print("\nYour Credit Card Number: ", customer_card[i])
                    total = ctm_booking_duration * int(car_price[index])
                    print(f"Car Name: {car_name[index].title()}")
                    print(f"Number of Days: {ctm_booking_duration}")
                    print(f"Total Payment: RM {total}")
                    # Prompt customer for their option
                    print('''
                    What would you like to do?
                    [1]Confirm Payment
                    [2]Change Number Of Days To Rent The Car
                    [3]Back To View Details Of Cars Available for Rent
                    '''
                    )
                    payment_option= input("Please Enter Your Option: ")
                    while True:
                        # Call functions based on customer's option
                        if payment_option == "1":
                            chosen_car = car_name[index]
                            # Call update_data function to update all related files after customer confirmed to rent
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
                        # Validate user's input if none of the option is entered
                        else:
                            payment_option= input("Please Enter Your Option: ")

# Update data after payment
def update_data(book_car_id, ctm_id, ctm_booking_duration, total, chosen_car):
    # Destructure number of lists returned from get_data function
    customer_id, customer_pass, customer_name, booked_car_name, customer_payment, customer_duration, customer_card = read_customer_data()
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()

    # Get current year, month, and day at the time when user rent the car
    year = []
    month = []
    day = []

    # Append each data into a list
    date_list = str(date.today()).split("-")
    year.append(date_list[0])
    #use if comparison to avoid error for leading zeroes of month
    if date_list[1] == "10":
        month.append(str(date_list[1]))
    else:
        month.append(str(date_list[1].replace("0","")))
    day.append(date_list[2])

    # Update history data
    f = open("history.txt", "a+")
    # Read data and store into list
    history_data = f.readlines()
    # Append to history_data list
    history_data.append(ctm_id + ",")
    history_data.append(book_car_id + ",")
    history_data.append(chosen_car + ",")
    history_data.append(ctm_booking_duration + ",")
    history_data.append(year[0] + ",")
    history_data.append(month[0] + ",")
    history_data.append(day[0] + ",")
    history_data.append(total + "\n")
    # Write new data from list into txt file
    f.writelines(history_data)
    f.close()

    # Update customer data
    for i in range(len(customer_id)):
        if ctm_id == customer_id[i]:
            booked_car_name[i] = chosen_car
            customer_payment[i] = total
            customer_duration[i] = ctm_booking_duration
            customer_data = open("customer.txt", "w")
            # Use loop to rewrite customer data in text file
            for index in range(len(customer_id)):
                customer_data.write(customer_id[index]+",")
                customer_data.write(customer_pass[index]+",")
                customer_data.write(customer_name[index]+ ",")
                customer_data.write(booked_car_name[index]+",")
                customer_data.write(customer_payment[index]+",")
                customer_data.write(customer_duration[index]+",")
                customer_data.write(customer_card[index]+"\n")
            customer_data.close()

    # Update customer data
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
                        cars_data = open("car.txt", "w")
                        # Use loop to rewrite car data in text file
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
# Login to Access System.
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
    Press enter to return back to main menu . . .
    ''')
    main_menu()


# After the login as an admin, admin menu interface
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
            view_car_available("2")

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

        # Validate user's input if none of the option is entered
        else:
            option3 = input("Please Enter Your Option :")


# Add Cars to be rented out
def new_car():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    f = open("car.txt", "a+")
    # Read data and store into list
    car_data = f.readlines()
    # Prompt user for input of new car details
    new_car_id = ("car" + str(len(car_id)+1))
    new_car_name = input("New Car's Name: ").lower()
    is_car_available = "yes"
    color = input("What is the color of the car?:")
    try:
        horsepower = int(input("What is the Horsepower of the car?:"))
        price = int(input("What is the price of the car rental?:"))
    # Validate to ensure an integer is entered
    except ValueError:
        x = input('''
        >>>Value Error . . . Please enter a number
        Press enter to return to admin menu...
        ''')
        admin_menu()
    new_car_details = ("color:" + color + " horsepower:" + str(horsepower) + " price:" + str(price))
    # Append to car_data list
    car_data.append(new_car_id + ",")
    car_data.append(new_car_name + ",")
    car_data.append(str(price) + ",")
    car_data.append(is_car_available + ",")
    car_data.append("none,none,none,none,none,none,none,")
    car_data.append(new_car_details + "\n")
    # Write new data into txt file
    f.writelines(car_data)
    f.close()

    x = input('''
    Done !
    >>>Press Enter to return to Admin Menu
    ''')

    admin_menu()


# Modify Car Details
def modify_car_detail():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    # Prompt user input of carID
    id_input = input(
        "To modify the car detail,\nPlease insert the car ID of the car:")

    # Loop through txt file with car ID to find the matched car
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            # Display current car details
            print("\n" + car_id[i])
            print("car name: " + car_name[i])
            print("--This is the current car details !--")
            print(car_details[i].replace(" ", "\n"))
            #prompt for input of new car details
            color = input("What is the color of the car?:")
            try:
                horsepower = int(input("What is the Horsepower of the car?:"))
                price = int(input("What is the price of the car rental?:"))
            # Validate to ensure an integer is entered
            except ValueError:
                x = input('''
                >>>Value Error . . . Please enter a number
                Press enter to return to admin menu...
                ''')
                admin_menu()
            new_detail = ("color:" + color + " horsepower:" + str(horsepower) + " price:" + str(price))
            car_price[i] = str(price)
            car_details[i] = new_detail

            cars_data = open("car.txt", "w")

            # Use loops to rewrite car details in txt file
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
    >>>Press enter to return to Admin Menu . . .
    ''')
    admin_menu()


# Return a Rented Car.
def return_rented_car():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    # Prompt input from user to enter car ID
    id_input = input("Please Enter the Car ID of the rented car :")
    # Loop through txt file to find cars that are rented out
    for i in range(len(car_id)):
        if id_input == car_id[i]:
            if car_available[i].replace(" ", "") == "no":
                print(
                    "\nPlease Check the details of the customer to return a rented car\n")
                # Display customer, booking and payment data
                print("Customer Name: ", booking_customer[i])
                print("Booking duration (Nth days) : ", booking_duration[i])
                print("Total Payment: ", booking_payment[i])

                # Give user the option to either return to admin menu(if customer details is wrong) or continue
                random_input = input(
                    "\n[1]Back to Admin Menu \nOr press anything to continue . . .")
                if random_input == "1":
                    admin_menu()

                # Clear previous customer data(payment/booking)
                car_available[i] = "yes"
                ctm_key[i] = "none"
                booking_customer[i] = "none"
                booking_duration[i] = "none"
                booking_payment[i] = "none"
                payment_year[i] = "none"
                payment_month[i] = "none"
                payment_day[i] = "none"

                cars_data = open("car.txt", "w")
                # Loop to overwrite the txt file with new data
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


# Display all records of Cars Rented Out
def all_rented_car():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\n---All Records of Rented Cars---")
    # Loop through txt file to find cars that are not available/rented out
    for i in range(len(car_id)):
        if car_available[i].replace(" ", "") == "no":
            # Display car data, customer and payment data
            print("car id: " + car_id[i])
            print("car name: " + car_name[i])
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("---Car details---\n" + car_details[i])
            # Take booking duration data from txt file and insert into variable as Integer
            add_num = int(booking_duration[i])
            add_num_new = timedelta(add_num)

            # Take payment date data from txt file and insert into variable as Integer
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])
            return_date = date(check_year,check_month,check_day) + add_num_new
            print("The date to return the car: " + str(return_date)+"\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


# Display all records of c. Customer Bookings
def all_customer_booking():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\n---All records of Customer bookings---")
    # Loop through txt file to find cars that are booked by customers
    for i in range(len(car_id)):
        if car_available[i].replace(" ", "") == "no":
            # Display customer and car data
            print("customer name: " + booking_customer[i])
            print("Total payment: " + booking_payment[i])
            print("Booking Duration (Nth day): " + booking_duration[i])
            print("Booked car's ID: " + car_id[i])
            #Take booking duration data from txt file and insert into variable as Integer
            add_num = int(booking_duration[i])
            add_num_new = timedelta(add_num)

            # Take payment date data from txt file and insert into variable as Integer
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])
            return_date = date(check_year,check_month,check_day) + add_num_new
            print("The date to return the car: " + str(return_date)+ "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


# All records of Customer Payment for a specific time duration
def payment_specific_time():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("\nPlease Enter a specific time to view all specific payments in 2021: ")
    # Prompt for input of year, month ,date
    try:
        start_year,start_month, start_day = int(input("Start Year:")), int(input("Start Month:")), int(input("Start Day:"))
        end_year,end_month, end_day = int(input("End Year:")), int(input("End month:")), int(input("End day:"))

    # Validate to ensure an integer is entered
    except ValueError:
        x = input('''
        >>>Value Error . . . Please enter a number
        Press enter to return to admin menu...
        ''')
        admin_menu()


    # Fit the input into a variable with date datatype
    start_date = date(start_year,start_month,start_day)
    end_date = date(end_year,end_month,end_day)

    print("\n---All Payments between "  + str(start_date) + " and " + str(end_date) + "---")
    # Loop through txt file to find match date
    for i in range(len(car_id)):
        #Use If comparison to avoid error for data that has no payment date
        if payment_month[i] != "none":
            # Turn datatype of data from str into int
            check_year = int(payment_year[i])
            check_month = int(payment_month[i])
            check_day = int(payment_day[i])

            # Fit integers into variable using date class imported to create a date datatype variable
            actual_date = date(check_year,check_month,check_day)

            # Use comparison to find data that its date is between the start and end date
            if start_date < actual_date < end_date:
                print("\nCustomer Name: " + booking_customer[i])
                print("Payment Date:" + str(actual_date))
                print("Total payment: " + booking_payment[i] + "\n")

    x = input("\nPress Enter to return to admin menu . . .")
    admin_menu()


# Specific record of Customer Booking, add date to return car
def specific_booking():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("---Please Enter the following specific criteria---")
    # Prompt for input on customer name and car ID
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Booking is shown below--")
    # Loop to search for similar data comparing txt file & input with (==/is equals to) operator
    for i in range(len(car_id)):
        if booking_customer[i].replace(" ", "") == criteria_customer:
            if car_id[i].replace(" ", "") == criteria_id:
                # Display data obtained from txt file
                print("Customer Name: " + booking_customer[i])
                print("Booked Car: " + car_name[i])
                print("Booked Car ID: " + car_id[i])
                print("Booking Duration: " + booking_duration[i] + "days\n")

                # Take booking duration data from txt file and insert into variable as Integer
                add_num = int(booking_duration[i])
                add_num_new = timedelta(add_num)

                # Take payment date data from txt file and insert into variable as Integer
                check_year = int(payment_year[i])
                check_month = int(payment_month[i])
                check_day = int(payment_day[i])
                return_date = date(check_year,check_month,check_day) + add_num_new
                print("The date to return the car: " + str(return_date))

                x=input('''
                Records of Matched Criteria are shown above !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()
    x=input('''
    No records are found with the given criteria!
    >>>Press Enter to return to Admin Menu
    ''')
    admin_menu()


# Search Specific record of Customer Payement
def specific_payment():
    # Destructure number of lists returned from get_data function
    car_id, car_name, car_price, car_available, ctm_key, booking_customer, booking_payment, booking_duration, payment_year, payment_month, payment_day, car_details = read_car_data()
    print("---Please Enter the following specific criteria---")
    # Prompt input of name data and carID data
    criteria_customer = input("customer name: ")
    criteria_id = input("Booked Car Id: ")

    print("\n--Records of Customer Payment is shown below--")
    # Loop to search for similar data comparing txt file & input with (==/is equals to) operator
    for i in range(len(car_id)):
        if booking_customer[i].replace(" ","") == criteria_customer:
            if car_id[i].replace(" ","") == criteria_id:
                # Display name and amount of payment of matched criteria
                print("Customer Name: " + booking_customer[i])
                print("Total payment: " + booking_payment[i])

                # Take payment date data from txt file and insert into variable as Integer (from str to int)
                check_year = int(payment_year[i])
                check_month = int(payment_month[i])
                check_day = int(payment_day[i])
                # Convert to date datatype
                payment_date = date(check_year,check_month,check_day)
                # Display the payment date
                print("Payment done on: " + str(payment_date)+"\n")

                x=input('''
                Records of Matched Criteria are shown above !
                >>>Press Enter to return to Admin Menu
                ''')
                admin_menu()
    x=input('''
    No records are found with the given criteria!
    >>>Press Enter to return to Admin Menu
    ''')
    admin_menu()


main_menu()
