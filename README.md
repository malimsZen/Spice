# Spice
Small shopping platform that takes customer orders and saves them into a database.

# Product Order

## Product Order Pseudo-code:

First, I’ll create a class that will capture the order-objects attributes. When shopping in a supermarket, customers pick products of certain brands and then decide on the product weight they intend to purchase. That means that an order(object) has attributes like product, weight, and cost. One unique feature about products though is that they have fixed, attributes. 


## Order:
1. Product
2. Weight
3. Cost



I’ll start out by creating an order class which define the object's attributes and method(behaviour): 

```python
def Order():
	class Order:
		def __init__(self,prod,weight): # order object gets to have this attributes.
			self.prod = prod
			self.weight = weight
			self.cost = self.weight * 10

		def Cost(self):#This method will calculate cost by multiplying each product's weight by 10.
            cost_per_gram = self.weight * 10 
            return cost_per_gram


					
			
```

Second, I have to determine how I’ll compute the order costs and totals in order to define the catalog rendering. I have a class that molds object with `prod, weight, cost` attributes. `Order` class has a `Total` method that accumulates each product’s total cost. I have to determine how the user will be able to make a choice and relay the user selections. In this section I've opted for using a sql database because it will be simpler to integrate the data and have an aggregated platform.

Third, I’ll display the product catalog most probably in dictionary form, displaying the available input options for customers.  

```python
import pprint
import mysql.connector

def bevOrder():

	mydb = mysql.connector.connect(
	host="localhost",
	user="yourusername",
	password="yourpassword",
	database="Orderdb"
			)# creating a connection between the python program and the SQL database.

	mycursor.execute("CREATE TABLE orderTable (id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), weight INT, cost INT)")

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


```

Finally, I’ve decided to store the records in a MySQL database because I’ve found it challenging to use a dictionary or any other data structure. I another option that I would use a text file but a database works better in this case.

<aside>
## **Lesson:**
One thing I’ve learned is the use of the Django framework could have made it easier for me to integrate all the intended modules and tools.

</aside>

I’ll connect my MySQL database inside the transaction function and use the object’s attributes as the table fields.  Time for the next nightmare, testing it. 

Bravo!

We have a working product, it’s still not serving the purpose as intended but at least I’ve found a way to channel the customer orders into a storage system, MySQL database. I’ll proceed to upload the project on GitHub and then do the updates later, it will be easier because I will have the opportunity to test the code without ruining the genesis code.