# https://pypi.org/project/PyAutoGUI/
# pip install PyAutoGUI
import pyautogui

anotacoes = []
while True:
    op = pyautogui.confirm('BLOCO DE NOTAS:\n\n'+ str(anotacoes),
     buttons=['Adicionar', 'Listar', 'Sair'])
    if op == 'Adicionar':
        nota = pyautogui.prompt('Digite a nota abaixo: \n\n\n\n')
        if nota != None:
            anotacoes.append(nota)
    elif op == "Listar": 
        pyautogui.alert('Lista de anotações: \n\n' + str(anotacoes))
    if (op == 'Sair'):
        break