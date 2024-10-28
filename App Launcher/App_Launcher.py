import subprocess as sub
import sqlite3 as sql
from colorama import init, Fore

# Initialize colorama
init()

# Connect to the database
db = sql.connect("app.db")
cursor = db.cursor()

# Create the table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS app (name_app TEXT, app_url TEXT)")

print("*** WELCOME TO THE APPLICATION ***")
options = (Fore.LIGHTCYAN_EX + "1- View Applications" + Fore.RESET + 
           Fore.LIGHTBLACK_EX + "\n2- Open Application" + Fore.RESET + 
           Fore.LIGHTGREEN_EX + "\n3- Add Application" + Fore.RESET)

def view_applications():
    print("-" * 30)
    cursor.execute("SELECT * FROM app")
    records = cursor.fetchall()
    if not records:
        print("No applications added.")
    else:
        for record in records:
            print(f'Your applications: {record[0]}')
    input("Press ENTER to continue: ")
    print("-" * 30)

def open_application():
    print("-" * 30)
    cursor.execute("SELECT * FROM app")
    records = cursor.fetchall()
    for record in records:
        print(f'Your applications: {record[0]}')
    selected_app = input("Please enter the name of the application you want to open: ").capitalize()
    app_found = False
    for name, url in records:
        if selected_app == name:
            sub.call(url)
            app_found = True
            print("-" * 30)
            input("Press ENTER to exit: ")
            break
    if not app_found:
        print("Application not found, please add it.")
        input("Press ENTER to continue: ")
    print("-" * 30)

def add_application():
    num_applications = int(input("How many applications do you want to add? Enter '0' if none: "))
    print("-" * 30)
    if num_applications == 0:
        print("No applications added")
        input("Press ENTER to continue: ")
    else:
        for _ in range(num_applications):
            app_name = input("Please enter the name of the application you want to add: ").capitalize()
            app_url = input("Please enter the URL of the application: ")
            cursor.execute('INSERT INTO app (name_app, app_url) VALUES (?, ?)', (app_name, app_url))
            db.commit()
            print(f'Added: Application Name: {app_name}')
        input("Applications have been added. Press ENTER to continue: ")
    print("-" * 30)

while True:
    print(options)
    selected_option = int(input("Please select an option: "))
    if selected_option == 1:
        view_applications()
    elif selected_option == 2:
        open_application()
    elif selected_option == 3:
        add_application()
    else:
        print("-" * 30)
        print("Please enter a value between 1 and 3.")
        print("-" * 30)
        break

db.commit()
db.close()
