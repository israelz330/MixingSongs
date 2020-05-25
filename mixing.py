import sys, pygame
pygame.init()
size = width, height = 200, 100
screen = pygame.display.set_mode(size)
i = 0

listaDeReproduccion = [
    'C:/Users/isrzap/Downloads/sample.MP3',
    'C:/Users/isrzap/Downloads/sampleWAV.WAV',
    'C:/Users/isrzap/Downloads/sampleOGG.OGG'
]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.mixer.music.get_busy() == False:
        print("Reproduciendo: " + listaDeReproduccion[i])
        pygame.mixer.music.load(listaDeReproduccion[i])
        pygame.mixer.music.play()
        i = i + 1


