import helpers.helpers as helpers
import Projects
###########dict menu

def crud_menu(email):
    print("Choose an option: ")
    print("""
    [---1-Create Project---]
    [---2-View Project---]
    [---3-Delete Project---]
    [---4-Edit Project---]
    [---5-Search Project---]
    """)
    user_choice = input("Choose an item: ")
    if user_choice.isnumeric():
        switch = int(user_choice)
        if switch == helpers.crud_items["Create"]:
            Projects.take_inputs(email)
        elif switch == helpers.crud_items["View"]:
            Projects.Projects.view_all()
        elif switch == helpers.crud_items["Delete"]:
            Projects.Projects.delete(email)
        elif switch == helpers.crud_items["Edit"]:            
            Projects.Projects.edit(email)
        elif switch == helpers.crud_items["Search"]:
            data =  Projects.Projects.search()
           
            if data:
                print(data)
            else:
                print("Not found")
        else:
            print("choose from 1 to 5")
            crud_menu(email)        
    else:
        print("please enter a valid input")
        crud_menu(email)        