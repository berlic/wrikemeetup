import socket

SEND_HOST = '127.0.0.1'
SEND_PORT = 9999

def send_msg(msg, tag=True):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SEND_HOST,SEND_PORT))
        if tag:
            msg = '<{}> {}'.format(socket.gethostname(),msg)
        sock.send(msg)
        sock.close()
    except socket.error:
        pass
