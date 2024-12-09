
import os
from time import sleep
from PIL import Image
from os.path import join,isfile,split
from functools import lru_cache
import json
# from pprint import pprint as print

SIZE = 600,600
Image.MAX_IMAGE_PIXELS = None
def criar_miniatura(size:tuple, filename:str,path_dest:str) -> None:
    """
    Create miniature for files tifs
     size tuple[int,int] = 

    """
    __,n = split(filename)
    new = f"bolsinha__{n.replace('tif','jpg')}"
    new_name = join(path_dest,new)
    with Image.open(filename) as im:
        print(f"{new_name}")
        im.thumbnail(size)
        im.save(new_name)


def gerar_bolsinhas(path_src:str,dst:str)  -> None:
    # for data in os.listdir(path_src):
    # 	print(data)

    #     # __file = join(path_src,data)
    if isfile(path_src) and "tif" in path_src:
        criar_miniatura(SIZE,path_src, dst)



@lru_cache()
def search_deep_files(path:str) -> list:
	t = []
	for root,dirs,files in os.walk(path):
		if len(dirs) > 1:
			for d in dirs:
				for data in os.listdir(join(root,d)):
					p =join(root,d,data)
					if os.path.isfile(p):
						t.append(p)
	return t

def search_in_files(files,target) -> any:
	results = []
	for file in files:
		with open(file,"r") as fp:
			data = json.load(fp)
			for keys,values in data.items():
				nome = values.get("ARQUIVO").lower()
				if target in nome:
					# print(values)
					# print("\n")
					results.append(values)
	return results


@lru_cache()
def search_design_storage(target:str) -> list:
	t = []
	alvo = target.lower()
	path_base = r"\\Storage-silkart\IMPRESSAO\MATEUS\bmps_temps"
	for root,dirs,files in os.walk(r"\\Storage-silkart\DESIGN"):
		if len(dirs) > 1:
			for d in dirs:
				for data in os.listdir(join(root,d)):
					p =join(root,d,data)
					# print(data)
					if os.path.isfile(p) and alvo in data.lower():

						b = gerar_bolsinhas(p,path_base)
						print(p)
						# t.append(p)

	# return t



if __name__ == "__main__":
	# alvos = ["retangular","cilindros"]
	# for alvo in alvos:
	# 	print(alvo)
	# 	search_design_storage(alvo)
	files = search_deep_files(r"\\Storage-silkart\IMPRESSAO\LOGS DAS MAQUINAS\ARQUIVOS_JSON")
	term = "CASA FELIZ - TOALHA BURRO - BURRO ".lower()
	results = search_in_files(files,term)

	for result in results:
		name = result.get("ARQUIVO")
		# print(name)

		if term 	 in name.lower():
			for v in result.values():

				print(f"\t{v}")
			print("\n\n")

		# print(f'{name} ,\t{result.get("INÍCIO, DATA E HORA DO RIP")}')

	# print(results)
					
