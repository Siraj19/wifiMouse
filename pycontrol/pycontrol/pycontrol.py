
import socket
import mouse
import threading

#global variable
data=b'0'
presscheck=False
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
HOST = socket.gethostbyname(hostname)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

#Functions for doing tasks
def close():
    global presscheck
    presscheck=False
    return "closing now"
def left():
    global presscheck
    presscheck=True
    while True:
       mouse.move(-5, 0, absolute=False, duration=0.01)
       if presscheck==False:
             break
    return "Moved left"
def right():
    global presscheck
    presscheck=True
    while True:
       mouse.move(5, 0, absolute=False, duration=0.01)
       if presscheck==False:
             break
    return "Moved right"
def up():
    global presscheck
    presscheck=True
    while True:
       mouse.move(0, -5, absolute=False, duration=0.01)
       if presscheck==False:
             break
    return "Moved up"
def down():
    global presscheck
    presscheck=True
    while True:
       mouse.move(0, 5, absolute=False, duration=0.01)
       if presscheck==False:
             break
    return "Moved down"
def left_click():
    global presscheck
    presscheck=False
    mouse.click('left')
    return "Clicked Left"
def right_click():
    global presscheck
    presscheck=False
    mouse.click('right')
    return "Clicked Right"
def no_recognition():
    return "Can't execute your command"

# Function to convert number into string 
# Switcher is dictionary data type here 
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
    print(data)
    func=switcher.get(data, no_recognition)
    return func()

 
def server_mouse():
    #close command
     close_command=b'close'
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
             #print(data)
             if presscheck==True:
                 #presscheck=False
                 th._stop_event.set()
             else:
               th = threading.Thread(target=commandline)
               th.start()
             last_command=data
            if not data:
             conn.close()
             break
            conn.sendall(data)
         if last_command ==close_command:
            break

server_mouse()
