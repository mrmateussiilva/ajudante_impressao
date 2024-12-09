import os 
from os import listdir
from os.path import join,splitext,split



p = r"C:\Users\Usuario\Downloads"
extensoes = "jpeg","bmp","pdf","zip"
os.chdir(p)
for file in listdir("."):
	n,e = splitext(file)
	if e.replace(".","") in extensoes:
		os.remove(file)
	print(e)