from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5000

class ChatServer(dispatcher):
    """
    接受连接并产生单个会话；处理其他会话的广播
    """

    # 参数为端口
    def __init__(self, port):
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line+"\r\n")

    def handle_accept(self):
        conn, addr = self.accept()
        self.sessions.append(ChatSession(conn))

class ChatSession(async_chat):
    """
    处理服务器和一个用户之间的连接
    """

    def __init__(self, server, sock):
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        self.push('Welcome to %s\r\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        如果发现了一个终止对象，也就意味着读入了一个完整行，将其广播给每个人
        :return:
        """
        line = ''.join(self, data)
        self.data = []
        self.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

if __name__ == '__main__':
    s = ChatServer(PORT)
    try: asyncore.loop()
    except KeyboardIntercept: print