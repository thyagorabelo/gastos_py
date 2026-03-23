import os
import webbrowser
from modulos import html

lista_de_arquivos = ["Janeiro.txt", "Fevereiro.txt", "Março.txt"]
for fname in lista_de_arquivos:
    webbrowser.open("file://" + os.path.realpath(html.produce_bar_chart(fname)))