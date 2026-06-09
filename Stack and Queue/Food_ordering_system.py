import time 
import threading

class Queue: 
    def __init__(self,data):
        self.data = data 
        self.next = None

front = None 
rear = None 
temp = None 
count = 0 

t = time.time()


order_list = input ('enter your order: ').split (',')
print (order_list)

def placing_order (order_list):
    global front , rear
    for order in order_list : 
        newnode = Queue(order)
        if front is None : 
            front = rear = newnode 
        else :
            rear.next = newnode
            rear = newnode 
        print (f"placing : {order}")
        time.sleep(0.5)

def serving_order (Queue):
    global front , rear , temp  
    while front is not None:
        temp=front
        print (f"serving : {temp.data}")
        time.sleep(2)
        front = front.next 
        del temp 
        if front is None : 
            rear = None

t1 = threading.Thread (target=placing_order, args= (order_list,))
t2 = threading.Thread(target=serving_order, args=(Queue,) )

t1.start()
time.sleep(1)
t2.start()

t1.join ()
t2.join ()

print(f"the time taken by the program execution : {time.time()-t}")