# This module is intended to create a Catalgoue for the user displaying all the options to the customer.
import pprint
import mysql.connector
    
#Defining a class for the Order objects which will have a product and amount attributes.

def bevOrder(): # Beverage order function.
    
    class Order:
        def __init__(self,prod,weight,cost): # Each object intance will have these attributes that will represent table fields.
            self.prod = prod
            self.weight = weight
            self.cost = cost * 10

        def Cost(self):#This method will calculate cost by multiplying each product's weight by 10.
            cost_per_gram = self.weight * 10 
            return cost_per_gram
            
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@$$w0rd",
        database="Orderdb"
        )
                
                # creating a connection string between the python program and the SQL database.
    
    mycursor = mydb.cursor()
    table_check = "IF OBJECT_ID('customers') IS NULL" # Check whether the table exists
    check = mycursor.execute(table_check)

    if table_check:
        mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), weight INT, cost INT)")
    
    
    Beverage = {1:'Tea Masala',2:'Ginger',3:'Tea Leaves',4:'Sugar'} # catalog in dictionary data structure.
    pprint.pprint(Beverage)
    
    print('Select product to start shopping.')
    
    # I'll need to create a loop cycle that will keep on iterating as long as the conditions are met. 
    
    while True:
        usrInpt = int(input('Product:'))
        wghtInpt = int(input('Weight:'))
        cost = wghtInpt * 10
        
        for bev in Beverage:
            choice = bev

            if choice == usrInpt:
                prodNme = Beverage[usrInpt]
                prodCost = 10
                cust_order = Order(prodNme,wghtInpt,prodCost)
                
                sql = "INSERT INTO customers (product, weight, cost) VALUES (%s,%s,%s)"
                val = (cust_order.prod,cust_order.weight,cust_order.cost)
                mycursor.execute(sql,val)
                
                mydb.commit()
                
                print(mycursor.rowcount,"records inserted.")
                
            elif choice == 0:    
                mycursor.execute("SELECT * FROM customers")
                
                myresult = mycursor.fetchall()
                
                for x in myresult:
                    print(x)
                    break
            else:
                print('Input the right character.')
        
bevOrder()

    
    

    
    
