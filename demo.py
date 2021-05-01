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
def new_register():
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

new_customer()
