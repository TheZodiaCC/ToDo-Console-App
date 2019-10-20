import os
import time
import json


class ToDOApp:

    def __init__(self):
        self.clear = "clear"  # For Linux/OS X
        # self.clear = "cls"  #For Windows
        self.version = "1.0"
        self.modification = "20/10/2019"
        self.choice = ""
        self.location = os.path.dirname(os.path.abspath(__file__))

    def main(self):

        os.system(self.clear)
        if os.path.exists(f"{self.location}/list.json"):
            print("List Loaded...\n")

        else:
            f = {"1": "test"}
            with open(f"{self.location}/list.json", "w") as file:
                json.dump(f, file)
            print("List Created...\n")

        # os.system(self.clear)
        print(f"ToDo App {self.version} \n")
        print("1 - Your Tasks \n2 - Add Task \n3 - Remove Task \n4 - About\n5 - Exit")
        self.choice = input("\nYour Choice: ")

        if self.choice == "1":
            ToDOApp.show_tasks(self)

        elif self.choice == "2":
            ToDOApp.add_task(self)

        elif self.choice == "3":
            ToDOApp.delete_task(self)

        elif self.choice == "4":
            ToDOApp.about(self)

        elif self.choice == "5":
            ToDOApp.exit(self)

        else:
            print("Wrong Choice. Try Again")
            time.sleep(1)
            ToDOApp.main(self)

    def show_tasks(self):
        with open(f"{self.location}/list.json") as list:
            elems = json.load(list)

        os.system(self.clear)
        print("Your Tasks:\n")

        for x in elems:
            print(f"{x} - {elems[x]}")

        self.choice = input("\nGo Back: ")

        ToDOApp.main(self)

    def add_task(self):
        with open(f"{self.location}/list.json") as list:
            elems = json.load(list)

        os.system(self.clear)
        print("Add Task - Your Tasks:\n")

        for x in elems:
            print(f"{x} - {elems[x]}")

        self.choice = input("\nDo you want to add new task ? Y/N : ")

        if self.choice == "y" or self.choice == "Y":
            dict_name = input("Name of your task: ")
            dict_content = input("Your Task: ")

            if dict_name in elems:
                self.choice = input("Task already exists. Do you want to replace it ? Y/N : ")

                if self.choice == "y" or self.choice == "Y":
                    d = {}
                    d[dict_name] = dict_content
                    elems.update(d)

                    with open(f"{self.location}/list.json", "w") as file:
                        json.dump(elems, file)

                    print("Task Replaced")
                    time.sleep(1)
                    ToDOApp.main(self)

                elif self.choice == "n" or self.choice == "N":
                    print("Choose a different name")
                    time.sleep(1)
                    ToDOApp.add_task(self)

                else:
                    print("Wrong Choice. Try Again")
                    time.sleep(1)
                    ToDOApp.main(self)

            else:
                d = {}
                d[dict_name] = dict_content
                elems.update(d)

                with open(f"{self.location}/list.json", "w") as file:
                    json.dump(elems, file)

                print("Task Added")
                time.sleep(1)
                ToDOApp.main(self)

        elif self.choice == "n" or self.choice == "N":
            ToDOApp.main(self)

        else:
            print("Wrong Choice. Try Again")
            time.sleep(1)
            ToDOApp.main(self)

    def delete_task(self):
        with open(f"{self.location}/list.json") as list:
            elems = json.load(list)

        os.system(self.clear)
        print(" Delete Task - Your Tasks:\n")

        for x in elems:
            print(f"{x} - {elems[x]}")

        self.choice = input("\nDo you want to remove task ? Y/N : ")

        if self.choice == "y" or self.choice == "Y":
            dict_name = input("Name of task you want to delete: ")

            if dict_name in elems:
                del elems[dict_name]
                print("Task Removed")

                with open(f"{self.location}/list.json", "w") as file:
                    json.dump(elems, file)

                time.sleep(1)
                os.system(self.clear)
                ToDOApp.main(self)
            else:
                print("Task doesn't exist")
                time.sleep(1)
                os.system(self.clear)
                ToDOApp.main(self)

        elif self.choice == "n" or self.choice == "N":
            ToDOApp.main(self)

        else:
            print("Wrong Choice. Try Again")
            time.sleep(1)
            ToDOApp.main(self)

    def about(self):
        os.system(self.clear)
        print(f"ToDo App {self.version} \n")
        print(f"Created By TheZodiaCC \nGitHub https://github.com/TheZodiaCC \nLast Modification {self.modification}")
        self.choice = input("\nGo Back: ")

        ToDOApp.main(self)

    def exit(self):
        print("Bye")
        time.sleep(1)
        exit()


app = ToDOApp()
app.main()