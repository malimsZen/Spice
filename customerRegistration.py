# In this section I'll be collecting customer information details for 
# registration on the sytem. Their information will be useful in terms 
# of making payments,delivering, and customer service as a whole.

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

    print('Customer Profile:')
    print('Name:',customer_info.name)
    print('Address/Location:',customer_info.address)
    print('Contacts:',customer_info.contact)

cust_Reg()


        



