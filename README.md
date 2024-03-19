The project creates employee.db  and makes some actions on it. You can delete a column, get_list by name, surname or age and also 
compare ages(in main.py). Main.py connects to employee.py where is the class named employee and where is the main logic written.

According to some best practice, instead of deleting data fully from database, I added new row named status("ACTIVE"/"DELETED") and during deletion, 
I change its status to "DELETED" in DB, entries with such status("DELETED") are not fetched or updated by any sql query or method in my code. 
