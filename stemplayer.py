import pygame
import sys
import os
import serial
import platform

pygame.init()

screen = pygame.display.set_mode((1024, 786))
pygame.display.set_caption('discord is not recognizing this for some reason')

serialInst = serial.Serial()
serialInst.baudrate = 9600
if platform.system() == 'Windows':
    serialInst.port = 'COM3'
else:
    serialInst.port = "/dev/cu.usbmodem14501" # COM3 for widnwos

print(os.listdir('stems')[0])
print(os.listdir('stems'))

class Stems():
    stem_list = []
    stem_key_list = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h]
    current_song = ""
    hardware = True
    def __init__(self):
        for i in sorted(os.listdir(f'stems/{self.current_song}')):
            self.stemhandler(i)
            print(i)
        for stem in self.stem_list:
            stem.play()
            print(f"Playing stem")

    def stemhandler(self, path):
        track = pygame.mixer.Sound(f'stems/{self.current_song}/{path}')
        track.set_volume(1)
        self.stem_list.append(track)

stems = Stems()
clock = pygame.time.Clock()

try:
    serialInst.open()
except:
    stems.hardware = False

MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MUSIC_END:
            screen.fill((91,91,91))
        for i in range(len(stems.stem_list)):
            if event.type == pygame.KEYDOWN:
                if event.key == stems.stem_key_list[i] and stems.stem_list[i].get_volume() == 0:
                    stems.stem_list[i].set_volume(1)
                    print('resumed')
                    break
                if event.key == stems.stem_key_list[i] and stems.stem_list[i].get_volume() != 0:
                    stems.stem_list[i].set_volume(0)
                    print('muted')
                    break
    
    if stems.hardware:
        if serialInst.in_waiting:
            print((serialInst.readline().decode('utf-8')))
            listofvol = serialInst.readline().decode('utf-8').split('|')
            for i in range(len(stems.stem_list)):
                stems.stem_list[i].set_volume(int(listofvol[i])/100)     


    pygame.display.update()
    clock.tick(60)
