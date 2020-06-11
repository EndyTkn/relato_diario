import time
import datetime
from lib.Relatorio import Relatorio

BLANK_SPACE = "     "
class HomeView:
    def __init__(self):
        self.relatorio = Relatorio()

    def iniciar(self):
        self.carrega_interface()

    def carrega_interface(self):
        self.listar_relatos()
        while(True):
            self.carrega_adicionar_realatorio()

        
    def carrega_adicionar_realatorio(self):
        hora = time.strftime("%Hh:%Mm:%Ss")
        relato = input('{}{}: '.format(BLANK_SPACE, hora))
        if(relato == ""):
            exit('Relatório Finalizado')

        self.relatorio.adicionar_relato([hora, relato])

    def listar_relatos(self):
        relatorio = self.relatorio.get_relatorio()
        dia = ""
        for dia in relatorio:
            print('{}:'.format(dia))
            for relato in relatorio[dia]:
                print('{}{}: {}'.format(BLANK_SPACE ,relato[0], relato[1]))
        if (dia != str(datetime.date.today())):
            print(str(datetime.date.today()))


