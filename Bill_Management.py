import mysql.connector as sqlcon
import random 
conn= sqlcon.connect(
    host="localhost",
    user="root",
    password="9600992926",
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS INDIRASUPERMARKET1")
cursor.execute("USE INDIRASUPERMARKET1")

cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS(cust_id int primary key,cus_name varchar(50), cus_phone bigint unique , bonus_points int)")
cursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTS ( prod_id int primary key, prod_name varchar (50), MRP float ) ")
cursor.execute("CREATE TABLE IF NOT EXISTS customer_BILL(prod_id int,foreign key(prod_id)references PRODUCTS(prod_id), prod_name varchar(50), qty int , mrp float , total_price float)")
cursor.execute("CREATE TABLE IF NOT EXISTS BILLS(bill_no int, cust_id int, recipient_name varchar(50), total_amount float, bil_date date)")


#creates 10000 bill numbers from 1 to 10000 each time this program is runned
bill_nos=[]
for i in range(1,10000):
    bill_nos.append(i)
    
#function to start billing for those customer who have their membership id          
def bill_area():    
    bill_area.c_id=int(input(" Enter customer id : "))
    ids=cus_ids()
    if bill_area.c_id in ids:        
        cursor.execute("SELECT cus_name,cus_phone FROM customers WHERE cust_id={}".format(bill_area.c_id))
        rec=cursor.fetchall()
        bill_area.c_name=rec[0][0]
        bill_area.c_ph=rec[0][1]
        while True:
            sure=input(" Are you sure to start billing for customer {}: ".format(bill_area.c_name))
            if sure in ("yes","Y","YES","y","Yes"):
                billing_prod_det(bill_area.c_id,bill_area.c_name,bill_area.c_ph)
            elif sure in ("NO","no","No","N","n"):
                menu()
            else:
                print(" Please enter yes or no !")
                continue
                             
    else:
        print(" There is no such customer with id {}".format(bill_area.c_id))
        print(" Please enter correct Id")
        menu()



#this is the function which is used to input product ids  and start billing
def products_billing(cid="null",cname="null",cphone="null"):
    print("")
    prod_cod=int(input(" Enter product code: "))
    cursor.execute("SELECT prod_id FROM PRODUCTS")
    ids=cursor.fetchall()
    pr_ids=[]
    for el in ids:
        pr_ids.append(el[0])
    if prod_cod in pr_ids:
        cursor.execute("SELECT * FROM PRODUCTS WHERE prod_id={}".format(prod_cod))
        pr_rec=cursor.fetchall()
        pr_name=pr_rec[0][1]
        price=pr_rec[0][2]
        print(" Price of {} is {} ".format(pr_name,price))
        qty=int(input(" Enter the quantity of  {} : ".format(pr_name)))
        print("")
        tot_pr=qty*price
        cursor.execute("INSERT INTO customer_bill values({},'{}',{},{},{})".format(prod_cod,pr_name,qty,price,tot_pr))
        conn.commit()
        
    elif prod_cod==0:
        cursor.execute("SELECT sum(total_price) FROM CUSTOMER_BILL")
        tot=cursor.fetchone()
        total_amnt=tot[0]
        print(" Total amount = {}".format(total_amnt))
        while True:
            sure=input(" Are you sure to print the bill (yes/no): ")
            if sure in ("yes","Y","YES","y","Yes"):
                conn.commit()
                cursor.execute("SELECT prod_id,prod_name,qty,mrp,total_price FROM CUSTOMER_BILL")
                bill=cursor.fetchall()
                cursor.execute("SELECT curdate()")
                date=cursor.fetchone()
                date_=date[0]
                tot_prod=len(bill)
                print("""

                                         INDIRA SUPERMARKET
                                             New Delhi
_________________________________________Phone no.1234567890__________________________________________________
**************************************************************************************************************
                                                        
                                                                                 DATE= '{}'
BILL NO. = {}
Cusromer ID = {}
Customer name = {}
customer phone no. = {}

***************************************************************************************************************
  PRODUCT CODE             PRODUCT NAME             QUANTITY                 MRP                      TOTAL
***************************************************************************************************************""".format(date_,billing_prod_det.bill_no,cid,cname,cphone))
                for el in bill:
                    print("  ",end="")
                    for i in el:
                        print(i,end="")
                        for j in range (25
                                        -len(str(i))):
                            print(" ",end="")
                    print("")


                print("""
______________________________________________________________________________________________________________
    TOTAL AMOUNT =  {}
------------------------------------

                                                            

                         *********************THANK YOU***************************
                                         PLEASE VISIT AGAIN """.format(total_amnt))
                print("")
                if menu.cu_id in ("yes","Y","YES","y","Yes"):
                    cursor.execute("UPDATE CUSTOMERS SET bonus_points=bonus_points+({}*0.025) WHERE cust_id={}".format(total_amnt,bill_area.c_id))
                    conn.commit()
                    cursor.execute("INSERT INTO BILLS VALUES ({},{},'{}',{},'{}')".format(billing_prod_det.bill_no,bill_area.c_id,bill_area.c_name,total_amnt,date_))
                    conn.commit()
                    cursor.execute("DELETE FROM customer_bill")
                    conn.commit()
                    menu()
                else:
                    cursor.execute("INSERT INTO BILLS VALUES ({},0,'null',{},'{}')".format(billing_prod_det.bill_no,total_amnt,date_))
                    conn.commit()
                    menu()
            elif sure in ("NO","no","No","N","n"):
                if menu.cu_id in("yes","Y","YES","y","Yes"):
                    products_billing(bill_area.c_id,bill_area.c_name,bill_area.c_ph)
                else:
                    products_billing()
            else:
                print(" Please enter yes or no !")
                print("")
                continue
                """if menu.cu_id in("yes","Y","YES","y","Yes"):
                    products_billing(bill_area.c_id,bill_area.c_name,bill_area.c_ph)
                else:
                    products_billing()"""
                

    else:
        print(" Please enter correct product id: ")
        while True:
            ch=input(" If u want search for product code enter 'yes' otherwise 'no' : ")
            if ch in("yes","Y","YES","y","Yes") :
                view_prod()
                break
            elif ch in ("NO","no","No","N","n"):
                while True:
                    if menu.cu_id in("yes","Y","YES","y","Yes"):
                        products_billing(bill_area.c_id,bill_area.c_name,bill_area.c_ph)
                    else:
                        products_billing()
            else:
                print(" Please enter yes or no !")
                continue

# function to go inside billing arear for those customer who dont have their membership
def billing_prod_det(ccid="null",ccname="null",ccphone="null"):
    cursor.execute("DELETE FROM customer_bill")
    conn.commit()
    global bill_nos
    billing_prod_det.bill_no=random.choice(bill_nos)
    bill_nos.remove(billing_prod_det.bill_no)
    print("")
    print(" NOTE: TO PRINT THE BILL ENTER 0 IN PLACE OF PRODUCT CODE !")
    while True:
        products_billing(ccid,ccname,ccphone)


#function to get all customer ids which are in use

def cus_ids():
    cursor.execute("SELECT cust_id FROM CUSTOMERS")
    ids=cursor.fetchall()
    id_used=[]
    for i in ids:
        id_used.append(i[0])
    return id_used

#function to get all phone nos of customers (phone numbers are unique)

def phoneNo_used():
    cursor.execute("SELECT cus_phone FROM CUSTOMERS")
    phns=cursor.fetchall()
    phns_used=[]
    for i in phns:
        phns_used.append(i[0])
    return phns_used

#function to update details of customer
def upd_cust_det() :
    u=input("""
  What do you want to update
   1. Name
   2. Phone No.
>>>   """)
    if u=="1":
        name=input(" Enter the new name of the customer:  ")
        cursor.execute("UPDATE CUSTOMERS SET cus_name='{}' WHERE cust_id={}".format(name,update_cus.id_c))
        while True:
            sureness(update_cus.id_c,"name")
    elif u=="2":
        phn=int(input(" Enter the new phone number of the customer: "))
        phns_u=phoneNo_used()
        if phn not in phns_u:
            cursor.execute("UPDATE CUSTOMERS SET cus_phone={} WHERE cust_id={}".format(phn,update_cus.id_c))
            while True:
                sureness(update_cus.id_c,"Phone no.")
        else:
            print(" There is a customer with same phone no.")
            print(" Please enter another phone no. ")
            upd_cus_det()
    else:
        print(" Please enter correct option")
        upd_cust_det()

#fuction to go inside update area of customer details
def update_cus():
    update_cus.id_c=int(input(" Enter Id of the customer: "))
    i=cus_ids()
    if update_cus.id_c in i:
       upd_cust_det()
    else:
        print(" There is no customer with Id {} ".format(update_cus.id_c))
        print(" Please enter correct customer id")
        print("")
        update_cus()

#function to get all product codes used (products have unique codes)        
def prod_id_used():
    cursor.execute("SELECT prod_id FROM PRODUCTS")
    ids=cursor.fetchall()
    id_used=[]
    for i in ids:
        id_used.append(i[0])
    return id_used

# function to update product details
def update_prod():
    pr_code=input(" Enter product code : ")
    pr_ids=prod_ids_used()
    if pr_code in pr_ids:
        cursor.execute("SELECT prod_name FROM PRODUCTS WHERE prod_id={}".format(pr_code))
        rec=cursor.fetchall()
        pr_name=rec[0][0]
        new_mrp=float(input(" Enter new MRP rate of the {}: ".format(pr_name)))
        cursor.execute(" UPDATE PRODUCTS SET mrp={} WHERE prod_id={}".format(new_marp,pr_code))
        conn.commit()
        print(" MRP rate of {} has been updated successfully".format(pr_name))
    else:
        print(" PLEASE ENTER CORRECT PRODECT CODE!")
        menu()
    
# function to print asked customer details        
def cust_det_print(string,inti):
    cursor.execute("SELECT * FROM CUSTOMERS WHERE {}={}".format(string,inti))
    rec=cursor.fetchall()
    print("""
************************************************************************************************
    CUSTOMER ID               CUSTOMER NAME             PHONE NO.                 BONUS POINTS
************************************************************************************************""")
    print("    ",end="")
    for i in rec[0]:
        print(i,end="")
        for l in range(0,(26-len(str(i)))):
            print(" ",end="")
    print("")


# function to get customer id and view customer details
def view_cus():
    choice=input("""
  What do u want to enter
   1. customer Id or
   2. customer phone no.
>>> """)
    if choice=="1":
        id_c=int(input(" Enter Id of the customer: "))
        i=cus_ids()
        if id_c in i:
            cust_det_print("cust_id",id_c)
            menu()
        else:
            print(" There is no customer with Id {} ".format(id_c))
            print(" Please enter correct id")
            view_cus()



    elif choice=="2":
        phn=int(input(" Enter the phone number of the customer: "))
        phns_u=phoneNo_used()
        if phn in phns_u:
            cust_det_print("cus_phone",phn)
            menu()
        else:
            print(" There is no customer with phone no. {} ".format(phn))
            print(" Please enter correct phone no.")
            view_cus()
    else:
        print(" PLEASE ENTER CORRECT OPTION !")
        view_cus()
        
def sureness(id_,b):
    sure=input(" Are you sure to change the {} of customer with id {} (yes/no): ".format(b,id_))
    if sure in ("yes","Y","YES","y","Yes"):
        conn.commit()
        print(" details of customer who's id is {} has been updated successfully ".format(id_))
        menu()
    elif sure in ("NO","no","No","N","n"):
        conn.rollback()
        print(" updation has been cancelled")
        menu()
    else:
        print(" Please enter yes or no !")
        sureness(id_,b)
def view_prod():
    name=input(" Enter product name: ")
    cursor.execute("SELECT * FROM PRODUCTS WHERE prod_name LIKE '%{}%' ".format(name))
    rec=cursor.fetchall()
    print("""
********************************************************************
    PRODUCT CODE              PRODUCT NAME              MRP RATE              
********************************************************************""")
    for i in rec:
        print("    ",end="")
        for j in i:
            print(j,end="")
            for l in range(0,(26-len(str(j)))):
                print(" ",end="")
        print("")
#program starts with menu() function
def menu():
    print("")
    print("")
    print("""
           MENU
----------------------------
****************************

  1. Products Billing
  2. Edit customer
  3. Edit products
""")
    op=input(" Enter your option: ")
    if op=="1":
        print("""
***********************************************************************************
                                 BILL AREA
***********************************************************************************""")
        while True:
            menu.cu_id=input(" does the customer have membership or not (yes/no): ")
            if menu.cu_id in("yes","Y","YES","y","Yes"):
                bill_area()
            elif menu.cu_id in ("NO","no","No","N","n"):
               billing_prod_det()
            else:
                print(" Please enter yes or no ")
                continue
        
    elif op=="2":
        while True:
            a_r=input("""
  Select your process:
   1. Add customer
   2. Remove customer
   3. Update customer details
   4. view customer details
>>>  """)
            print("\n")
            if a_r=="1":
                add_cus()
                menu()
            elif a_r=="2":
                rem_cus()
                menu()
                
            elif a_r=="3":
                update_cus()
                menu()

            elif a_r=="4":
                view_cus()
            else:
                print(" Please select correct option ")
                continue

    elif op=="3":
        while True:
            a_r=input("""
  Select your process:
   1. Add product
   2. Update product details
   3. view product details
>>>  """)
            print("\n")
            if a_r=="1":
                prod_name=input(" Enter product name : ")
                prod_ids=prod_id_used()
                while True:
                    p_id=random.randint(5000,10000)
                    if p_id in prod_ids:
                        continue
                    else:
                        break
                mrp=float(input(" Enter MRP rate of the product: "))
                print(" product code of {} is {} ".format(prod_name,p_id))
                cursor.execute("INSERT INTO PRODUCTS VALUES({},'{}',{})".format(p_id,prod_name,mrp))
                conn.commit()
                print(" {} has been added to available products list".format(prod_name))
                menu()
            elif a_r=="2":
                update_prod()
                menu()
                
            elif a_r=="3":
                view_prod()
                menu()

            else:
                print("Please select correct option ")
                continue
    else:
        print(" Please enter correct option")
        print("")
        menu()

#function to add new customer     
def add_cus():
    id_used=cus_ids()
    while True:
        c_id=random.randint(100,10000)
        if c_id in id_used:
            continue
        else:
            break
    print("""
__________________________________
      Details of customer
----------------------------------""")
    c_name=input(" Enter the name of customer: ")
    while True:
        c_ph=input(" Enter the phone number of {} : ".format(c_name))
        if len(c_ph)<5:
            print(" please enter correct phone no.!")
            continue
        else:
            break
    c_bonus=int(input(" Enter  initial bonus of {} : ".format(c_name)))
    while True:
            try:
               cursor.execute("INSERT INTO CUSTOMERS VALUES({},'{}',{},{})".format(c_id,c_name,c_ph,c_bonus))
               break
            except sqlcon.errors.IntegrityError :
                print(" There is already a member with same phone no.")
                c_ph=input(" So pleae enter another phone number of {} : ".format(c_name))
                continue
    print(" Customer id of {} is {} ".format(c_name,c_id))
    while True:
        sure=input(" Are you sure to add the membership of {} (yes/no): ".format(c_name))
        if sure in ("yes","Y","YES","y","Yes"):
            conn.commit()
            print(" Membership of {} has been added. ".format(c_name))
            break
        elif sure in ("NO","no","No","N","n"):
            conn.rollback()
            print(" Adding of membership has been declined")
            break
        else:
            print(" Please enter yes or no !")
            continue
        

#function to remove customer membership
def rem_cus():
    while True:
        i=int(input(" Enter customer's id who's membership has to be removed: "))
        id__=cus_ids()
        if i in id__:
            cursor.execute("SELECT cus_name FROM customers WHERE cust_id ={}".format(i))
            n=cursor.fetchone()
            name=n[0]
            cursor.execute("DELETE FROM CUSTOMERS WHERE cust_id={}".format(i))
            while True:
                    sure=input(" Are you sure to remove the membership of {} (yes/no): ".format(name))
                    if sure in ("yes","Y","YES","y","Yes"):
                        conn.commit()
                        print(" Membership of {} has been removed. ".format(name))
                        menu()
                    elif sure in ("NO","no","No","N","n"):
                        conn.rollback()
                        print(" removal of membership has been declined")
                        menu()
                    else:
                        print(" Please enter yes or no !")
                        continue
            
        else:
            print(" There is no customer with id {}".format(i))
            print(" Please enter correct customer id")
            rem_cus()


print("""
                                INDIRA SUPERMARKET
_____________________________________New Delhi_________________________________________
***************************************************************************************""")


menu()
