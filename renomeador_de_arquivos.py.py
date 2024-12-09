import os
import glob
import time
import argparse
import shutil
#from PIL import Image



arquivos_antigos = []
NOME_DE_CLIENTES = (
	"KAMILA VERGNA - ", #0
	"BARCHE (IMPRESSAO E SUBLIMAÇÃO) - ", #1
	"GILCIMAR-(IMPRESSAO)-",#2
	"RAMONES GARCIA-(IMPRESSAO)-",#3
	"DUELO - (IMPRESSAO)-",#4
	"RE INDUSTRIA - (IMPRESSAO)-",#5
	"DANIELA -(IMPRESSÃO)-",#6
	"CASA FELIZ -(SUBLIMAÇÃO)-CANGA-",#7
	"YAMOH -(SUBLIMAÇÃO) - ",#8
	"DESTACK -(IMPRESSAO)",#9
	"MARGARETE ALVES -(SUBLIMAÇÃO)",#10
	"LILIANE GONÇALVES -(IMPRESSAO)",#11
	"BEATRIZ VICTOR -(SUBLIMAÇÃO)",#12
	"JOERLAINE -(SUBLIMAÇÃO)",#13
	"ESCOLA POLIVALENTE - ",#14
	"ESDRAS -(SUBLIMAÇÃO)",#15
	"NUBIA NUNES -(SUBLIMAÇÃO)",#16
	"CRISTIANE FERNADES -(SUBLIMAÇÃO)",#17
	"ROMULO -(SUBLIMAÇÃO LOCAL)",#18
	"IZAURA -(SUBLIMAÇÃO)",#19
	"IVANIA BORANA - (SUBLIMAÇÃO)", #20
	"ALEXANDRE - (SUBLIMAÇÃO)", #21
	"OK PRINT - ", #22
	"INFORGRAPH - ", #23
	"DRK EVENTOS - ", #24
	"ANEZIO - (IMPRESSAO) ", #25
	"SHOPEE - (CREPE SALINAS) - CANGAS ", #26
	)


def renomar_arquivos(path,flag,exte=".tif"):
	os.chdir(path)
	for arquivo in os.listdir("."):
		# _file = 
		if os.path.isfile(arquivo) and flag not in arquivo and exte in arquivo:
			new_name = f"{flag} {arquivo.upper()}"
			os.rename(arquivo,new_name)
		# if flag in arquivo:
		# 	text = arquivo.split(" ")[-1]
		# 	os.rename(arquivo,text)

		# 	print(text)

from PIL import Image

PREFIXO = 	"PATRICIA DOS SANTOS - (CREPE SALINAS) - CANGA "
FLAG_TECIDO = ""
caminho_base =  r"\\Storage-silkart\IMPRESSAO\09 12 2024\PATRICIA DOS SANTOS"
# os.chdir(caminho_base)
# for i,arquivo in enumerate(os.listdir(".")):
# 	# _file = 
# 	if os.path.isfile(arquivo):
# 		if "wha" in arquivo.lower():
# 			os.rename(arquivo,f"ARQUVIO {i}.tif")

# 		# img = Image.open(arquivo)
		# print(img.mode)
		# new_name = f"{flag} {arquivo.upper()}"
renomar_arquivos(
	caminho_base,
	PREFIXO
	)


