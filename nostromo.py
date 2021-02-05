#! /usr/bin/python
# slowcat --- Imprime un texto lentamente

# Author: Niwook
# Created: 30/05/2019
# Public domain
# Code: https://github.com/Niwook/Niwook_python
############################################################
import sys, time, os


delay = .1
exit = True

text = '''
Wellcome to comercial spaceship Nostromo.
I am the captain Dallas.
She is lt.Ripley.

Come in.

'''


def iter():
    for puntero in text_in:
        print("\033[1;32m" + puntero, end="")
        time.sleep(delay)
        sys.stdout.flush()
    if puntero > len.text:
        exit = False



while exit:
      try:
          text_in = text  # input()
          iter()
      except:
          break

os._exit(1)
######################################################################
# eof: slowcat.py
