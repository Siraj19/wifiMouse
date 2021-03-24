
#!/usr/bin/env python3

import socket
import tkinter as tk
    
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
HOST = socket.gethostbyname(hostname)

#Functions for doing tasks
def close():
    input_command(b'close')
def left():
    input_command(b'left')
def right():
    input_command(b'right')
def up():
    input_command(b'up')
def down():
    input_command(b'down')
def left_click():
    input_command(b'left_click')
def right_click():
    input_command(b'right_click')

def input_command(command):

    #HOST = '192.168.1.183'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(command)
    data = s.recv(1024) 
    print('Received', repr(data))


root = tk.Tk()
root.title("place() method")
root.geometry("710x480")


quit_button = tk.Button(root, text="QUIT", command=close)
quit_button.configure(height = 10,  width = 100)
quit_button.place(x=0, y=0)

left_button = tk.Button(root, text="Left",command=left)
left_button.configure(height = 10,  width = 25)
left_button.place(x=0, y=161)

right_button = tk.Button(root, text="Right",command=right)
right_button.configure(height = 10,  width = 25)
right_button.place(x=525, y=161)

up_button = tk.Button(root, text="Up",command=up)
up_button.configure(height = 10,  width = 50)
up_button.place(x=185, y=161)

left_click = tk.Button(root, text="Left Click",command=left_click)
left_click.configure(height = 10,  width = 25)
left_click.place(x=0, y=322)

right_click = tk.Button(root, text="Right Click",command=right_click)
right_click.configure(height = 10,  width = 25)
right_click.place(x=525, y=322)

down_button = tk.Button(root, text="Down",command=down)
down_button.configure(height = 10,  width = 50)
down_button.place(x=185, y=322)

root.mainloop()