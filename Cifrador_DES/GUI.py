import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from DES import *


class GUI():
    background_color = "#0d0159"
    white = "#fff"
    select_color = "#4326fc"
    show_inputs = False
    last_option = 0
    window = None
    frame = None
    cipher = None
    selected = False
    option_action = 0
    option_mode = 0

    path_message = ""
    plaintext = ""

    choose_file = False

    dynamic_widgets = []

    def __init__(self):
        self.window = Tk()
        self.window.title("Practica 1: Cifrador DES")
        self.window.config(bg=self.background_color)
        self.window.resizable(0, 0)

        frame1 = LabelFrame(self.window, background=self.background_color)
        frame1.grid(row=0,column=0,padx=5,pady=5)

        self.label_opt = Label(frame1,
                                text="Selecciona la acción",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
        self.label_opt.grid(row=0,column=0,padx=5,pady=5,columnspan=2,sticky="ew")

        option_action = IntVar()

        self.radioButton4 = Radiobutton(frame1,
                                        text="Cifrar",
                                        variable=option_action,
                                        value=1,
                                        bg=self.background_color,
                                        selectcolor=self.select_color,
                                        fg=self.white,
                                        font=("Arial", 12),
                                        command = lambda: self.selectButton_Action(option_action.get())
                                        )
        self.radioButton4.grid(row=1,column=0, padx=5,pady=5,sticky="ew")

        self.radioButton5 = Radiobutton(frame1,
                                        text="Descifrar",
                                        variable=option_action,
                                        value=2,
                                        bg=self.background_color,
                                        selectcolor=self.select_color,
                                        fg=self.white,
                                        font=("Arial", 12),
                                        command = lambda: self.selectButton_Action(option_action.get())
                                        )
        self.radioButton5.grid(row=1,column=1, padx=5,pady=5,sticky="ew")

        label_Mode = Label(frame1,
                            text="Selecciona el modo de operación",
                            fg=self.white,
                            bg=self.background_color,
                            font=("Arial", 14)
                            )
        label_Mode.grid(row=2,column=0,padx=5,pady=5,columnspan=2,sticky="ew")

        option_mode = IntVar()
        radioButton0 = Radiobutton(frame1,
                                    text="ECB",
                                    variable=option_mode,
                                    value=1,
                                    bg=self.background_color,
                                    selectcolor=self.select_color,
                                    fg=self.white,
                                    font=("Arial", 12),
                                    command=lambda: self.selectButton_function(option_mode.get())
                                    )
        radioButton0.grid(row=3,column=0,padx=5,pady=5,sticky="ew")

        radioButton1 = Radiobutton(frame1,
                                    text="CBC",
                                    variable=option_mode,
                                    value=2,
                                    bg=self.background_color,
                                    selectcolor=self.select_color,
                                    fg=self.white,
                                    font=("Arial", 12),
                                    command=lambda: self.selectButton_function(option_mode.get())
                                    )
        radioButton1.grid(row=3,column=1,padx=5,pady=5,sticky="ew")

        radioButton2 = Radiobutton(frame1,
                                    text="CFB",
                                    variable=option_mode,
                                    value=3,
                                    bg=self.background_color,
                                    selectcolor=self.select_color,
                                    fg=self.white,
                                    font=("Arial", 12),
                                    command=lambda: self.selectButton_function(option_mode.get())
                                    )
        radioButton2.grid(row=4,column=0,padx=5,pady=5,sticky="ew")

        radioButton3 = Radiobutton(frame1,
                                    text="OFB",
                                    variable=option_mode,
                                    value=4,
                                    bg=self.background_color,
                                    selectcolor=self.select_color,
                                    fg=self.white,
                                    font=("Arial", 12),
                                    command=lambda: self.selectButton_function(option_mode.get())
                                    )
        radioButton3.grid(row=4,column=1,padx=5,pady=5,sticky="ew")

    def run(self):
        self.window.mainloop()

    def selectButton_Action(self, option):
        self.destroyDynamicWidgets()
        self.option_action = option

    def destroyDynamicWidgets(self):
        self.path_message = ""
        self.plaintext = ""
        for i in self.dynamic_widgets:
            i.destroy()

    def selectButton_function(self, option):
        self.option_mode = option
        self.destroyDynamicWidgets()
        if(self.option_action == 1):
            self.generateEncryptWidgets()
        elif(self.option_action == 2):
            self.generateDecryptWidgets()


    def generateEncryptWidgets(self):
        if(self.option_mode != 1):
            frame3= LabelFrame(self.window, background=self.background_color)
            frame3.grid(row=2,column=0, padx=5,pady=5)

            self.dynamic_widgets.append(frame3)

            label_key = Label(frame3,
                                text="Llave",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
            label_key.grid(row=0,column=0, padx=5,pady=5)
            self.dynamic_widgets.append(label_key)
            input_key = Entry(frame3)
            input_key.grid(row=0,column=1, padx=5,pady=5)
            self.dynamic_widgets.append(input_key)

            label_iv = Label(frame3,
                                text="Vector Inicial",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
            label_iv.grid(row=0,column=2, padx=5,pady=5)
            self.dynamic_widgets.append(label_iv)
            input_iv = Entry(frame3)
            input_iv.grid(row=0,column=3, padx=5,pady=5)
            self.dynamic_widgets.append(input_iv)
            FileBtn = Button(frame3,
                                text="Buscar Imagen",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.pathFile()
                                )
            FileBtn.grid(row=1,column=0, padx=5,pady=5,columnspan=2,sticky="ew")
            self.dynamic_widgets.append(FileBtn)
            EncryptBtn = Button(frame3,
                                text="Cifrar",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.encrypt(input_key.get(), iv=input_iv.get())
                                )
            EncryptBtn.grid(row=1,column=2,padx=5,pady=5,columnspan=2,sticky="ew")
            self.dynamic_widgets.append(EncryptBtn)
        else:
            frame3= LabelFrame(self.window, background=self.background_color)
            frame3.grid(row=2,column=0, padx=5,pady=5)

            self.dynamic_widgets.append(frame3)

            label_key = Label(frame3,
                                text="Llave",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
            label_key.grid(row=0,column=0, padx=5,pady=5)
            self.dynamic_widgets.append(label_key)
            input_key = Entry(frame3)
            input_key.grid(row=0,column=1, padx=5,pady=5)
            self.dynamic_widgets.append(input_key)

            FileBtn = Button(frame3,
                                text="Buscar Imagen",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.pathFile()
                                )
            FileBtn.grid(row=1,column=0, padx=5,pady=5,sticky="ew")
            self.dynamic_widgets.append(FileBtn)

            EncryptBtn = Button(frame3,
                                text="Cifrar",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.encrypt(input_key.get())
                                )
            EncryptBtn.grid(row=1,column=1, padx=5,pady=5,sticky="ew")
            self.dynamic_widgets.append(EncryptBtn)

    def generateDecryptWidgets(self):
        if(self.option_mode != 1):
            frame3= LabelFrame(self.window, background=self.background_color)
            frame3.grid(row=2,column=0, padx=5,pady=5)

            self.dynamic_widgets.append(frame3)

            label_key = Label(frame3,
                                text="Llave",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
            label_key.grid(row=0,column=0, padx=5,pady=5)
            self.dynamic_widgets.append(label_key)
            input_key = Entry(frame3)
            input_key.grid(row=0,column=1, padx=5,pady=5)
            self.dynamic_widgets.append(input_key)

            label_iv = Label(frame3,
                                text="Vector Inicial",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
            label_iv.grid(row=0,column=2, padx=5,pady=5)
            self.dynamic_widgets.append(label_iv)
            input_iv = Entry(frame3)
            input_iv.grid(row=0,column=3, padx=5,pady=5)
            self.dynamic_widgets.append(input_iv)

            FileBtn = Button(frame3,
                                text="Buscar Imagen",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.pathFile()
                                )
            FileBtn.grid(row=1,column=0, padx=5,pady=5,columnspan=2,sticky="ew")
            self.dynamic_widgets.append(FileBtn)

            EncryptBtn = Button(frame3,
                                text="Descifrar",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.decrypt(input_key.get(), iv=input_iv.get())
                                )
            EncryptBtn.grid(row=1,column=2, padx=5,pady=5,columnspan=2,sticky="ew")
            self.dynamic_widgets.append(EncryptBtn)
        else:
            frame3= LabelFrame(self.window, background=self.background_color)
            frame3.grid(row=2,column=0, padx=5,pady=5)

            self.dynamic_widgets.append(frame3)

            label_key = Label(frame3,
                                text="Llave",
                                fg=self.white,
                                bg=self.background_color,
                                font=("Arial", 14)
                                )
            label_key.grid(row=0,column=0, padx=5,pady=5)
            self.dynamic_widgets.append(label_key)
            input_key = Entry(frame3)
            input_key.grid(row=0,column=1, padx=5,pady=5)
            self.dynamic_widgets.append(input_key)

            FileBtn = Button(frame3,
                                text="Buscar Imagen",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.pathFile()
                                )
            FileBtn.grid(row=1,column=0, padx=5,pady=5,sticky="ew")
            self.dynamic_widgets.append(FileBtn)

            EncryptBtn = Button(frame3,
                                text="Descifrar",
                                bd=0,
                                fg=self.white,
                                bg=self.select_color,
                                font=("Arial", 12),
                                command=lambda: self.decrypt(input_key.get())
                                )
            EncryptBtn.grid(row=1,column=1, padx=5,pady=5,sticky="ew")
            self.dynamic_widgets.append(EncryptBtn)

    def pathFile(self):
        self.path_message = filedialog.askopenfilename(
                                initialdir=os.getcwd(), 
                                title='Seleccione una imagen BMP', 
                                filetype=(('bmp images', "*.bmp"),('all files', '*'))
                            )
        self.choose_file = True

    def encrypt(self, keys, iv=''):
        self.cipher = DESImageCipher()
        if(iv != ''):
            if(len(keys) > 8):
                messagebox.showeror(
                    message="Error con el tamaño de la llave", title="Error"
                )
            if(len(iv) > 8):
                messagebox.showerror(
                    message="Error con el tamaño del vector de inicialización", title="Error"
                )
            if(len(iv) <= 8 and len(keys) <= 8):    
                self.cipher.setImagePath(self.path_message)
                self.cipher.setKey(bytes(keys, 'utf-8'))
                self.cipher.setIv(bytes(iv, 'utf-8'))
                modo = None
                if(self.option_mode == 1):
                    modo = 'ECB'
                elif(self.option_mode == 2):
                    modo = 'CBC'
                elif(self.option_mode == 3):
                    modo = 'CFB'
                elif(self.option_mode == 4):
                    modo = 'OFB'
                self.cipher.setMode(modo)
                self.cipher.encrypt()
                messagebox.showinfo(
                    message="Imagen cifrada correctamente", title="Operación exitosa"
                )
        elif(iv == ''):
            self.cipher.setImagePath(self.path_message)
            self.cipher.setKey(bytes(keys, 'utf-8'))
            if(len(keys) > 8):
                messagebox.showerror(
                    message="Error con el tamaño de la llave", title="Error"
                )
            else:
                modo = None
                if(self.option_mode == 1):
                    modo = 'ECB'
                elif(self.option_mode == 2):
                    modo = 'CBC'
                elif(self.option_mode == 3):
                    modo = 'CFB'
                elif(self.option_mode == 4):
                    modo = 'OFB'
                self.cipher.setMode(modo)
                self.cipher.encrypt()
                messagebox.showinfo(
                    message="Imagen cifrada correctamente", title="Operación exitosa"
                )
        else:
            messagebox.showinfo(
                message="Error", title="Error"
            )

    def decrypt(self, key, iv=''):
        self.cipher = DESImageCipher()
        if(iv != ''):
            if(len(key) > 8):
                messagebox.showeror(
                    message="Error con el tamaño de la llave", title="Error"
                )
            if(len(iv) > 8):
                messagebox.showerror(
                    message="Error con el tamaño del vector de inicialización", title="Error"
                )
            if(len(iv) <= 8 and len(key) <= 8):
                self.cipher.setImagePath(self.path_message)
                self.cipher.setKey(bytes(key, 'utf-8'))
                self.cipher.setIv(bytes(iv, 'utf-8'))
                modo = None
                if(self.option_mode == 1):
                    modo = 'ECB'
                elif(self.option_mode == 2):
                    modo = 'CBC'
                elif(self.option_mode == 3):
                    modo = 'CFB'
                elif(self.option_mode == 4):
                    modo = 'OFB'
                self.cipher.setMode(modo)
                self.cipher.decrypt()
                messagebox.showinfo(
                    message="Imagen descifrada correctamente", title="Operación exitosa"
                )
        elif(iv == ''):
            self.cipher.setImagePath(self.path_message)
            self.cipher.setKey(bytes(key, 'utf-8'))
            if(len(key) > 8):
                messagebox.showerror(
                    message="Error con el tamaño de la llave", title="Error"
                )
            else:
                modo = None
                if(self.option_mode == 1):
                    modo = 'ECB'
                elif(self.option_mode == 2):
                    modo = 'CBC'
                elif(self.option_mode == 3):
                    modo = 'CFB'
                elif(self.option_mode == 4):
                    modo = 'OFB'
                self.cipher.setMode(modo)
                self.cipher.decrypt()
                messagebox.showinfo(
                    message="Imagen descifrada correctamente", title="Operación exitosa"
                )
        else:
            messagebox.showinfo(
                message="Error", title="Error"
            )


if __name__ == "__main__":
    gui = GUI()
    gui.run()