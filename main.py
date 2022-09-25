import os
from tkinter import *
import sqlite3
from sqlite3 import Error
from tkinter import filedialog
from tkinter import messagebox

# VARIABLES
filecount = 0 # Will be used to check how many db files there are in the db folder.
cwd = os.getcwd() # Will be used throughout the project for simplicity
dbpath = cwd + "\\DB\\" # Will be used throughout the project for simplicity
current_working_database = None
window = Tk() # Create a window of tk object\
frame = Frame(window) # Main frame object
frame.grid(row=0, column=0, sticky="NW")
filetypes = (
    ('database files', '*.db'),
    ('sqlite files', '*.sqlite'),
    ('All files', '*.*')
)
file_names = []

# FUNCTIONS
# EU Creates Own Database
def eu_create_own_db():
    # Erase the previous frame content
    for packedItem in frame.winfo_children():
        packedItem.destroy()
    print("End user create their own db...")
    window.title("Setup: [CREATE DATABASE]") # set a title
    window.configure(width=500, height=300) # set window width & height
    window.configure(bg='white') # set background color

    # Put the main window in the center:
    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))

    # Create Object to add to window
    headerlbl = Label(frame, text="Creating your own database! (COMING SOON)")

    # pack items
    headerlbl.pack()
    
# EU Creates a generic database
def eu_generic_db():
    window.destroy()
    generic_dbpath = dbpath + "\\Inventory.db"
    current_working_database = generic_dbpath
    f = open(generic_dbpath, "w")
    f.close()
    conn = sqlite3.connect(current_working_database)
    c = conn.cursor()
    # Create Roles Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Role
              (role_id INTEGER(10) PRIMARY KEY, role_name VARCHAR(40), role_description VARCHAR(40))
    ''')
    # Create Staff Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Staff
              (staff_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(40), last_name VARCHAR(40), address VARCHAR(40), phone INT(10), email VARCHAR(40), username VARCHAR(40), password VARCHAR(40), role_id INT(10),
              FOREIGN KEY(role_id) REFERENCES Role(role_id))
    ''')
    # Create Customer Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Customer
              (customer_id INTEGER(10) PRIMARY KEY, first_name VARCHAR(40), last_name VARCHAR(40), address VARCHAR(40), phone INT(10), email VARCHAR(40), staff_id INT(10),
              FOREIGN KEY(staff_id) REFERENCES Staff(staff_id))
    ''')
    # Create Orders Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS `Order`
              (order_id INTEGER(10) PRIMARY KEY, date_of_order DATE, order_details VARCHAR(40), customer_id INT(10),
              FOREIGN KEY(customer_id) REFERENCES Customer(customer_id))
    ''')
    # Create Payment Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Payment
              (bill_id INTEGER(10) PRIMARY KEY, payment_type VARCHAR(40), payment_details VARCHAR(40))
    ''')
    # Create Supplier Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Supplier
              (supplier_id INTEGER(10) PRIMARY KEY, name VARCHAR(40), address VARCHAR(40), phone INT(10), fax INT(10), email VARCHAR(40), details VARCHAR(40))
    ''')
    # Create Category Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Category
              (category_id INTEGER(10) PRIMARY KEY, name VARCHAR(40), description VARCHAR(40))
    ''')
    # Create Product Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Product
              (product_id VARCHAR(40) PRIMARY KEY, name VARCHAR(40), description VARCHAR(40), unit VARCHAR(40), price FLOAT(8, 1), quantity INT(10), status INT(10), details VARCHAR(40), supplier_id INT(10), category_id INT(10),
              FOREIGN KEY(supplier_id) REFERENCES Supplier(supplier_id),
              FOREIGN KEY(category_id) REFERENCES Category(category_id))
    ''')
    # Create Order_Detail Table
    c.execute('''
              CREATE TABLE IF NOT EXISTS Order_Detail
              (order_detail_id INTEGER(10) PRIMARY KEY, unit_price FLOAT(8, 1), size INT(10), quantity INT(10), discount INT(10), total FLOAT(8, 1), date DATE, product_id VARCHAR(40), order_id INT(10), bill_id INT(10),
              FOREIGN KEY(product_id) REFERENCES Product(product_id),
              FOREIGN KEY(order_id) REFERENCES `Order`(order_id),
              FOREIGN KEY(bill_id) REFERENCES Payment(bill_id))
    ''')
    c.close()
    conn.close()

# (PROMPT FUNCTION: Ask user to use generic db generation or create their own)
def req_db_gen_prompt():
    print("Prompt the user...")
    window.title("Setup: [DATABASE]") # set a title
    window.configure(width=500, height=300) # set window width & height
    window.configure(bg='white') # set background color

    # Put the main window in the center:
    winWidth = window.winfo_reqwidth()
    winwHeight = window.winfo_reqheight()
    posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
    posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
    window.geometry("+{}+{}".format(posRight, posDown))

    # Create Object to add to window
    reasonlbl = Label(frame, text="No database was detected!")
    promptlbl = Label(frame, text="Would you like to use our generic db scheme?")
    nobtn = Button(frame, text="NO - Create my own", command=eu_create_own_db)
    yesbtn = Button(frame, text="YES - Use Generic", command=eu_generic_db)

    # pack items
    reasonlbl.pack()
    promptlbl.pack()
    nobtn.pack()
    yesbtn.pack()
    frame.pack()
    window.mainloop() # execute mainloop for that window

# MAIN
def main():
    print("MAIN EXECUTION..")

# SETUP
if __name__ == '__main__':
    # Check to see how many .sqlite or .db files are in the database folder
    for root, dirs, files in os.walk(dbpath):
        # for each file that is found
        for file in files:
            # check if it has a .db extension
            if file.endswith('.db'):
                file_names.append(dbpath + file)
            # if not check if it has a .sqlite extension
            elif file.endswith('.sqlite'):
                file_names.append(dbpath + file)
    
    # if zero files are found then no database exist (prompt) the user to use our generic generated db or creat their own.
    if len(file_names) == 0:
        req_db_gen_prompt()
    # if the number of files returned is more than 1 then (prompt) the user with file open dialog box.
    elif len(file_names) > 1:
        messagebox.showinfo("Multiple Database Instances Found!", "Please select OK and choose your database.")
        filename = filedialog.askopenfilename(title="Open the database file", initialdir=dbpath, filetypes=filetypes)
        current_working_database = filename
        
    # if the number of files returned is JUST one then import the database.
    elif len(file_names) == 1:
        for filename in file_names:
            current_working_database = filename
    main()