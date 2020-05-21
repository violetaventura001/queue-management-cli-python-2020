import json, os
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue1 = Queue(mode="FIFO", current_queue=[]) #first in first out
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    print(queue1.get_queue())
    

def add():
    phone_number = input("Hello, Please enter the best phone number to reach you at.")
    queue1.enqueue(phone_number)
    print(f'Thank You, phone number {phone_number} has been added to the waiting list.')
    print_queue()

def dequeue():
    phone_number = queue1.dequeue()
   # send(body=f'The {phone_number} has been removed from the waiting list', to={phone_number})
    #print(f"Your phone number {phone_number} has been removed and notified.")

def save():
    #obtain the cuurent array using ---> queue1.get_queue()
    with open('phone_numbers.json', 'w') as outfile:
        json.dump(queue1.get_queue(), outfile)
    print("Your number queue has been saved.")


def load():#downloading
    downloaded_queue = []
    with open('phone_numbers.json', 'r') as outfile:
        downloaded_queue = json.load(outfile)
    while queue1.size() > 0:
        queue1.dequeue()
    for item in downloaded_queue:
        queue1.enqueue(item)
    print("Your most updated queue list has been downloaded.")
    print_queue()    
    
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
    if option == 1:
        add()
    elif option == 2:
        dequeue()    
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()    
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Invalid option "+str(option))
