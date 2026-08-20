import socket

IP = "localhost"
PORT = 5005

# define udp socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_gesture(gesture):
    message = gesture.encode("utf-8")
    sock.sendto(message, (IP, PORT))

send_gesture("hello world")