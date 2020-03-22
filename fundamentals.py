# Programa que descarga datos de info fundamental por empresas desde Seeking
# Alpha
# Objetivo: descargar archivos, fusionarlos e idealmente, calcular datos extra.

import requests
from bs4 import BeautifulSoup as bs
import urllib3
#import wget
import os
import sys

head = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "X-Requested-With": "XMLHttpRequest"
}
url_list = []
#symbol_url = []
# Funcion para construir la URL a la que conectarse.
def build_url(symb):
  connector = '?s='
  form_url = 'https://seekingalpha.com/symbol/' + symb.upper() + connector + symb.lower()
#  symbol_url = symbol_url + [fomr_url]
  return form_url


# TODO Debe aceptar parametros que son los simbolos de las empresas en bolsa.
# Accede a seeking alpha y descarga los datos de fundamentales disponibles.

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# TODO add more options. Idealmente, habria varios args por cada opt. Por ahora
# es suficiente con esto.

# Build the list of urls based on symbol name.
for symb in args:
  url_list = url_list + [build_url(symb)]
#TESTING
print (args)
print (url_list)
