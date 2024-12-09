from PIL import Image, ImageOps,ImageDraw,ImageFont


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
