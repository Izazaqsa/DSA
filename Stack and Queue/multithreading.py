import time 
import threading 

numbers = list(map(int,input('enter numbers split by space: ').split()))
print (numbers)

def square (numbers):
    sq_num = []
    for i in numbers : 
        time.sleep(0.5)   # sleep the system for the mention time
        num = i * i 
        sq_num.append(num)
    print (f"The square of the number are : \n{sq_num}")

def cube (numbers):
    cube_num = []
    for i in numbers : 
        time.sleep (0.5)
        num = i * i * i
        cube_num.append (num)
    print (f"The cube of the numbers are : \n{cube_num}")


t = time.time ()

# square ()
# cube ()

t1 = threading.Thread (target=square, args=(numbers,))  # creating threads here and it takes tuples so that why use the comma 
t2 = threading.Thread(target= cube , args=(numbers,))

t1.start ()
t2.start ()

t1.join ()
t2.join ()

print (f"the time taken by the program execution is : {time.time ()-t}")