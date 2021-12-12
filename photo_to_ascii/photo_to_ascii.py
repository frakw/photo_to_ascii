#!/usr/bin/python
# -*- coding: utf-8 -*- 
#圖片轉ascii code
import tkinter as tk
import os
from PIL import Image,ImageTk
import numpy as np
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import messagebox
def print_ascii():
    if not filepath:
        messagebox.showerror(title='還沒選擇檔案', message=R'請按"開啟檔案"的按鈕')
        return
    global result
    img_L = Image.open(filepath).convert('L')#.resize((128,128))
    #img_L.show()
    pixel_array = np.array(img_L)
    result = R""
    transfer.configure(text='轉換中...',state=tk.DISABLED)
    window.update_idletasks()
    for i in range(0,img_L.height):
        for j in range(0,img_L.width):
            result+=ascii_table[pixel_array[i][j]//len(ascii_table)]
        result+='\n'
    #print(result)
    ascii_shower.delete('1.0','end')
    ascii_shower.insert('1.0',result)
    transfer.configure(text='轉換',state=tk.NORMAL)
def get_file_path():
    global filepath
    tmp_filepath = askopenfilename(title='選擇一張圖片進行轉換', filetypes=[('圖檔','*.png *.jpg *jpeg *bmp *tiff *ppm')],initialdir=R'C:\Windows')#PPM, PNG, JPEG TIFF, and BMP.
    if tmp_filepath :
        filepath = tmp_filepath
        #print(filepath)
        img = ImageTk.PhotoImage(Image.open(filepath))#.resize((128,128))
        img_shower.configure(image=img)
        img_shower.image = img
        window.update_idletasks()
        print_ascii()
def to_txt():
    if not filepath:
        messagebox.showerror(title='還沒選擇檔案', message=R'請按"開啟檔案"的按鈕')
        return
    save_filepath = asksaveasfilename(title='儲存位置', filetypes=[('TXT檔','*.txt')],initialfile='output.txt',initialdir='./')
    if save_filepath:
        fp = open(save_filepath,mode='w')
        fp.write(result)

result=""
ascii_table = " .,:;irsXA253hMHGS#9B&@"
filepath = ""
window = tk.Tk()
tkFont.Font(family='Consolas', size=15)#要放在window = tk.Tk()之後
window.title('圖片轉ascii code')
window.geometry('1280x900')

open_file = tk.Button(window,text='開啟檔案',command=get_file_path)
transfer = tk.Button(window,text='轉換',command=print_ascii)
output = tk.Button(window,text='輸出到txt檔',command=to_txt)

f = tk.Frame(window,width=640,height=825)
img_shower=tk.Label(window,image=None)

Xscrollbar = tk.Scrollbar(f, orient = tk.HORIZONTAL)
Yscrollbar = tk.Scrollbar(f, orient = tk.VERTICAL)

Xscrollbar.pack(side=tk.BOTTOM,fill=tk.X)
Yscrollbar.pack(side=tk.RIGHT,fill=tk.Y)
ascii_shower = tk.Text(f,font=('Consolas', 2),wrap = 'none',yscrollcommand=Yscrollbar.set,xscrollcommand=Xscrollbar.set)
ascii_shower.pack(expand = tk.YES,fill = tk.BOTH)
Xscrollbar['command'] = ascii_shower.xview
Yscrollbar['command'] = ascii_shower.yview

open_file.place(x=0,y=0,width=426,height=75)
transfer.place(x=427,y=0,width=426,height=75)
output.place(x=853,y=0,width=426,height=75)

img_shower.place(x=0,y=76,width=640,height=825)
f.place(x=640,y=76,width=640,height=825)

window.mainloop()