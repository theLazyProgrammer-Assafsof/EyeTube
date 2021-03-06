# -*- coding: utf-8 -*-

'''import numpy as np
import cv2

# Capture video from file
cap = cv2.VideoCapture("D:\\dogs.mp4")

while True:

    ret, frame = cap.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)


        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()'''


'''import pygame
import time
import sys
import os

FPS = 30

pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie('D:\\here\\00.mpg')
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie_len = movie.get_length()

movie.set_display(movie_screen)
movie.play()

num = '01'
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if movie.get_time() >= movie_len:
        print num
        movie = pygame.movie.Movie('D:\\here\\' + num + '.mpg')
        movie.set_display(movie_screen)
        movie.play()

        num = str(int(num) + 1)
        if len(num) == 1:
            num = '0' + num
        while not os.path.exists('D:\\here\\' + num + '.mpg') and int(num) < 30:
            num = str(int(num) + 1)
            if len(num) == 1:
                num = '0' + num
        if num == '30':
            movie.stop()
            playing = False


    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)


pygame.quit()'''

'''import moviepy
import os
from moviepy.editor import *
import pygame

pygame.display.set_caption('Game title')

os.environ["SDL_VIDEO_CENTERED"] = "1"

clip = VideoFileClip("D:\\The_Hobbit_Trailer.mp4")

clip.preview()

execfile("startGame.py")'''

'''from moviepy.editor import *

clip = VideoFileClip("D:\\The_Hobbit_Trailer.mp4").fx(vfx.mirror_y)
ipython_display(clip, width=240)'''

"""import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        wf = wave.open(PATH + '000.wav', 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        part = 1
        data = wf.readframes(CHUNK)

        while data != '' and playing:
            stream.write(data)
            data = wf.readframes(CHUNK)

        while playing:

            wf = wave.open(PATH + get_part_video_num(part) + '.wav', 'rb')
            data = wf.readframes(CHUNK)

            while data != '' and playing:
                stream.write(data)
                data = wf.readframes(CHUNK)


            part += 1

        stream.stop_stream()
        stream.close()

        p.terminate()



def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 30
CHUNK = 1024
PATH = "E:\\tmp\\savesecachehere\\theslimvid\\"
#PATH = "E:\\tmp\\upload_tmp\\"


'''wf = wave.open(PATH + '000.wav', 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)'''


player = Music_player()


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + "000.mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()

player.start()

#part = 1
#data = wf.readframes(CHUNK)

#while data != '':
#    stream.write(data)
#    data = wf.readframes(CHUNK)

num = 1
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

        #wf = wave.open(PATH + get_part_video_num(part) + '.wav', 'rb')
        #data = wf.readframes(CHUNK)

        #part += 1

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
    #stream.write(data)
    #data = wf.readframes(CHUNK)


#stream.stop_stream()
#stream.close()

#p.terminate()
pygame.quit()"""




'''import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self, part):
        threading.Thread.__init__(self)
        self.part = part

    def run(self):

        wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        self.part += 1
        data = wf.readframes(CHUNK)

        while data != '' and playing:
            stream.write(data)
            data = wf.readframes(CHUNK)

        while playing:

            wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')
            data = wf.readframes(CHUNK)

            while data != '' and playing:
                stream.write(data)
                data = wf.readframes(CHUNK)
                if len(data) < CHUNK:
                    self.part += 1
                    wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')
                    data += wf.readframes(CHUNK)


            self.part += 1

        stream.stop_stream()
        stream.close()

        p.terminate()



def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 30
CHUNK = 1024
PATH = "E:\\tmp\\savesecachehere\\theslimvid\\"
#PATH = "E:\\tmp\\upload_tmp\\"

num = 47
player = Music_player(num)


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + get_part_video_num(num) + ".mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()

player.start()
num += 1

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()'''



"""import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self, part):
        threading.Thread.__init__(self)
        self.part = part

    def run(self):

        wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)


        while playing:
            stream.write(data)
            data = wf.readframes(CHUNK)
            if len(data) < CHUNK or data == '':
                self.part += 1
                wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')
                data += wf.readframes(CHUNK)



        stream.stop_stream()
        stream.close()

        p.terminate()



def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 30
CHUNK = 1024
PATH = "E:\\tmp\\savesecachehere\\theslimvid\\"
#PATH = "E:\\tmp\\upload_tmp\\"

num = 47
player = Music_player(num)


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + get_part_video_num(num) + ".mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()

player.start()
num += 1

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()"""


'''
import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self, part):
        threading.Thread.__init__(self)
        self.part = part
        self.next = False

    def run(self):

        wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)


        while playing:
            stream.write(data)
            data = wf.readframes(CHUNK)
            if len(data) < CHUNK or data == '':
                #self.part += 1
                #wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')
                wf = next_wf
                self.next = False
                #data += wf.readframes(CHUNK)



        stream.stop_stream()
        stream.close()

        p.terminate()





def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 30
CHUNK = 1024
PATH = "E:\\tmp\\savesecachehere\\theslimvid\\"
#PATH = "E:\\tmp\\upload_tmp\\"

num = 58
player = Music_player(num)
next_wf = None


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + get_part_video_num(num) + ".mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
player.start()
movie.play()

num += 1

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

    if not player.next:
        next_wf = wave.open(PATH + get_part_video_num(num) + '.wav', 'rb')
        player.next = True

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()'''



import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self, part):
        threading.Thread.__init__(self)
        self.part = part
        self.next = False
        self.streamnum = 1

    def run(self):

        #wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)


        while playing:
            if self.streamnum == 1:
                stream.write(data)
                data = wf.readframes(CHUNK)
            else:
                stream.write(data)
                data = wf2.readframes(CHUNK)
            if len(data) < CHUNK or data == '':
                #self.part += 1
                #wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')
                #wf = next_wf
                if self.streamnum == 1:
                    self.streamnum = 2
                else:
                    self.streamnum = 1
                self.next = False
                #data += wf.readframes(CHUNK)



        stream.stop_stream()
        stream.close()

        p.terminate()





def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 30
CHUNK = 1024
PATH = "E:\\tmp\\savesecachehere\\theslimvid\\"
#PATH = "E:\\tmp\\upload_tmp\\"

num = 58
wf = wave.open(PATH + get_part_video_num(num) + '.wav', 'rb')
wf2 = wave.open(PATH + get_part_video_num(num + 1) + '.wav', 'rb')
player = Music_player(num)
next_wf = None


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + get_part_video_num(num) + ".mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
player.start()
movie.play()

num += 1

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

    if not player.next:
        if player.streamnum == 2:
            wf = wave.open(PATH + get_part_video_num(num) + '.wav', 'rb')
        else:
            wf2 = wave.open(PATH + get_part_video_num(num) + '.wav', 'rb')
        player.next = True

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()



""" SCREWED ONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self, part):
        threading.Thread.__init__(self)
        self.part = part
        self.next = False
        self.dat = musicdata

    def run(self):

        #wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        #data = wf.readframes(CHUNK)


        while playing:
            stream.write(self.dat)
            self.dat = musicdata
            self.next = True
            #data = wf.readframes(CHUNK)
            '''if len(data) < CHUNK or data == '':
                #self.part += 1
                #wf = wave.open(PATH + get_part_video_num(self.part) + '.wav', 'rb')
                wf = next_wf
                self.next = False
                #data += wf.readframes(CHUNK)'''



        stream.stop_stream()
        stream.close()

        p.terminate()





def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 30
CHUNK = 1024
PATH = "E:\\tmp\\savesecachehere\\theslimvid\\"
#PATH = "E:\\tmp\\upload_tmp\\"

num = 58
numwf = num
wf = wave.open(PATH + get_part_video_num(numwf) + '.wav', 'rb')
wf2 = wave.open(PATH + get_part_video_num(num + 1) + '.wav', 'rb')
musicdata = wf.readframes(CHUNK ** 2)
player = Music_player(num)
next_wf = False


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + get_part_video_num(num) + ".mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

movie.set_display(movie_screen)
movie.play()
player.start()

num += 1

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

        #wf = wf2
        #wf2 = wave.open(PATH + get_part_video_num(num) + '.wav', 'rb')

    if wf.readframes(CHUNK) == '':
        numwf += 1
        print numwf, '?'
        #wf = wf2
        #wf2 = wave.open(PATH + get_part_video_num(numwf) + '.wav', 'rb')
        wf = wave.open(PATH + get_part_video_num(numwf) + '.wav', 'rb')
        #next_wf = False

    '''if not player.next:
        musicdata = wf.readframes(CHUNK ** 2)
    else:
        musicdata += wf.readframes(CHUNK ** 2)
        player.next = False'''

    if player.next:
        musicdata = ''
    else:
        musicdata += wf.readframes(CHUNK ** 2)


    '''if not player.next:
        next_wf = wave.open(PATH + get_part_video_num(num) + '.wav', 'rb')
        player.next = True'''

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
"""


"""
import pygame
import pyaudio
import wave
import threading


class Music_player(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        wf = wave.open("D:\\check_here\\sassy.wav", 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        part = 1
        data = wf.readframes(CHUNK)

        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

        '''while True:

            wf = wave.open("D:\\check_here\\" + get_part_video_num(part) + '.wav', 'rb')
            data = wf.readframes(CHUNK)

            while data != '':
                stream.write(data)
                data = wf.readframes(CHUNK)
                if len(data) < CHUNK:
                    part += 1
                    wf = wave.open("D:\\check_here\\" + get_part_video_num(part) + '.wav', 'rb')
                    data += wf.readframes(CHUNK)


            part += 1'''

        stream.stop_stream()
        stream.close()

        p.terminate()



def get_part_video_num(num):
    if len(str(num)) == 1:
        return '00' + str(num)
    elif len(str(num)) == 2:
        return '0' + str(num)
    else:
        return str(num)


FPS = 60
CHUNK = 4096
PATH = "D:\\mpsplits\\"


'''wf = wave.open(PATH + '000.wav', 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)'''


player = Music_player()


pygame.init()
clock = pygame.time.Clock()
movie = pygame.movie.Movie(PATH + "000.mpg")
screen = pygame.display.set_mode(movie.get_size())
movie_screen = pygame.Surface(movie.get_size()).convert()

player.start()
movie.set_display(movie_screen)
movie.play()

#part = 1
#data = wf.readframes(CHUNK)

#while data != '':
#    stream.write(data)
#    data = wf.readframes(CHUNK)

num = 1
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            movie.stop()
            playing = False

    if not movie.get_busy():
        print num
        movie = pygame.movie.Movie(PATH + get_part_video_num(num) + '.mpg')
        movie.set_display(movie_screen)
        movie.play()
        num += 1

        #wf = wave.open(PATH + get_part_video_num(part) + '.wav', 'rb')
        #data = wf.readframes(CHUNK)

        #part += 1

    screen.blit(movie_screen, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
    #stream.write(data)
    #data = wf.readframes(CHUNK)


#stream.stop_stream()
#stream.close()

#p.terminate()
pygame.quit()"""
