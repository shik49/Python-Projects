"""
Health Management system
File I/O system
This python project keeps the track of health of 3 clients by keeping the time record of the meal given to the clients
and exercise done by the clients
3 clients - Harry, Rohan and Hammad
output - 3 files for food and 3 files for exercise

"""


import datetime
i = True
while i == True:
    def getdate():
         return datetime.datetime.now()


    def harry():
        print("choose the record\n1. Food\n2. Exercise")
        act = int(input("Enter the serial number of record: "))
        if act == 1:
            data = input("Please select \"e\" to enter the record and \"r\" to retrieve the record")
            food_harry = open("food_harry.txt", "r+")
            if data == "e":
                ans = "y"
                while ans == "y":
                    rec_food = input("Enter the food record: ")
                    time = ["\n[", str((getdate())), "] "]
                    # print(time)
                    food_harry.writelines(time)
                    food_harry.write(rec_food)
                    ans = input("Do you want to enter another record: \"y\" for yes and \"n\" for no: ")
                    print("The data is entered successfully")
            elif data == "r":
                print(food_harry.read())
            food_harry.close()
        elif act == 2:
            data = input("Please select \"e\" to enter the record and \"r\" to retrieve the record")
            exer_harry = open("exer_harry.txt", "r+")
            if data == "e":
                ans = "y"
                while ans == "y":
                    rec_exer = input("Enter the Exercise record: ")
                    time = ["\n[", str((getdate())), "] "]
                    # print(time)
                    exer_harry.writelines(time)
                    exer_harry.write(rec_exer)
                    ans = input("Do you want to enter another record: \"y\" for yes and \"n\" for no: ")
                    print("The data is entered successfully")
            elif data == "r":
                print(exer_harry.read())
            exer_harry.close()

    def rohan():
        print("choose the record\n1. Food\n2. Exercise")
        act = int(input("Enter the serial number of record: "))
        if act == 1:
            data = input("Please select \"e\" to enter the record and \"r\" to retrieve the record")
            food_rohan = open("food_rohan.txt", "w+")
            if data == "e":
                ans = "y"
                while ans == "y":
                    rec_food = input("Enter the food record: ")
                    time = ["\n[", str((getdate())), "] "]
                    # print(time)
                    food_rohan.writelines(time)
                    food_rohan.write(rec_food)
                    ans = input("Do you want to enter another record: \"y\" for yes and \"n\" for no: ")
                    print("The data is entered successfully")
            elif data == "r":
                print(food_rohan.read())
            food_rohan.close()
        elif act == 2:
            data = input("Please select \"e\" to enter the record and \"r\" to retrieve the record")
            exer_rohan = open("exer_rohan.txt", "w+")
            if data == "e":
                ans = "y"
                while ans == "y":
                    rec_exer = input("Enter the Exercise record: ")
                    time = ["\n[", str((getdate())), "] "]
                    # print(time)
                    exer_rohan.writelines(time)
                    exer_rohan.write(rec_exer)
                    ans = input("Do you want to enter another record: \"y\" for yes and \"n\" for no: ")
                    print("The data is entered successfully")
            elif data == "r":
                print(exer_rohan.read())
            exer_rohan.close()

    def hammad():
        print("choose the record\n1. Food\n2. Exercise")
        act = int(input("Enter the serial number of record: "))
        if act == 1:
            data = input("Please select \"e\" to enter the record and \"r\" to retrieve the record")
            food_hammad = open("food_hammad.txt", "w+")
            if data == "e":
                ans = "y"
                while ans == "y":
                    rec_food = input("Enter the food record: ")
                    time = ["\n[", str((getdate())), "] "]
                    # print(time)
                    food_hammad.writelines(time)
                    food_hammad.write(rec_food)
                    ans = input("Do you want to enter another record: \"y\" for yes and \"n\" for no: ")
                    print("The data is entered successfully")
            elif data == "r":
                print(food_hammad.read())
            food_hammad.close()
        elif act == 2:
            data = input("Please select \"e\" to enter the record and \"r\" to retrieve the record")
            exer_hammad = open("exer_hammad.txt", "w+")
            if data == "e":
                ans = "y"
                while ans == "y":
                    rec_exer = input("Enter the Exercise record: ")
                    time = ["\n[", str((getdate())), "] "]
                    # print(time)
                    exer_hammad.writelines(time)
                    exer_hammad.write(rec_exer)
                    ans = input("Do you want to enter another record: \"y\" for yes and \"n\" for no: ")
                    print("The data is entered successfully")
            elif data == "r":
                print(exer_hammad.read())
            exer_hammad.close()


    print("Welcome to Health Management System\n")
    print("1. List of clients\n2.Exit\n")
    ask = int(input("Select the serial number of the action: "))
    if ask == 1:
        print("Your clients are: \n1. Harry\n2. Rohan\n3. Hammad")
        client = int(input("Enter the respective serial number to select the client: "))
        if client == 1:
            harry()
        elif client == 2:
            rohan()
        elif client == 3:
            hammad()
    elif ask == 2:
        break
#
# try:
#     name = input("What is your name: ")
#     place = input("Where are you from")

except:
print("YOu have entered the wrong: ")
