import sys, socket, threading

class Server:

    # specifying format for encoding/decoding messages
    FORMAT = "utf-8"
    instructions = "\n<!HELP> to view instructions\n" \
                    + "<!JOIN> <ROOMNAME> to join/create a room\n"\
                    + "<!LIST> to list all rooms\n"\
                    + "<!ROOM> to display current room\n"

    # creating server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, addr):

        # starting server and initialising channels, clients list, and nicknames list
        self.server.bind(addr)
        self.server.listen()
        self.channels = {}
        self.clientList, self.nicknames = [], []

    # broadcasts messages to all clients
    def broadcast(self, client, message):

        # we find which room the client is in, then send message to everyone in that room
        for rooms, clients in self.channels.items():
            if client in clients:
                for person in clients:
                    person.send(message)
                # then break since we're done
                break

    # removes client from the room they're in, returns last room encountered
    def remove_client(self, client):
        # we first must remove the client from the room they're currently in
        for room in self.channels:
            if client in self.channels[room]:
                # once we found them, we remove them from room and break the loop
                self.channels[room].remove(client)
                break

        # then return the room we found client in (old room they were in)
        return room

    # handling !JOIN command if room doesn't exist (i.e. creating a room)
    def createRoom(self, client, nickname, roomName, messageList):

        # get the old room in order to notify the 
        # others in that room that clientA has left
        oldRoom = self.remove_client(client)

        # "oldRoom" is the last room we came across in the loop from remove_client() (which is where clientA was)
        # so we inform everyone in that room that clientA left it
        # also informing them of where clientA joined
        for person in self.channels[oldRoom]:
            person.send("{} left the room and joined '{}'".format(nickname, roomName).encode(self.FORMAT))

        # creating new room with client in it
        self.channels[roomName] = [client]

        # displaying changes to server
        print("{} created and joined '{}'".format(nickname, roomName))
        
        # informing client they're in a new room
        client.send("You're now in room '{}'".format(roomName).encode(self.FORMAT))

    # handling !JOIN command if room exists on server
    def joinRoom(self, client, nickname, roomName, messageList):

        # first check if client not in the room
        if client not in self.channels[roomName]:

            # if not, we remove them from the room they're currently in
            oldRoom = self.remove_client(client)

            # again, informing others that clientA left the room and where they joined
            for person in self.channels[oldRoom]:
                person.send("{} left the room and joined '{}'".format(nickname, roomName).encode(self.FORMAT))

            # appending client to the list of clients in the existing room
            self.channels[roomName].append(client)

            # now informing clients in existing room that clientA has joined
            # also only informing the client with a different message about joining the room
            for person in self.channels[roomName]:
                # i.e informing everyone who was already in the room with this message
                if person != client:
                    person.send("{} has joined the room".format(nickname).encode(self.FORMAT))
                # but the client who joined gets unique message about the room they joined
                else:
                    client.send("You're now in room '{}'".format(roomName).encode(self.FORMAT))

        # else client is already in the room, inform them
        else:
            client.send("Already in room '{}'".format(roomName).encode(self.FORMAT))

    # handling !HELP command
    # (also used if user doesn't pass in room name to !JOIN command)
    def sendHelp(self, client):
        client.send(self.instructions.encode(self.FORMAT))

    # handling the !LIST command
    def listRooms(self, client):

        msg = "\n"
        for room in self.channels:
            # setting the appropriate noun based on number of users per room
            # (i.e. instead of always having "0 user(s)" or "1 user(s)", etc. Essentially making it specific
            if len(self.channels[room]) == 1:
                noun = "user"
            else:
                noun = "users"
            # appending nicknames which correspond to the clients in each room
            names = [self.nicknames[self.clientList.index(person)] for person in self.channels[room]]
            # updates the message string for the info on the available rooms
            msg += "{} ({} {}): {}\n".format(room, len(self.channels[room]), noun, names)

        client.send(msg.encode(self.FORMAT))

    # handling the !HELP command
    def displayRoom(self, client):

        for room in self.channels:
            if client in self.channels[room]:
                client.send("You are currently in '{}'".format(room).encode(self.FORMAT))
                # once we found the room, we break the loop
                break

    # handling interactions between clients
    def handle(self, client):

        # while client is connected
        while True:
            # try receive message of 1024 bytes, then broadcasting
            try:
                # message remains encoded so it can be broadcasted to server (if it's an ordinary message and not a command)
                message = client.recv(1024)
                # splitting the message to identify commands if present
                messageList = message.decode(self.FORMAT).split()

                # (instead of creating exception for this..)
                # if user presses enter without messeage, send it anyway
                if len(messageList) == 1:
                    self.broadcast(client, message)

                # error checking
                # (i.e. else if client doesn't enter room name, send them instructions)
                elif len(messageList) == 2 and messageList[1] == "!JOIN":
                    self.sendHelp(client)

                # else if user wants to join/create room
                elif messageList[1] == "!JOIN":
                    # getting nickname of client, and desired roomname
                    nickname = messageList[0][:-1]
                    roomName = messageList[-1].lower()

                    # if the room doesn't exist, we create it
                    if roomName not in self.channels:
                        self.createRoom(client, nickname, roomName, messageList)

                    # else the room exists, so client joins it
                    else:
                        self.joinRoom(client, nickname, roomName, messageList)

                # (NEW FUNCTIONALITIES: instruction manual, list rooms, display current room)
                # else if user uses !HELP command
                elif messageList[1] == "!HELP":
                    self.sendHelp(client)

                # else if user uses !LIST command
                elif messageList[1] == "!LIST":
                    self.listRooms(client)

                # else if user uses !ROOM command (shows what room they're currently in)
                elif messageList[1] == "!ROOM":
                    self.displayRoom(client)

                # else its just a message, broadcast to all clients (including sender)
                else:
                    self.broadcast(client, message)

            # else removes and closes clients connection if they leave
            # (since client cannot receive messages after closing connection)
            except:

                # deleting client from client list, closing their connection
                index = self.clientList.index(client)
                self.clientList.remove(client)
                client.close()

                # getting client nickname from name list, then broadcast that client left
                nickname = self.nicknames[index]

                # displaying changes to server
                print("{} left server".format(nickname))

                # then removing the client from the room they're in
                self.remove_client(client)

                # informing everyone in the server that someone has left
                for person in self.clientList:
                    person.send("{} left the server...".format(nickname).encode(self.FORMAT))

                # finally we remove the nickname
                self.nicknames.remove(nickname)
                # break from loop
                break

    # listening to client to initialise connection to server
    def receive(self):

        # accepting connections
        while True:
            client, address = self.server.accept()
            print("Connected with {}".format(address))

            # "codeword" to ask client for nickname and room name
            client.send('getName+Channel'.encode(self.FORMAT))

            # expect response to be a nickname and room name
            response = client.recv(1024).decode(self.FORMAT).split()
            nickname, roomName = response[0], response[1].lower()

            # if room doesn't exist, we create it and add client to room
            if roomName not in self.channels:
                self.channels[roomName] = [client]
                # displaying changes to server
                print("{} created and joined '{}'".format(nickname, roomName))

            # else the room exists, we append client to room
            else:
                self.channels[roomName].append(client)

                # inform everyone a client has joined the room
                for person in self.channels[roomName]:
                    if person != client:
                        person.send("{} has joined the room".format(nickname).encode(self.FORMAT))

            # appending nickname and client to their associated list
            self.nicknames.append(nickname)
            self.clientList.append(client)

            # printing info about client to server
            print("Nickname of client: {}".format(nickname))

            # informing client they are connected, and giving them instructions
            client.send("Welcome to the server!".encode(self.FORMAT))
            client.send(self.instructions.encode(self.FORMAT))

            # each client running on a thread (handles messages being sent at the same time)
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

# initialising server in main()
def main():

    # default host and port number if not specified in command line
    if len(sys.argv[1:]) != 2:
        host, port = '0.0.0.0', 8080
    else:
        host, port = sys.argv[1], int(sys.argv[2])
    # storing host and port in tuple for binding
    ADDR = (host, port)

    # creating server instance
    s = Server(ADDR)

    # display connection information on server
    print("Server started on {}:{}".format(ADDR[0], ADDR[1]))
    s.receive()

if __name__ == '__main__':
    main()
