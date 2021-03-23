
import socket
import mouse

HOST = '192.168.1.183'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

#Functions for doing tasks
def close():
    return "closing now"
def left():
    mouse.move(-100, 0, absolute=False, duration=0.2)
    return "Moved left"
def right():
    mouse.move(100, 0, absolute=False, duration=0.2)
    return "Moved right"
def up():
    mouse.move(0, -100, absolute=False, duration=0.2)
    return "Moved up"
def down():
    mouse.move(0, 100, absolute=False, duration=0.2)
    return "Moved down"
def left_click():
    return "Clicked Left"
    mouse.click('left')
def right_click():
    mouse.click('right')
    return "Clicked Right"
def no_recognition():
    return "Can't execute your command"

# Function to convert number into string 
# Switcher is dictionary data type here 
def commandline(argument): 
    switcher = { 
        b'close': close, 
        b'left': left,
        b'right': right,
        b'up': up,
        b'down': down,
        b'left_click': left_click,
        b'right_click': right_click,
               } 
    func=switcher.get(argument, no_recognition)
    return func()

 
def server_mouse():
    #close command
     close_command=b'close'
     last_command=''

     #Waiting for commands and assigining work
     while True:
         conn, addr = s.accept()
         with conn:
          print('Connected by', addr)
          while True:
            data = conn.recv(1024)
            if data:
             #print(data)
             print(commandline(data))
             last_command=data
            if not data:
             conn.close()
             break
            conn.sendall(data)
         if last_command ==close_command:
            break

server_mouse()
