(Running the programs on the command line are implemented as requested from the 
assignment spec).

Clients can leave server via keyboard interrupt ("Ctrl" + "C")

For the broadcast method, I have it so the messages are sent to ALL clients on the 
server, including the sender, as this would also give the sender confirmation the 
message was sent through.

For the extra functionality implemented, I decided to add extra commands that the 
user can enter in the chat. As well as being able to join/create rooms via the 
'!JOIN' command, the client can do the following:

    - !HELP: provides the user with a help manual about the commands available to 
    them.
    - !LIST: lists all the rooms available. It displays the number of users and the 
    users in each room.
    - !ROOM: reminds the client what room they're in (since this is on the terminal, 
    it'll improve readability and make it easier to navigate.)

The '!JOIN' command allows users to join or create rooms on the server. If the user 
uses the command without passing in the room name after it, the help manual will 
appear to let them know of the correct usage of the commands. If the user passes in 
a room name, the server checks if the room exists. If it doesn't, the server removes 
the client from the room they're currently in and adds the client to a new room. 
Else, the server checks if they're already in the room they specified. If they 
aren't, again, the server removes the client from the current room they're in, but 
adds them to the existing room they specified. Else, the server informs the client 
they're already in the room. Appropriate messages are sent to the users in the 
chatrooms whenever someone leaves and joins rooms.

Whenever someone leaves the server, all clients are notified regardless of what 
chatroom they are in.

Whenever the user uses !LIST and !HELP, the output is spaced out to improve
readability.

The relevant messages are printed on the server end to reflect on the clients' 
actions, in a way "logging" the interactions between the clients and the server.

LINKS TO VIDEOS:
Part 3 (Two-way chat): https://www.youtube.com/watch?v=QNr4x13KQHk
Part 4 (Chatrooms): https://www.youtube.com/watch?v=AQEX3U-y4f8

