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

# Funcion para construir la URL a la que conectarse.
def build_url(symb):
  #connector = '?s='
  form_url = 'https://seekingalpha.com/symbol/' + symb.upper() + 'income-statement' 
  #connector + symb.lower()
#  symbol_url = symbol_url + [fomr_url]
  return form_url

# TODO modulo que recibe lista de urls y conecta con SeekingAlpha para descargar
# los datos.
def Download(url):
  

# TODO Permitir mas opciones con sus argumentos. Parse en bucle las opciones y
# las agrupa con sus argumentos para mejorar la busqueda.
# IDEA 1: opcion '-n' seguido del nombre que se da al directorio con los
# archivos descargados.
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

# Build the list of urls based on symbol name.
for symb in args:
  url_list = url_list + [build_url(symb)]
#TESTING
print (args)
print (url_list)
