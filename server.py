# -*- coding: utf-8 -*-


import socket
import select
import threading
from random import randint
import sqlite3
import hashlib
from os import remove


class Streamer(threading.Thread):
    """streams the video to the client"""

    def __init__(self, thread_id, port, filePath, part, numOfParts):
        """constractor: create a video streamer thread"""
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.port = port
        self.sock = socket.socket()
        self.client = None
        self.address = None
        self.file = None
        self.filePath = filePath
        self.part = part
        self.numOfParts = numOfParts

    def run(self):
        """streams a video to a single client"""
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(1)
        (self.client, self.address) = self.sock.accept()

        while self.part < self.numOfParts:
            self.file = open(self.filePath + self.get_part_video_num() + '.mpg', 'rb')
            #self.sock.send('part' + str(self.part) + ':' + fileraw)
            print self.get_part_video_num()
            self.client.send(self.get_part_video_num())
            fileraw = self.file.read(1024)
            while fileraw != '':
                self.client.send(fileraw)
                fileraw = self.file.read(1024)
            self.client.send('p-end')
            ok = self.client.recv(4)
            self.part += 1
            self.check_request()
            self.file.close()

        self.stop()

    def get_part_video_num(self):
        if len(str(self.part)) == 1:
            return '00' + str(self.part)
        elif len(str(self.part)) == 2:
            return '0' + str(self.part)
        else:
            return str(self.part)


    def check_request(self):
        """checks if a client request was made"""
        mutex.acquire()
        cond = threads[self.port]
        mutex.release()

        #nothing new
        if cond[0] == 0:
            pass
        #send from part
        elif cond[0] == 1:
            pass
        #terminate\stop
        elif cond[0] == 2:
            pass
        #send parts
        elif cond[0] == 3:
            pass

    def change_part(self, partnum):
        """change the parts from wich it will send"""
        if partnum.isdigit() and int(partnum) < self.numOfParts:
            self.part = partnum

    def stop(self):
        """stops the server thread"""
        self.client.send('END')
        self.client.close()
        self.sock.close()

    def send_parts(self):
        """sends parts in list"""
        pass




class Receive_vid(threading.Thread):
    """receive upload of a video"""

    def __init__(self, port, temp_path, name, hashfile):
        """constractor: create a video upload receiver thread"""
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket()
        self.temp_path = temp_path
        self.count = 0
        self.data = ''
        self.name = name
        self.hashfile = hashfile

    def run(self):
        """starts a receiver thread"""
        m = hashlib.md5
        self.sock.bind(('0.0.0.0', self.port))
        self.sock.listen(1)
        (self.client, self.address) = self.sock.accept()

        f = open(self.temp_path + str(self.port) + '.mp4', 'wb')

        while True:
            c_hash = self.client.recv(1024)
            #print c_hash
            if c_hash == 'end-of-upload':
                f.close()
                """
                code in here for making the video to valid mpeg
                """
                self.client.send('complete')
                self.client.close()
                self.sock.close()
                break
            self.client.send('ok')
            self.data = self.client.recv(4096)
            hashed = m(self.data)
            #print hashed.hexdigest()
            while not hashed.hexdigest() == c_hash:
                #print c_hash
                #print hashed.hexdigest()
                self.count += 1
                if self.count > 5:
                    self.client.close()
                    f.close()
                    #remove(self.temp_path + str(self.port) + '.mp4')
                    return
                self.client.send('sa')
                self.data = self.client.recv(4096)
                hashed = m(self.data)
            else:
                self.client.send('kg')
                f.write(self.data)
                self.count == 0







class Communication():
    """handles the communication of the server"""

    def __init__(self, sock):
        """gets the servers socket"""
        self.sock = sock

    def handle_request(self, dat, client):
        """handles the data and returns the requested action"""
        print dat
        if dat == "" or dat == "exit":
            open_client_sockets.remove(client)
            print "Connection with client closed"

        elif dat[:6] == 'Watch:':
            """in this case the client want to watch a video"""
            name = dat[6:]
            fold, parts = sql.get_movie(name)
            port = rand_port()

            mutex.acquire()
            threads[port] = (0, 0)
            mutex.release()

            stream = Streamer(0, port, fold, 0, parts)
            stream.start()
            self.send_to_customer('video_stream:' + str(port) + ':' + str(parts), client)

        elif dat[:5] == 'from:':
            port = dat[5:9]
            part = dat[10:]
            mutex.acquire()
            threads[port] = (1, part)
            mutex.release()

        elif dat[:5] == 'stop:':
            port = dat[5:]
            mutex.acquire()
            threads[port] = (2, 0)
            mutex.release()

        elif dat[:7] == 'upload:':
            name = dat[7:dat.index(':!:')]
            f_hash = dat[dat.index(':!:') + 3:]
            if sql.exists_in_base('HASH', f_hash) and sql.exists_in_base('MOVIE_NAME', name):
                port = rand_port()

                mutex.acquire()
                threads[port] = (0, 0)
                mutex.release()

                receiver = Receive_vid(port, TMP_UPLOAD + 'tmp_' + name, name, f_hash)
                receiver.start()

                self.send_to_customer('upload_approved:' + str(port), client)
            else:
                self.send_to_customer('invalid', client)


    def send_to_customer(self, dat, client):
        """sends to the client the data"""
        client.send(dat)


class Sqlcommands():
    """a class that handles the communication with the database"""

    def __init__(self):
        """gets the sql database"""
        pass

    def get_movie(self, name):
        """returns the movie path and number of parts"""
        return PATH, 59

    def exists_in_base(self, param, value):
        """returns if exists in database"""
        return True


def rand_port():
    p = randint(3000, 7000)
    while True:
        mutex.acquire()
        l = threads
        mutex.release()
        if p in l:
            p = randint(3000, 7000)
        else:
            break
    return p



PATH = "D:\\from2\\"
#TMP_UPLOAD = 'E:\\tmp\\upload_tmp\\'
TMP_UPLOAD = "D:\\ab\\"
#PATH = "E:\\tmp\\test_subj\\"


server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 7777))
server_socket.listen(10)
open_client_sockets = []

#will be a dictionary that will be built from a port key and a request tuple
threads = {}
#will be the ipc controller
mutex = threading.Lock()

#handles the requests
com = Communication(server_socket)
#handles database
sql = Sqlcommands()

#main server loop
while True:
    rlist, wlist, xlist = select.select([server_socket]+open_client_sockets, [], [])

    #itarates over all of the requests
    for current_socket in rlist:
        #checks if a new socked connects
        if current_socket is server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
        else:
            #gets the data
            data = current_socket.recv(1024)
            #handles the client request
            com.handle_request(data, current_socket)
