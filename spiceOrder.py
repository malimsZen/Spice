# I'll be creating the order process done by the client. The customer will get
# to select the preferred spice then the amount before being billed the total bill. 
# This is the program introduction message which will be accompanied by
# instructions on whether to continue using the platform or exit.

import mysql.connector as msc
import pprint

def intro():
    
    # input selection options.
    proceed = {1:'Yes'}
    exit = {2:'No'}

    
    # Creating a continuos loop that runs if the two provided input selections aren't met.
    while True:
        message = input('''
                    Spice your food, spice your heart
                    Would you like to shop?
                    1. Yes
                    2. No
                    ''')
        # condition checks the input values to determine what to output.
        if message == '1' or '2':
            if message == '2':
                print('Thank you, we hope to see you soon')
                break
            elif message == '1':
                print('We \'re glad to have you on board, please proceed to shopping.')
                break   
            else:
                print('Kinldy make sure your input is the correct character/digit')
                continue
        
            
intro() #The function is working as intended.

# In this section I'll be collecting customer information details for 
# registration on the sytem. Their information will be useful in terms 
# of making payments,delivering, and customer service as a whole.

#Another idea has popped up, I need to check if the customer credentials exists in the database
#to grant a new registration. I'll do that as an update later on,now I'm going only to take in
# customer information.

def cust_Reg():


    welcome_message = '''Welcome to Spice Land, where we meet the needs
         of your taste buds.'''

    print(welcome_message)
    
    #created a class to capture customer instances that share the same attributes(name,address & contact).
    class Customer:

        def __init__(self,name,address,contact):

            self.name = name
            self.address = address
            self.contact = contact


        

    # Collecting customer information.
    full_name = input('Kindly input your full names(first,sur,last): ')
    house_no = input('House number(block,house number): ')
    cus_contact = int(input('Phone number: '))

    #declaring customer objects. 
    customer_info = Customer(full_name,house_no,cus_contact)

    mydb = msc.connect(
        host="localhost",
        user="root",
        password="P@$$w0rd",
        database="spiceDB"
    ) #Creating a string connection to mysql database.

    mycursor = mydb.cursor()

    sql = '''
    INSERT INTO cust_Info VALUES (%s,%s,%s)
    '''

    val = (customer_info.name,customer_info.address,customer_info.contact)

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount,'record inserted')

    return 'Name:',customer_info.name
    return 'Address/Location:',customer_info.address
    return 'Contacts:', customer_info.contact

cust_Reg()

# I'll have to come up with an attribute that can be shared between customer and order tables.

# This module is intended to create a Catalgoue for the user displaying all the options to the customer.

#Defining class for the Order objects which will have a product and amount attributes.

def bevOrder(): # Beverage order function.
    
    class Order:
        def __init__(self,prod,weight,cost): # Each object intance will have these attributes that will represent table fields.
            self.prod = prod
            self.weight = weight
            self.cost = cost * 10

        def Cost(self):#This method will calculate cost by multiplying each product's weight by 10.
            cost_per_gram = self.weight * 10 
            return cost_per_gram
    

    mydb = msc.connect(
        host="localhost",
        user="root",
        password="P@$$w0rd",
        database="spiceDB"
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
            mycursor.execute("SELECT * FROM prod_Order")
            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)
            break

        elif usrInpt < 0 or usrInpt >= 5:
            print('Input the correct character.')
            continue
             
        
        wghtInpt = int(input('Weight:'))
        cost = wghtInpt * 10
        
        prodNme = Beverage[usrInpt] #prodNme initialiazed to the key:value chain. 
        cust_order = Order(prodNme,wghtInpt,cost)

        sql = '''
        INSERT INTO prod_Order (product,weight,cost) VALUES(%s,%s,%s)
        '''
        val = (cust_order.prod,cust_order.weight,cust_order.cost)
        
        mycursor.execute(sql,val)

        mydb.commit()

        print(mycursor.rowcount,'record inserted.')


        prodSelect = usrInpt

    

        
bevOrder()

    
# I've been thinking of how to go about the menu selection and a simpler idea has popped 
# up in my mind. I could easily create a menu table in the Spice database then used Pandas
#  to iterate through it when making selections. 
    
#Instead of appending the food spice menu and creating a long function, I'll create a separate
#functionm,this time revised with Pandas.

