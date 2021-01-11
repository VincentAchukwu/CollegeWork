import sys, socket, threading

class Client:

    # specifying format for encoding/decoding messages
    FORMAT = "utf-8"
    # creating client socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, nickname, addr, channel):

        # initialising nickname, address and chatroom name
        # and connecting client to server
        self.nickname = nickname
        self.channel = channel
        self.client.connect(addr)

    # listening to server, sends nickname
    def receive(self):

        # while client connected to server
        while True:
            try:
                message = self.client.recv(1024).decode(self.FORMAT)
                # if the message sent is codeword "getName+Channel", send nickname and channel to server
                # doesn't print it, but sends nickname and channel to server
                if message == "getName+Channel":
                    self.client.send("{} {}".format(self.nickname, self.channel).encode(self.FORMAT))
                # else it's just a message, display to client only
                else:
                    print(message)

            # If some error occurs, ends client connection
            except:
                print("An error occured!")
                self.client.close()
                break

    # client sends messages to server
    def write(self):

        # as long as they are connected, client can interact with it
        while True:

            # sends message to server in format "NAME: MESSAGE"
            userIn = input()
            message = "{}: {}".format(self.nickname, userIn)

            # send it to server
            self.client.send(message.encode(self.FORMAT))

def main():

    # ensuring client enters valid arguments
    try:
        nickname, host, port, channel = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]

    # if not, display instructions on how to pass arguments and end program
    except:
        print("Error: please enter name, valid host, port, and channel")
        sys.exit()

    # storing host and port in tuple for binding
    ADDR = (host, port)


    c = Client(nickname, ADDR, channel)

    # initiating threads for listening and writing to server
    receiveThread = threading.Thread(target=c.receive)
    receiveThread.start()

    writeThread = threading.Thread(target=c.write)
    writeThread.start()

if __name__ == '__main__':
    main()
