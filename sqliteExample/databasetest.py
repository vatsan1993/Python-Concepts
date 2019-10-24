from sqliteExample.EmployeeBase import Employee
from sqliteExample.databaseOperations import DB

mydb= DB("site")
mydb.createConnection()

emp= Employee("Srivatsan", "Sohavaram", 10000)

mydb.insert_emp(emp)
emp= Employee("Max", "Winchester", 10000)

mydb.insert_emp(emp)
print(mydb.get_Entries_by_firstname("Srivatsan"))
print(mydb.get_Entries_by_lastname("Winchester"))
print(mydb.get_Entries_by_pay(10000))


mydb.close_connection()
