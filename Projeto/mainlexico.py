# -*- coding: utf-8 -*-

# # Universidade Federal de Goiás
# Instituto de Informática - INF
# Compiladores - Compilador para MGol
#
# Módulo: Main
# Função principal do programa, que
# integra todos os outros módulos do
# compilador
#
# Alunos: Carlos Henrique Rorato Souza
# e Larissa Santos de Azevedo

import sys
from Lexico.tabelaTransicao import *
from Lexico.tabelaSimbolos import *
from Lexico.analisadorLexico import *

#Criação e preenchimento da tabela de transições do DFA
TabelaTransicao = []
preenche_tabela_dfa(TabelaTransicao)

#Criação e preenchimento da tabela de símbolos
TabelaSimbolos = preenchePalavrasReservadas()

argumentos = sys.argv

arq = open("teste.mgol", encoding="utf-8")


while(1):
    resultado = analisadorLexico(arq, TabelaTransicao, TabelaSimbolos)
    if resultado:
        if resultado.get("token") == "$":
            print(resultado)
            break
        else:
            print(resultado)

arq.close() 