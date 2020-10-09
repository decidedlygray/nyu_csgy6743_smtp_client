from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = 'smtp.google.com'

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    # if recv[:3] != '220':
    #     print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #     print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    email_to_be_from = 'charlesworrell@gmail.com'
    mail_from = 'MAIL FROM:<{}?\r\n'.format(email_to_be_from)
    clientSocket.send(mail_from.encode())
    server_response = clientSocket.recv(1024)
    server_response = server_response.decode()
    # print(server_response)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    email_to_send_to = 'cw2879@nyu.edu'
    rcp_to = 'RCPT TO:<{}>\r\n'.format(email_to_send_to)
    clientSocket.send(rcp_to.encode())
    server_response = clientSocket.recv(1024).decode()
    # print(server_response)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    # REF: https://www.samlogic.net/articles/smtp-commands-reference.htm
    data_cmd = 'DATA\r\n'
    clientSocket.send(data_cmd.encode())
    server_response = clientSocket.recv(1024).decode()
    # print(server_response)
    # Fill in end

    # Send message data.
    # Fill in start
    message_data = 'Subject: This is a test\r\n'
    message_data += 'Body: Neat\r\n'
    ## clientSocket.send(message_data.encode())
    ## server_response = clientSocket.recv(1024).decode()
    ## print(server_response)
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(message_data.encode())
    end_msg = '.\r\n'
    clientSocket.send(end_msg.encode())
    server_response = clientSocket.recv(1024).decode()
    # print(server_response)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit_cmd = 'QUIT\r\n'
    clientSocket.send(quit_cmd.encode())
    server_response = clientSocket.recv(1024).decode()
    # print(server_response)
    # Fill in end


if __name__ == '__main__':
    smtp_client(25, '127.0.0.1')
    # smtp_client(25, 'smtp.nyu.edu')
