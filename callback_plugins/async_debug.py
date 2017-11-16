from ansible.plugins.callback import CallbackBase
import threading
import socket

BIND_HOST = '127.0.0.1'
BIND_PORT = 9999

try:
    from __main__ import display
except ImportError:
    display = None

def recv_msg(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # msg = '[Debug message from {}] {}'.format(addr,data)
        msg = '[Debug message] {}'.format(data)
        if display is not None:
            display.vv(msg)
        else:
            print msg

def wait_clients():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((BIND_HOST, BIND_PORT))
    sock.listen(10)
    while True:
        conn, addr = sock.accept()
        cli_thread = threading.Thread(target=recv_msg, args=(conn,addr[0]))
        cli_thread.setDaemon(True)
        cli_thread.start()

class CallbackModule(CallbackBase):
    def __init__(self):
        super(CallbackModule, self).__init__()
        srv_thread = threading.Thread(target=wait_clients)
        srv_thread.setDaemon(True)
        srv_thread.start()
