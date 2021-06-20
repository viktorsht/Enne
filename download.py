from time import sleep
from msgs import Mensagens
import pafy
import os
import sys


class Download:
    def __init__(self,url):
        self.url = url
        self.video = pafy.new(self.url)
        self.nome_arquivo = None
        self.pasta_arquivo = '/home/mr-santos/'
    def go_download(self):
        try:
            audio_musica = self.video.getbestaudio()
            self.nome_arquivo = self.pasta_arquivo +str(self.video.title) + '.mp3'
            audio_musica.download(self.nome_arquivo)
        except:
            return Mensagens.erro_download()
