# AstraX_DKMX9_Inventory
Simple Inventory System using SQLITE, Python, and Tkinter
[FILE SYSTEM STRUCTURE]
MAIN.PY
--> DB (DIR)

[DATABASE STRUCTURE]
--> SKU
--> DESCRIPTION
--> BIN#
--> LOCATION
--> UNIT
--> QTY
--> REORDER QTY
--> COST
--> INVENTORY VALUE
--> REORDERED

[BACKLOG]
(STARTING POINT)
--> Create Main Execution
---> Need to detect if local db already exist and create a db if one doesn't already exist.
---> Going to just search for any sqlite db extension and pull it
------> If more than one record is found then use File Dialog to have the user set a specific one
------> If only one record is found then just pull it.
------> If none are found then create one title (generic) "DB"
---------> ALSO needs to prompt the user "Do you want to use generic db setup or create your own?"
********** NOTE: This will allow users to make their own db columns.
