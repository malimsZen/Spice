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
    
    
    Beverage = {1:'Tea Masala',2:'Ginger',3:'Tea Leaves',4:'Sugar'} # catalog in dictionary data structure.
    pprint.pprint(Beverage)
    
    print('Select product to start shopping by inputting character 1-5.')
    
    # I'll need to create a loop that will keep on iterating as long as the conditions are met. 
    prodSelect = 1 # Initializing the product select counter.

    while prodSelect > 0 and prodSelect < 5: # For the loop to continue, user must meet stated conditions.

        usrInpt = int(input('Product:'))

        if usrInpt == 0:# This condition will save any previous order into the db and break.
            mycursor.execute("SELECT * FROM customers")
            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
            break

        elif usrInpt < 0 and usrInpt >= 5:
            print('Input the correct character.')
            continue
             
        
        wghtInpt = int(input('Weight:'))
        cost = wghtInpt * 10
        
        prodNme = Beverage[usrInpt] #prodNme initialiazed to the key:value chain. 
        cust_order = Order(prodNme,wghtInpt,cost)

        sql = '''
        INSERT INTO customers (product,weight,cost) VALUES(%s,%s,%s)
        '''
        val = (cust_order.prod,cust_order.weight,cust_order.cost)
        
        mycursor.execute(sql,val)

        mydb.commit()

        print(mycursor.rowcount,'record inserted.')


        prodSelect = usrInpt

    

        
bevOrder()

    

    
