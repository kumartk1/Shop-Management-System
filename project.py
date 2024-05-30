import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import csv
from matplotlib import style

def main():
  print()
  print()
  print("******************************************************")
  print("*---------------Welcome to D-Mart--------------------*") 
  print("******************************************************")
  print()
  print()
  print("Press 1: TO ADD NEW ITEM")
  print("Press 2: TO SEARCH AN ITEM")
  print("Press 3: TO DELETE AN ITEM")
  print("Press 4: TO SEE LIST OF ITEMS")
  print("Press 5: TO ADD NEW EMPLOYEE TO THE LIST")
  print("Press 6: TO SEARCH DETAILS OF AN EMPLOYEE")
  print("Press 7: TO DELETE DETAILS OF AN EMPLOYEE")
  print("Press 8: TO SEE EMPLOYEE DETAILS")
  print("Press 9: TO ADD A NEW RECORD OF IMPORT TO LIST")
  print("Press 10: TO SEE WHOLE RECORD OF IMPORTS")
  print("Press 11: TO SEE CHARTS OF SELECTED DATA")
  print("Press 12: EXIT")
  print()
  print()
  choice = int(input("Please Enter Your Choice:"))
  print()
  print()
  if choice == 1:
    add_new_item()
  elif choice == 2:
    search_item()
  elif choice == 3:
    delete_item()
  elif choice == 4:
    show_items()
  elif choice == 5:
    add_new_employee()
  elif choice == 6:
    search_employee()
  elif choice == 7:
    delete_employee()
  elif choice == 8:
    show_employee_details()
  elif choice == 9:
    add_new_imports()
  elif choice == 10:
    import_details()
  elif choice == 11:
    linecharts()
  elif choice == 12:
    exit()
  else:
    print("Your Choice is IRRELEVENT")

def add_new_item():

    itemid = int(input("Enter the item id:"))
    itemname = input("Enter the item name:")
    brand = input("Enter the brand of the item:")
    price = input("Enter the price of the item:")
    quantity = input("Enter the quantity of the item:")
    place_of_import = input("Enter the place from where the item is imported:")
    df = pd.read_csv('items.csv')
    n = df['itemid'].count()
    print(n)
    df.loc[n] = [itemid, itemname, brand, price, quantity, place_of_import]
    df.to_csv('items.csv', index=False)
    print()
    print()
    print("++ Item added sucessfully ++")
    print()
    print(df)
    main()
def search_item():
  
   itemid = int(input("Enter the item id:"))
   df = pd.read_csv("items.csv")
   idf = df.loc[df["itemid"] == itemid]
   if idf.empty:
       print("NO Item Found With Given Code!!!")
   else:
       print()
       print()
       print("Item Details Are:")
       print(idf)

   main()
def delete_item():
  
    itemid = int(input("Enter the item id:"))
    df = pd.read_csv("items.csv")
    df = df.drop(df[df["itemid"] == itemid].index)
    df.to_csv("items.csv", index=False)
    print()
    print("Item Deleted Sucessfully")
    print()
    print(df)
    main()
def show_items():
  
    df = pd.read_csv("items.csv")
    print(df)

    main()
def add_new_employee():

    empid = int(input("Enter the employee id:"))
    empname = input("Enter the name of the employee:")
    age = input("Enter the age of the employee:")
    address = input("Enter the address of the employee:")
    phone = input("Enter the phone number of the employee:")
    salary = (input("Enter the salary of the Employee:"))
    df = pd.read_csv("employees.csv")
    n = df["empid"].count()
    df.loc[n] = [empid, empname, age, address, phone, salary]
    df.to_csv("employees.csv", index=False)
    print()
    print("New Employee Sucessfully added")
    print()
    print(df)
    main()

def search_employee():

    empid = int(input("Enter the employee id:"))
    df = pd.read_csv("employees.csv")
    wdf = df.loc[df["empid"] == empid]
    if wdf.empty:
       print("NO Employee found with given employee id!!!!")
    else:
       print()
       print()
       print("Employee Details are:")
       print(wdf)
    main()
def delete_employee():
    empid = int(input("Enter the employee id:"))
    df = pd.read_csv("employees.csv")
    df = df.drop(df[df["empid"] == empid] .index)
    df.to_csv("employees.csv", index=False)
    print()
    print("Employee Record deleted sucessfully")
    print()
    print(df)
    main()

def show_employee_details():
   
    df = pd.read_csv("employees.csv")
    print(df)

    main()
def add_new_imports():
   
    Imp_No = int(input("Enter the Import No:"))
    Imp_Name = input("Enter the name of the importer:")
    Date_of_Departure = input("Enter the date of departure of stock:")
    Date_of_Arrival = input("Enter the date of stock arrival:")
    Import_Charges = int(input("Enter the delivery charges:"))
    Total_Tax = int(input("Enter the total tax:"))
    df = pd.read_csv("imports.csv")
    n = df["Imp_No"].count()
    df.loc[n] = [Imp_No, Imp_Name, Date_of_Departure,Date_of_Arrival, Import_Charges, Total_Tax]
    df.to_csv("imports.csv", index=False)
    print()
    print("Import Records are sucessfully added")
    print()
    print(df)
    main()
def import_details():

    df = pd.read_csv("imports.csv")
    print(df)
    main()
def linecharts():


    print("Press 1: For Item Vs Price Chart")
    print("Press 2: For Employee Vs Salary Chart")
    print()
    choice = int(input("Please enter your choice:"))
    if choice == 1:
       df = pd.read_csv("items.csv")
       df = df[["itemname", "price"]]
       plt.xlabel("Itemname------>", size=20, color='r')
       plt.ylabel("Price------->", size=20, color='r')
       df.plot('itemname', 'price', color='c', kind='line')
       plt.title('Itemname Vs Price')
       style.use('ggplot')
       plt.show()

    elif choice == 2:
       df = pd.read_csv("employees.csv")
       df = df[["empname", "salary"]]
       plt.xlabel("Employee Name-------->", size=20, color='r')
       plt.ylabel("Salary of Employees-------->", size=20, color='r')
       df.plot("empname", "salary", color='c', kind='line')
       plt.title('Employee Vs Salary')
       plt.show()
    else:
       print("SORRY!!! No Charts Available")
    main()
def exit():

   print("**********************************************************")
   print("*______Thanks for shopping at D-Mart..Visit again______*")
   print("**********************************************************")

main()

