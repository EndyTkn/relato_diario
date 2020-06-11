import json
import datetime

class Relatorio:
    def __init__(self):
        self.relatorio = {}
        self.caminho_arquivo = "./lib/relatorio.json"

        self.carregar_realatorio()

    def carregar_realatorio(self):
        try:
            with open(self.caminho_arquivo, 'a+') as arquivo_relatorio:
                arquivo_relatorio.seek(0)
                arquivo_string = arquivo_relatorio.read()
                if (arquivo_string == ''):
                    return
                self.relatorio = json.loads(arquivo_string)
        except Exception:
            raise

    def adicionar_relato(self, relato):
        dia = str(datetime.date.today())
        if (dia not in self.relatorio):
            self.relatorio[dia] = [
                relato
            ]
        else:
            self.relatorio[dia].append(relato)
        try:
            with open(self.caminho_arquivo, 'w') as arquivo_relatorio:
                arquivo_relatorio.write(json.dumps(self.relatorio, sort_keys=True))
        except Exception:
            raise


    def get_relatorio(self):
        return self.relatorio

        
        
        


    