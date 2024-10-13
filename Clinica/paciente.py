import sys
import os

# Adicionando o diretorio "Clínica" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class Paciente:
    # começar aqui se inspirando nas outras classes da pasta Restaurante