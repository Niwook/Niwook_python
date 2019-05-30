#! /usr/bin/python
# slowtype --- Imprime un archivo léntamente

# Author: Niwook
# Created: 30/05/2019
# Public domain
# Commentary: Basado en el código de Grox.net
# Code: https://grox.net/software/mine/slowcat/slowcat.py
############################################################
import sys, time, os


delay = .02


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
        print("\033[1;36m" + puntero, end="" + "\033[1;39m")
        time.sleep(delay)
        sys.stdout.flush()


while True:
      try:
          text_in = input()
          print('')
          iter()


      except:
          break


print ("\n")
######################################################################
# eof: slowcat.py
