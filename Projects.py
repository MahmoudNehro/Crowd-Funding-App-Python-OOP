import re
class Projects:
    def __init__(self, project_title, Details, total_target, start_date, end_date, email):
        self.project_title = project_title
        self.Details = Details
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date
        self.email = email

    def create_project(self):
        # storing
        file = open('projects.txt', 'a')
        file.write(self.project_title + '|' + self.Details + '|' + self.total_target +
                   '|' + self.start_date + '|' + self.end_date + '|' + self.email + '\n')
        file.close()
    
    @staticmethod
    def view_all():
        try:
            file = open('projects.txt', 'r')
            for project in file:
                projects = project.split('|')
                for i in projects:
                    print(i)
                print("=======================")    


        except FileNotFoundError:
            print("Not found", FileNotFoundError)
            open('projects.txt', 'w')
    @staticmethod        
    def search():
        date_regex='^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        start_date = input("Please enter start date to search: ")
        while not re.search(date_regex,start_date):
            print("Please enter valid date")
            start_date = input("Enter start date: ")
        end_date = input("Please enter end date to search: ")
        while not re.search(date_regex,end_date):
            print("Please enter valid date")
            end_date = input("Enter end date to search: ")  
        file = open('projects.txt', 'r')
        for project in file:
            projects = project.split('|')
            if start_date == projects[3] and end_date == projects[4]:
                return  f"Project title: {projects[0]}, project details: {projects[1]}, total funding: {projects[2]} start_date: {projects[3]} , end_date: {projects[4]}"
        return None    
    @staticmethod
    def edit(email):
        date_regex='^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        old_title = input("Please enter a title: ")
        new_data = []
        try:
            file = open('projects.txt', 'r')
            for project in file:
                projects = project.split('|')
                email1= email + '\n'
                if(old_title==projects[0] and email1 == projects[5]):
                    new_title = input("Enter your project title: ") 
                    file1 = open('projects.txt', 'r')
                    for item in file1:
                        items = item.split('|')
                        while new_title==items[0]:
                            print("title is repeated")
                            new_title = input("Enter your project title: ") 
                    while not new_title.isalpha():
                         print("Please enter a valid title")
                         new_title = input("Enter your project title: ")

                    new_details = input("Enter your project details: ")
                    while not new_details.isalpha():
                        print("Please enter details")
                        new_details = input("Enter your project details: ")

                    new_target = input("Enter your target: ")
                    while not new_target.isnumeric():
                        print("Please enter valid currency")
                        new_target = input("Enter your target: ")

                    new_start_date = input("Enter start date: ")
                    while not re.search(date_regex,new_start_date):
                        print("Please enter valid date")
                        new_start_date = input("Enter start date: ")
                    new_end_date = input("Enter end date: ")
                    while not re.search(date_regex,new_end_date):
                        print("Please enter valid date")
                        new_end_date = input("Enter end date: ")  
                    projects[0] = new_title
                    projects[1]= new_details
                    projects[2]= new_target
                    projects[3]= new_start_date
                    projects[4]= new_end_date
                new_file='|'.join(projects)
                new_data.append(new_file)
            new_data1=''.join(new_data)
            file1 = open('projects.txt', 'w')
            file1.write(new_data1)
            file1.close()
    


        except FileNotFoundError:
            print("Not found", FileNotFoundError)
            open('projects.txt', 'w')
    @staticmethod
    def delete(email):
        old_title = input("Please enter a title: ")
        new_data = []
        try:
            file = open('projects.txt', 'r')
            for project in file:
                projects = project.split('|')
                email1= email + '\n'
                if(old_title==projects[0] and email1 == projects[5]):
                    projects.clear()
                new_file='|'.join(projects)
                new_data.append(new_file)
            new_data1=''.join(new_data)
            file1 = open('projects.txt', 'w')
            file1.write(new_data1)
            file1.close()
    


        except FileNotFoundError:
            print("Not found", FileNotFoundError)
            open('projects.txt', 'w')

def take_inputs(email):
        date_regex = '^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'
        # title
        project_title = input("Enter your project title: ")
        file1 = open('projects.txt', 'r')
        for item in file1:
            items = item.split('|')
            while project_title == items[0]:
                print("Title is repeated! ")
                project_title = input("Enter your project title: ")
        while not project_title.isalpha():
            print("Please enter a valid title")
            project_title = input("Enter your project title: ")
        # details
        Details = input("Enter your project details: ")
        while not Details.isalpha():
            print("Please enter details")
            Details = input("Enter your project details: ")
        # target
        total_target = input("Enter your target: ")
        while not total_target.isnumeric():
            print("Please enter valid currency")
            total_target = input("Enter your target: ")
        # start_date
        start_date = input("Enter start date: ")
        while not re.search(date_regex, start_date):
            print("Please enter valid date")
            start_date = input("Enter start date: ")
        # end_date
        end_date = input("Enter end date: ")
        while not re.search(date_regex, end_date):
            print("Please enter valid date")
            end_date = input("Enter end date: ")
        new_project = Projects(project_title,Details,total_target,start_date,end_date,email)
        new_project.create_project()