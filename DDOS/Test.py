import socket


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
raise ConnectionRefusedError
connection.settimeout(5)
try:
    connection.connect(("10.0.0.6", 80))
except:
    print("Timeout!")
connection.settimeout(None)