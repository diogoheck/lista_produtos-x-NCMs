def ncm_produto_x_ncm_alteradas(NCM, lista_ncm):
    NCM = str(NCM)
    if NCM[0:8] in lista_ncm:
        return True
    elif NCM[0:7] in lista_ncm:
        return True
    elif NCM[0:6] in lista_ncm:
        return True
    elif NCM[0:5] in lista_ncm:
        return True
    elif NCM[0:4] in lista_ncm:
        return True
    elif NCM[0:3] in lista_ncm:
        return True
    elif NCM[0:2] in lista_ncm:
        return True

    return False

