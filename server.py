import socket

# create socket
s_socket = socket.socket()
s_hostname = socket.gethostname()
s_ip = socket.gethostbyname(s_hostname)
s_port = 49152  # available to use port number
s_nickname = input("Enter nickname: ")

# bind socket
s_socket.bind((s_ip, s_port))
print("binding successful\t", s_nickname, s_hostname, s_ip, s_port)

# listen
s_socket.listen(5)  # 5: number of queued connections
print("listening...")

# accept
conn, c_ip = s_socket.accept()
print("connection accepted\t", c_ip[0])

# get and send nickname
c_nickname = (conn.recv(1024)).decode()
conn.send(s_nickname.encode())
print("chat started with: ", c_nickname)

# send and receive messages
while True:
    out_message = input(s_nickname + '>\t')
    conn.send(out_message.encode())
    in_message = conn.recv(1024).decode()
    print(c_nickname + '>\t' + in_message)

