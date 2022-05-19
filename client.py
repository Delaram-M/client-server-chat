import socket

# create socket
conn = socket.socket()
c_hostname = socket.gethostname()
c_ip = socket.gethostbyname(c_hostname)
c_nickname = input("Enter nickname: ")
print("socket created\t", c_nickname, c_hostname, c_ip)

# connect to server
s_ip = input("Enter friend\'s server IP address: ")
s_port = 49152  # port number used in server
conn.connect((s_ip, s_port))
print("connected to server: ", s_ip, s_port)

# get and send nickname
conn.send(c_nickname.encode())
s_nickname = (conn.recv(1024)).decode()
print("chat started with: ", s_nickname)

# send and receive messages
while True:
    in_message = conn.recv(1024).decode()
    print(s_nickname + '>\t' + in_message)
    out_message = input(c_nickname + '>\t')
    conn.send(out_message.encode())



