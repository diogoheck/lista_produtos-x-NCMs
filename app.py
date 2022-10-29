from openpyxl import load_workbook
import os

# ler a planilha das NCMs ST 
pasta_ncm = load_workbook('planilhas' + os.sep + 'NCMs_Alteradas.xlsx')
planilha_ncm = pasta_ncm['planilha_ncm']
# gerar uma lista de NCMs
lista_ncm = [str(linha[0]) for linha in planilha_ncm.values]
print(lista_ncm)
# ler a planilha de produtos (CSV)
# comparar a coluna das NCM dos produtos x NCMs ST
# se encontrar o produto com NCMs ST, pintar de amarelo
# salvar nova planilha de produtos 
