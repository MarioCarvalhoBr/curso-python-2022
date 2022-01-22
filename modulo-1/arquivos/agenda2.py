#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
import sys

# ver agenda toda
def mostra_todos_registros(agenda):
   for nome in agenda:
      print (nome, agenda[nome])

# insere alguem
def insere(agenda, nome, telefone):
   agenda[nome] = telefone

# mostra um determinado nome da agenda
def busca(agenda, nome):
   try:
      print (nome, agenda[nome])
   except Exception:
      print (nome, 'não está na agenda.')

# apaga alguém
def apaga(agenda, nome):
   try:
      del agenda[nome]
   except Exception:
      print (nome, 'não está na agenda.')

# apaga todos os nomes da agenda
def limpa(agenda):
   for nome in agenda:
      del agenda[nome]

# ajuda para --help
def ajuda():
   print ("Uso:")
   print (sys.argv[0], "[comando] [parâmetros]")
   print ("--help: mostra esta ajuda")
   print ("--show NOME: mostra o NOME e seu respectivo telefone")
   print ("--show: mostra todos os nomes. É a operação padrão")
   print ("--add NOME TELEFONE: adiciona NOME e TELEFONE para a agenda")
   print ("--del NOME: remove NOME e seu respectivo telefone da agenda")
   print ("--clean: apaga todos os nomes da agenda")
   
def main():
   # se não for passado nenhum comando, o comando eh para mostrar tudo
   if len(sys.argv) == 1:
      comando = "show"
   else:
      comando = sys.argv[1]
   comando.lower()
   
   # abre a agenda
   agenda = shelve.open('agenda.db')

   # help
   if comando in ("help", "-h", "--help", "ajuda"):
      ajuda()
   # visualização
   elif comando in ("show", "-s", "--show"):
      if len(sys.argv) == 1 or len(sys.argv) == 2:
         mostra_todos_registros(agenda)
      elif len(sys.argv) == 3:
         nome = sys.argv[2]
         busca(agenda, nome)
      else:
         ajuda()
   # deleção
   elif comando in ("del", "-d", "-del", "--del", "delete"):
      if len(sys.argv) == 3:
         nome = sys.argv[2]
         apaga(agenda, nome)
      else:
         ajuda(bin)
   # inserção
   elif comando in ("add", "-a", "-add", "--add"):
      if len(sys.argv) == 4:
         nome = sys.argv[2]
         tel = sys.argv[3]
         insere(agenda, nome, tel)
      else:
         ajuda()
   # destruição
   elif comando in ("clean", "-c", "-clean", "--clean"):
      limpa(agenda)
   else:
      ajuda()
   
   # fecha o banco
   agenda.close()

if __name__ == "__main__":
   main()   