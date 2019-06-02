#! /usr/bin/python
# slowcat --- Imprime un archivo lentamente

# Author: Niwook
# Created: 30/05/2019
# Public domain
# Commentary: Basado en el código de Grox.net
# Code: https://grox.net/software/mine/slowcat/slowcat.py
############################################################
import sys, time, os, pyglet


delay = .1
pyglet.options['audio'] = ('openal', 'pulse', 'silent')
sound = pyglet.resource.media('typesimple.wav', streaming=False)
sound1 = pyglet.resource.media('type.wav', streaming=False)
sound2 = pyglet.resource.media('beep.wav', streaming=False)
sound3 = pyglet.resource.media('ready.wav', streaming=False)
sound4 = pyglet.resource.media('doublebeep.wav', streaming=False)


# Poner la ayuda y activar o no el sonido y ver o no la parafernalia ▀ ▀ ▀
if len(sys.argv) > 1:
    arg = sys.argv[1]
    if arg != "-d":
        print("usar: %s [-d delay]" % (sys.argv[0]))
        print("delay: retraso en segundos")
        print("ejemplo: %s -d .02 < archivo" % (sys.argv[0]))
        sys.exit()
    if len(sys.argv) > 2:
        delay = float(sys.argv[2])
        os.system('clear')

def iter():
    for puntero in text_in:
        print("\033[1;32m" + puntero, end="")
        time.sleep(delay)
        sys.stdout.flush()
        if delay == .1:
            sound.play()
        elif delay < .1:
            sound1.play()
        else:
            sound2.play()
    sound2.play()



sound2.play()
sound3.play()

scale = 30
print("\033[22;32m" + " Iniciando transmisión ".center(scale * 2, '░'))
print ("\n")
t = time.perf_counter()
for i in range(scale + 1):
    a = '█' * i
    b = '░' * (scale - i)
    c = (i / scale) * 100
    t -= time.perf_counter()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, -t), end='')
    time.sleep(0.05)
print ("\n")


while True:
      try:
          text_in = input()
          print('')
          iter()


      except:
          break


sound4.play()
print ("\n")
sound3.play()
time.sleep(2)
print("\033[22;32m" + " Transmisión finalizada ".center(scale * 2, '░')  + "\033[1;39m")
print ("\n")
os._exit(1)
pyglet.app.run()
######################################################################
# eof: slowcat.py
