import json, os
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue1 = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue1.get_queue())
    

def add():
    phone_number = input("Hello, Please enter the best phone number to reach you at.")
    queue1.enqueue(phone_number)
    print(f"Your phone number {phone_number} has been added to the list.")

def dequeue():
    phone_number = queue1.dequeue()
    send(body='', to='')
    #insert send sms statement to the end user
    #print(f"Your phone number {phone_number} has been removed and notified.")

def save():
    #obtain thee cuurent array using ---> queue1.get_queue()
    #write to the json file.
    #open file, prepared for writing(w), and write method to json file
    imported_queue = json.load(file)
    #close the file
    pass

def load():
    #open the file for reading "r"
    #take the content inside the file to load
    pass  
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 3:
        print_queue()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Invalid option "+str(option))
