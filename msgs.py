class Mensagens:
    def __init__(self):
        self.e_download = "Erro download não completado!"
        self.status_inicializar = "Inicializando!"

    def erro_download(self):
        return self.e_download

    def inicializar(self):
        return self.status_inicializar
