from PIL import Image
import numpy as np
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from base64 import b64encode


class DESImageCipher:
    # Image
    url = None  # Ruta completa de la imagen
    image = None  # Objeto de la imagen
    image_name = None  # nombre de imagen sin extensiones
    path = None  # Ruta de la carpeta de la imagen
    image_size = None  # Resolucion de la iamgen
    image_ext = None

    # Cipher
    key = None
    iv = None
    mode = DES.MODE_ECB

    def __init__(self):
        pass

    def setImagePath(self, ruta: str):
        self.url = ruta
        aux = ruta.split("/")
        name = aux[-1].split(".")
        self.image_ext = name[-1]
        self.image_name = name[0]
        self.path = self.url.replace(aux[-1], "")

    def setKey(self, key: bytes):
        if(len(key) == 8):
            self.key = key
        else:
            self.key = pad(key, 8)

    def setIv(self, iv: bytes):
        if(len(iv) == 8):
            self.iv = iv
        else:
            self.iv = pad(iv, 8)

    def setMode(self, modo: str):
        if(modo == 'ECB'):
            self.mode = DES.MODE_ECB
        elif(modo == 'CBC'):
            self.mode = DES.MODE_CBC
        elif(modo == 'CFB'):
            self.mode = DES.MODE_CFB
        elif(modo == 'OFB'):
            self.mode = DES.MODE_OFB
        else:
            print("Mode not recognized")

    def getMode(self):
        if(self.mode == DES.MODE_ECB):
            return "ECB"
        elif(self.mode == DES.MODE_CBC):
            return "CBC"
        elif(self.mode == DES.MODE_CFB):
            return "CFB"
        elif(self.mode == DES.MODE_OFB):
            return "OFB"
        else:
            return None

    def encrypt(self):
        if(self.url != None and self.key != None):
            img = Image.open(self.url)
            self.image = np.array(img)
            self.image_size = img.size
            new_url = self.path + self.image_name + "_e" + self.getMode() + "." + self.image_ext

            cipher = None
            if(self.getMode() != "ECB"):
                cipher = DES.new(self.key, self.mode, iv=self.iv)
            else:
                cipher = DES.new(self.key, self.mode)

            ct_bytes = cipher.encrypt(
                pad(
                    self.image.tobytes(),
                    DES.block_size,
                )
            )
            img_data = np.frombuffer(ct_bytes)

            image_nva = Image.frombuffer(
                "RGB",
                self.image_size,
                img_data
            )
            image_nva.save(
                new_url
            )

    def decrypt(self):
        if(self.url != None and self.key != None):
            img = Image.open(self.url)
            self.image = np.array(img)
            self.image_size = img.size

            new_url = self.path + self.image_name + "_d" + self.getMode() + "." + self.image_ext
            cipher = None
            if(self.getMode() != "ECB"):
                cipher = DES.new(self.key, self.mode, iv=self.iv)
            else:
                cipher = DES.new(self.key, self.mode)

            aux = self.image.tobytes()
            pt = cipher.decrypt(
                aux
            )

            img_data = np.frombuffer(pt)

            Image.frombuffer(
                "RGB",
                self.image_size,
                img_data
            ).save(
                new_url
            )