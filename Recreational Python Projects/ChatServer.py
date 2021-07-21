from asyncore import dispatcher
from asynchat import async_chat
import socket
import asyncore
PORT = 5005
NAME = 'OneInAMillion'


class ChatSession(async_chat):
    def __init__(self, server, sock):
        # Standard setup tasks:
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []
        # Greet the user:
        self.push('Welcome to the server Mr/Mrs %s! My name is %s\r\n' % (self.server.addr1, self.server.name))

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(self.server.addr1 + ": " + line + "\n")
        print self.server.addr1 + ": " + line
        self.server.broadcast(self.server.name + " (Admin): " + raw_input("\n Admin Type Message: ") + "\n")

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)


class ChatServer(dispatcher):
    def __init__(self, port, name):
        # Standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.addr1 = ''
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        print "Connected:", addr[0]
        self.addr1 = addr[0]
        self.sessions.append(ChatSession(self, conn))


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: print
