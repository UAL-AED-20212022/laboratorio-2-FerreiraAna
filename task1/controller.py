from models.LinkedList import LinkedList

def Registar_Pais_Inicio(lk, pais_novo):
    lk.insert_at_start(pais_novo)
    return 1

def Registar_Pais_Fim(lk, pais_novo):
    lk.insert_at_end(pais_novo)
    return 1

def Registar_Pais_Depois_Elemento(lk, pais_registado, pais_novo):
    lk.insert_after_item(pais_registado, pais_novo)
    return 1

def Registar_Pais_Antes_Elemento(lk, pais_registado, pais_novo):
    lk.insert_before_item(pais_registado, pais_novo)
    return 1

def Registar_Pais_Indice(lk, pais_novo, indice):
    lk.insert_at_index(indice, pais_novo)
    return 1

def Verificar_Numero_Elementos(lk):
    return 1

def Verificar_Pais(lk, nome_pais):
    if (lk.search_item(nome_pais) == False):
        return 1
    elif (lk.search_item(nome_pais) == True):
        return -1

def Eliminar_Primeiro_Elemento(lk):
    lk.delete_at_start()
    return 1

def Eliminar_Ultimo_Elemento(lk):
    lk.delete_at_end()
    return 1

def Eliminar_Pais(lk, nome_pais):
    if (lk.search_item(nome_pais) == False):
        return 1 
    elif (lk.search_item(nome_pais) == True):
        lk.delete_element_by_value(nome_pais)
        return -1

        