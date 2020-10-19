from socket import *

msg = "\r\n I love computer networks!"

endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver =  ("imap.gmail.com", 993)                  #Fill in start #Fill in end


# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in start

#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start

mailfrom = "<richardtran298@gmail.com>\r\n"
clientSocket.send(mailfrom.encode())
revc2 = clientSocket.recv(1024).decode()
print(revc2)
if recv1[:3] != '250':
    print('250 reply not received from server.')
    
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start

rcpttocommand = "<imap.gmail.com>\r\n"
clientSocket.send(rcpttocommand.encode())
recv3 = clientSocket.recv(1024)
print(recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Fill in end


# Send DATA command and print server response.
# Fill in start

data = "data\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
print(recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Fill in end


# Send message data.
# Fill in start
message = input("Enter your message: \r\n")

# Fill in end

# Message ends with a single period.
# Fill in start

messageend = '\r\n . \r\n'

# Fill in end
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
clientSocket.send(message + messageend)
recv_msg = clientSocket.recv(1024)
print(recv_msg.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send QUIT command and get server response.
# Fill in start

lientSocket.send("Quit \r\n")
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Fill in end