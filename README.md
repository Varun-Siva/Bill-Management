# Bill-Management
HARDWARE
  	PROCESSOR: Intel Core Duo 2.4 Ghz or above
  	RAM: 2 GB or higher
SOFTWARE :
  	OPERATING SYSTEM: Windows 7 or above.
  	INTERPRETER: Python 3.6 (or later version)
  	DBMS: Mysql 5.5

•	RANDOM
  This module is used to create random numbers from a given set 
•	MYSQL-CONNECTOR
  This module is extensively used to provide mysql-python
  connectivity and to perform insertion and deletion in database.
1.	To create menu:   one function is used . 
  menu():
  this function shows the user with various options to input and proceed further.
2.	To create billing area:  two functions are used. Bill_area(), products_billing()
  Bill_area(): 
  This function askes the user wether the customer has a membership or not.
  Products_billing():
  This function starts taking details of product bought by customer and prints the bill.

3.	To get all customer id’s and phone numbers used:
  Two functions are used.  cus_ids(), phoneNo_used().
  Cus_ids():
  This function returns a list of all the customer id’s used so that it can be used in other functions.
  phoneNo_used():
  this function returns a lis of all  customer’s phone no.

4.	To edit customer details: four functions are used . upd_cust_det(), view_cus(), add_cus(), rem_cus().
  upd_cust_det():
  this function updates customer details using customer Id.
  view_cus():
  this function prints the detail of the customer .
  add_cus():
  this function adds new customer along with their details and membership.
   rem_cus():
  this function removes a customers membership along with their details.

5.	To edit product details:  Two  functions are used. view_prod(), update_prod().
  view_prod():
  This function prints the details of all products which contains the entered name.
  update_prod():
  This function updates the details of the products 
