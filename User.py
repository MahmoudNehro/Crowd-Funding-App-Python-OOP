import re
import crud_menu as crud
class User:
    def __init__(self,first_name,last_name,email,password,mobile):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile = mobile
    @staticmethod    
    def take_info():
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex_phone = '^01[0-2,5]{1}[0-9]{8}$'
        # first_name ####################
        first_name = input("Enter your first name: ")
        while not first_name.isalpha():
            print("Please enter a valid name")
            first_name = input("Enter your first name: ")
        # last_name ##################
        last_name = input("Enter your last name: ")
        while not last_name.isalpha():
            print("Please enter a valid name")
            last_name = input("Enter your last name: ")
        # email ###########################
        email = input("Enter your email: ")
        file1 = open('users.txt', 'r')
        for item in file1:
            items = item.split('|')
            while email==items[2]:
                print("Email is repeated! ")
                email = input("Enter your email: ") 
        while(not re.search(regex, email)):
            print("Please enter a valid email")
            email = input("Enter your email: ")
        # password  #####################
        password = input("Enter your password: ")
        while len(password) < 8:
            print("Password can't be shorter than 8 characters")
            password = input("Enter your password: ")
        #confirm password #################
        confirm_password = input("confirm your password: ")
        while confirm_password != password:
            print("password doesn't match")
            confirm_password = input("confirm your password: ")
        #mobile phone #################
        mobile = input("enter your mobile: ")
        while not re.search(regex_phone, mobile) :
            print("invalid phone number")
            mobile = input("enter your mobile: ")    
        new_user = User(first_name,last_name,email,password,mobile)
        new_user.store_info()    

    def store_info(self):
        file = open("users.txt", "a")
        file.write(self.first_name + '|' + self.last_name + '|' + self.email + '|' + self.password + '|'+ self.mobile + '\n')
        file.close()
    def login(self):
        self.email = input("Please Enter your email: ")
        self.password = input("Enter your password: ")
        found = False
        try:
            file = open('users.txt', 'r')
            for user in file:
                users = user.split('|')
                if (users[2] == self.email) and (users[3] == self.password):
                    found = True

        except FileNotFoundError:
            print("Not found", FileNotFoundError)
            open('users.txt', 'w')
   
        if found:
            print("========Valid Login!========")
            crud.crud_menu(self.email)
        else:
            print("Invalid, try again or register")

        