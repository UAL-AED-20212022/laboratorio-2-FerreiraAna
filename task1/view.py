#view
import controller as c
from models.LinkedList import LinkedList

lk = LinkedList()

def main():
    while True:
        commands = input().split() 

        if commands[0] == "RPI":
            pais_novo = commands[1]
            RPI(lk, pais_novo)

        elif commands[0] == "RPF":
            pais_novo = commands[1]
            RPF(lk, pais_novo)

        elif commands[0] == "RPDE":
            pais_novo = commands[1]
            pais_registado = commands[2]
            RPDE(lk, pais_registado, pais_novo)

        elif commands[0] == "RPAE":
            pais_novo = commands[1]
            pais_registado = commands[2]
            RPAE(lk, pais_registado, pais_novo)

        elif commands[0] == "RPII":
            pais_novo = commands[1]
            indice = int(commands[2])
            RPAE(lk, indice, pais_novo)
        
        elif commands[0] == "VNE":
            VNE(lk)

        elif commands[0] == "VP":
            nome_pais = commands[1]
            VP(lk, nome_pais)

        elif commands[0] == "EPE":
            EPE(lk)

        elif commands[0] == "EUE":
            EUE(lk)

        elif commands[0] == "EP":
            nome_pais = commands[1]
            EP(lk, nome_pais)

def RPI(lk, pais_novo):
    if (c.Registar_Pais_Inicio(lk, pais_novo) == 1):
        lk.traverse_list()

def RPF(lk, pais_novo): 
    if (c.Registar_Pais_Fim(lk, pais_novo) == 1):
        lk.traverse_list()

def RPDE(lk, pais_registado, pais_novo): 
    if (c.Registar_Pais_Depois_Elemento(lk, pais_registado, pais_novo) == 1):
        lk.traverse_list()

def RPAE(lk, pais_registado, pais_novo): 
    if(c.Registar_Pais_Antes_Elemento(lk, pais_registado, pais_novo) == 1):
        lk.traverse_list()

def RPII(lk, indice, pais_novo): 
    if(c.Registar_Pais_Indice(lk, indice, pais_novo) == 1):
        lk.traverse_list()

def VNE(lk):
    if (c.Verificar_Numero_Elementos(lk) == 1):
        print(f"O número de elementos são {lk.get_count()}")

def VP(lk, nome_pais):
    if (c.Verificar_Pais(lk, nome_pais) == 1):
        print(f"O país {nome_pais} não se encontra na lista")
    elif (c.Verificar_Pais(lk, nome_pais) == -1):
        print(f"O país {nome_pais} encontra-se na lista")

def EPE(lk):
    if (c.Eliminar_Primeiro_Elemento(lk) == 1):
        elemento = lk.start_node.item
        print(f"O país {elemento} foi eliminado da lista")

def EUE(lk):
    if (c.Eliminar_Ultimo_Elemento(lk) == 1):
        elemento = lk.get_last_node()
        print(f"O país {elemento} foi eliminado da lista")

def EP(lk, nome_pais):
    if (c.Eliminar_Pais(lk, nome_pais) == 1):
        print(f"O país {nome_pais} não se encontra na lista")
    elif (c.Eliminar_Pais(lk, nome_pais) == -1):
        print(f"O país {nome_pais} foi eliminado da lista") 