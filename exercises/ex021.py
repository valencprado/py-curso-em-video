# programa que abra e reproduza o áudio de um arquivo MP3.
# fazendo com o guanabara 🤓
import pygame
pygame.init()
pygame.mixer.music.load("paramore.mp3")
pygame.mixer.music.play()
pygame.event.wait()
