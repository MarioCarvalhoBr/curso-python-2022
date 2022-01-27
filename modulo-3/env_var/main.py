import os
import pandas as pd
import time

# Pega uma variavel de ambiente
valor = os.environ.get("VALOR")
print("valor: ", valor)

# Cria uma variavel de ambiente
os.environ['PANDAS_VERSAO'] = pd.__version__

pd_versao = os.environ.get('PANDAS_VERSAO')
print("pd_versao: ", pd_versao)

# Precisa de permissão do ADM
# Seta as var env no sistema
os.system("SETX {0} {1} /M".format("NOME_VARIAVEL", "VALOR_VARIAVEL"))
os.system("SETX {0} {1} /M".format("MARIO_IDADE", "24"))
