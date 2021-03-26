#Including Libraries
import socket
import mouse
import threading

# Declaring global variables
data=b'0'          #For reading data and using in functions 
presscheck=False   #An easy alternate of stoping thread


hostname = socket.gethostname()           # Getting the hostname by socket.gethostname() method
HOST = socket.gethostbyname(hostname)     # Getting the IP address using socket.gethostbyname() method
PORT = 50000                              # Assigning a free port number for the connection

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creating a TCP connection socket
s.bind((HOST, PORT))                                 #Assigning our socket IP & Port number
s.listen()

#Functions for doing different tasks
def close():
    global presscheck
    presscheck=False


def left():
    global presscheck
    presscheck=True
    while True:
       mouse.move(-5, 0, absolute=False, duration=0.01)
       if presscheck==False:
             break

def right():
    global presscheck
    presscheck=True
    while True:
       mouse.move(5, 0, absolute=False, duration=0.01)
       if presscheck==False:
             break

def up():
    global presscheck
    presscheck=True
    while True:
       mouse.move(0, -5, absolute=False, duration=0.01)
       if presscheck==False:
             break

def down():
    global presscheck
    presscheck=True
    while True:
       mouse.move(0, 5, absolute=False, duration=0.01)
       if presscheck==False:
             break

def left_click():
    global presscheck
    presscheck=False
    mouse.click('left')

def right_click():
    global presscheck
    presscheck=False
    mouse.click('right')

def no_recognition():

    print("Invalid Instruction Command")

#This function reads global variable data which is being recieved as a instruction 
#from the client request and calls appropiate function
def commandline(): 
    switcher = { 
        b'close': close, 
        b'left': left,
        b'right': right,
        b'up': up,
        b'down': down,
        b'left_click': left_click,
        b'right_click': right_click,
               } 
    global data
    func=switcher.get(data,no_recognition)
    return func()

def server_mouse():
     close_command=b'close'           #close command
     last_command=''                  
     global data
     global presscheck
     #Waiting for commands and assigining work
     while True:
         conn, addr = s.accept()
         with conn:
          print('Connected by', addr)
          while True:
            data = conn.recv(1024)
            if data:
             if presscheck==True:
                 presscheck=False
             else:
               th = threading.Thread(target=commandline)
               th.start()
             last_command=data

            if not data:
             conn.close()
             break
            #conn.sendall(data)
         if last_command ==close_command:
            break

# Main code
print("Server started!")
print("Host name: ",hostname)
print("Host ip  : ",HOST)
thread = threading.Thread(target=server_mouse)
thread.start()
