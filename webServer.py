# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  serverSocket.listen(1)  #Listen for incoming connections

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()     #Accept incoming connection

    try:
      message = connectionSocket.recv(1024).decode()   #Receive message from client
      filename = message.split()[1]
      
      #opens the client requested file.
      f = open(filename[1:], "rb")  #Open file in binary mode

      #This variable can store the headers you want to send for any valid or invalid request.
      #Fill in start 
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"

      #Fill in end
               
      for i in f: #for line in file
        outputdata += i  #Append file contents to outputdata

      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      connectionSocket.send(outputdata)  #Send response to client
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      not_found_response = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<html><body><h1>404 Not Found</h1></body></html>"
      connectionSocket.send(not_found_response)  #Send 404 response to client
      #Fill in end

      #Close client socket
      #Fill in start
      connectionSocket.close()  #Close connection with client
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)