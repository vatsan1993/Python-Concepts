import sqlite3

class DB:

    def __init__(self,name):
        self.conn = sqlite3.connect("name" + ".db")
        self.c = self.conn.cursor()

    def createConnection(self):
        self.c.execute("""create table employees (
            first text,
            last text,
            pay integer)""")



    def insert_emp(self,emp):
        self.c.execute("insert into employees values(:first, :last, :pay)",{'first':emp.first, 'last':emp.last,'pay':emp.pay})
        self.conn.commit()

    def get_Entries_by_firstname(self, fname):
        # use ? symbol inplace of :first when using tuples.
        req= {'first': fname}
        self.c.execute("select * from employees where first=:first", req)
        return (self.c.fetchone())

    def get_Entries_by_lastname(self, lname):
        req= {'last': lname}
        self.c.execute("select * from employees where last=:last", req)
        return (self.c.fetchone())


    def get_Entries_by_pay(self, pay):
        req= {'pay': pay}
        self.c.execute("select * from employees where pay=:pay", req)
        return (self.c.fetchall())

    def update_pay(self,emp, pay):
        with self.conn:
            self.c.execute("""UPDATE employees SET pay = :pay
                        WHERE first = :first AND last = :last""",
                      {'first': emp.first, 'last': emp.last, 'pay': pay})

    def remove_emp(self,emp):
        with self.conn:
            self.c.execute("DELETE from employees WHERE first = :first AND last = :last",
                      {'first': emp.first, 'last': emp.last})

    def  close_connection(self):
        self.conn.close()




