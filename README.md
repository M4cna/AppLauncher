# AppLauncher
 This Python project, named "App Launcher," allows users to manage their applications by viewing, adding, and opening them. It uses SQLite for database management and provides a user-friendly interface through the command line. Here is a brief overview of its functionality:

View Applications:

1-Users can view a list of all applications currently stored in the database.

2-If no applications are stored, it informs the user accordingly.

Open Application:

1-Users can open an application by entering its name.

2-If the application is found in the database, it is executed.

3-If not, it prompts the user to add the application first.

Add Application:

1-Users can add new applications by entering the application's name and URL.

2-The new application is then stored in the SQLite database

Database Management:

1-The SQLite database is used to store application names and URLs.

2-Data is persisted, meaning it remains even after the program is closed and reopened.
