# In this section I'll be collecting customer information details for 
# registration on the sytem. Their information will be useful in terms 
# of making payments,delivering, and customer service as a whole.

#Another idea has popped up, I need to check if the customer credentials exists in the database
#to grant a new registration. I'll do that as an update later on,now I'm going only to take in
# customer information.

import mysql.connector as msc
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





        



