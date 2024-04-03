import mysql.connector as mysql


mydb = mysql.connect(
            host="localhost",
            user="root",
            password="waynehatjr",
            database="red30",
            auth_plugin='mysql_native_password'
        )


mycursor = mydb.cursor()

sql = """INSERT INTO sales(
   cust_name, prod_number, quantity, price, discount, order_total)
   VALUES 
   ('Wayne', 'A001', 1, 10.00, 0.10, 10),
   ('Tyler', 'A002', 2, 10.00, 0.20, 20)
   """

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "was inserted")

mydb.close()