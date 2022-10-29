from openpyxl import load_workbook
import os

def ler_planilha_excel_ncm_st():
    pasta_ncm = load_workbook('planilhas' + os.sep + 'NCMs_Alteradas.xlsx')
    planilha_ncm = pasta_ncm['planilha_ncm']
    lista_ncm = [str(linha[0]) for linha in planilha_ncm.values]
    return lista_ncm

