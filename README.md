# AstraX_DKMX9_Inventory
Simple Inventory System using SQLITE, Python, and Tkinter
[FILE SYSTEM STRUCTURE]
MAIN.PY
--> DB (DIR)

[GENERIC DATABASE TABLE STRUCTURE]
--> ROLE
--> STAFF
--> CUSTOMER
--> ORDER
--> PAYMENT
--> SUPPLIER
--> CATEGORY
--> PRODUCT
--> ORDER_Detail

[COMPLETED BACKLOG] ---------> as of push request (Add main.py (Create Main Execution Point)) (Version 0.1)
(STARTING POINT)
(COMPLETED) Create Main Execution
(COMPLETED) Need to detect if local db already exist and create a db if one doesn't already exist.
(COMPLETED) Going to just search for any sqlite db extension and pull it
(COMPLETED) If more than one record is found then use File Dialog to have the user set a specific one
(COMPLETED) If only one record is found then just pull it.
(COMPLETED) If none are found then create one title (generic) "DB"
(COMPLETED) ALSO needs to prompt the user "Do you want to use generic db setup or create your own?"

[CURRENT BACKLOG] ----------> (Version 0.2)
--> after database is selected --> list tables (needs to have options to view, edit, add, delete table)
--> viewing table --> options on each row to (edit the row, add a row, delete a row)

[NEXT BACKLOG #1] ----------> (Version 0.3)
--> Add a toolbar that will be used on any window in regards to (Viewing the database tables and viewing a specific table)
----> (Toolbar Options) will prepare the roadmap for greater features specifically, at this moment, (File, Report Generation, Settings)
(FILE) will have basics New database, Open Database, Close Database, Exit.
(Settings) Need to implement some form of settings options. Not planned yet..
(Report Generation) I would like to implement some form of report generation like Sales Report Generation etc...

[FUTURE BACKLOG #2] -------> (Version 0.4)
--> Update the user interface design.
--> Add window LOGO.
--> Add a branded background to the tool itself.
--> Add csv to file type support and create a method to convert CSV to sqlite database. 

[FUTURE BACKLOG #3] ---------> (Version 0.5)
--> When adding a table to an open database (add an option to import from csv files to the window that manages (adding table))
