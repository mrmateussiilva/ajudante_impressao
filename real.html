from os import listdir
from PIL import Image, ImageOps,ImageDraw,ImageFont
from os.path import join,splitext,isfile,split
import os
import functools

Image.MAX_IMAGE_PIXELS = None
SIZE = 640,640
FONT = ImageFont.truetype(r"C:\Users\Usuario\Desktop\arialbd.ttf", 46)


class ImagePy:
    def __init__(self) -> None:
        self.mode = "RGB"


    def pixel_for_cm(self,size,dpi):
        if len(size) == 2:
            return tuple(map(lambda x: round(x),map(lambda x: 2.54 * (x / dpi),size)))
        else: (0,0)


    def info_image(self,filename):
        with Image.open(filename) as img:
            dpi = int(img.info['dpi'][0])
            size_px = img.size
            size_cm = self.pixel_for_cm(size_px,dpi)
            #print(f"Tamanho(CM): {size_cm}, DPI: {dpi}, MODE: {img.mode}")
            return dpi,size_cm,size_px


    def pad_top(self,filename:str,color:str="white"):
        sizepad = 46 #PX
        dpi,size_cm,size_px = self.info_image(filename)
        size = size_px[0], size_px[1] + sizepad
        with Image.open(filename) as img:
            #print(size_cm)
            #print(self.pixel_for_cm(size,dpi))
            imgpad = ImageOps.pad(img, size,centering=(0,1), color=color)
            name = get_name_painel(filename)
            draw = ImageDraw.Draw(imgpad)
            draw.text((0,0),name,font=FONT,fill="black")
            imgpad.save(filename,dpi=(dpi,dpi))



def create_thumbnail(filename:str,path_dest:str,size:tuple=(640,640)) -> None:
    """
    Create miniature  the files for tifs
     filename: str = Caminho completo do arquivo
     path_dest: str = Caminho da pasta de destino do novo arquivo
     size: tuple[int,int] = Largura e altura em pixels da thumbnail


    """
    __,n = split(filename)
    new = f"bolsinha__{n.replace('tif','bmp')}"
    new_name = join(path_dest,new)
    with Image.open(filename) as im:
        print(f"{new_name}")
        im.thumbnail(size)
        im.save(new_name)


def gerar_bolsinhas(path_src:str,path_dst:str)  -> None:
    path_dest  = r"\\Storage-silkart\IMPRESSAO\26 08 2024\BOLSINHAS\PARA FAZER"
    for data in listdir(path_src):
        __file = join(path_src,data)
        if isfile(__file) and "tif" in __file:
            criar_miniatura(SIZE,__file, path_dest)


def get_name_painel(pathfile:str) -> str:
    p,e = splitext(pathfile)
    s,m = split(p)
    return m.split("-")[0]


#@functools.lru_cache()
def monitor(path,exte="tif"):
    imagepy = ImagePy()
    for file in listdir(path):

        if isfile(join(path,file)) and exte in file:
            print(get_name_painel(file))
            imagepy.pad_top(join(path,file))
            # breakpoint
            # print(file)



if __name__ == "__main__":
    # path = r"\\Storage-silkart\IMPRESSAO\01 10 2024\RENOMEAR"
    # monitor(path)
    gerar_bolsinhas(r"\\Storage-silkart\IMPRESSAO\09 12 2024\BOLSINHAS\PARA FAZER",r"\\Storage-silkart\IMPRESSAO\09 12 2024\BOLSINHAS\PARA FAZER")