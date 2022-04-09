import helpers.helpers as helpers
import User
def main():
    if __name__ == "__main__":
        print("""
        [------1-Register------]
        [------2-Login--------]
            """)
        user_choice = input("Plese Choose an option: ")
        if user_choice.isnumeric():
            switch = int(user_choice)
            if switch == helpers.menu_items["Register"]:
                User.User.take_info()
            elif switch == helpers.menu_items["Login"]:
                new_user = User.User("","","","","")
                new_user.login()
            else:
                print("please choose 1 or 2")
                main()    
        else:
            print("Please choose a valid input")
            main()    

main()