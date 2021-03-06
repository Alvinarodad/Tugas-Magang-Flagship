#Program berikut menggunakan Tkinter Widget GUI 
#Source code yang digunakan adalah Python
#Source code berikut digunakan untuk mengecek informasi memori (RAM)
from tkinter import *     #memanggil library Tkinter
import subprocess as sub  #memanggil library subprocess dan dinyatakan sebagai sub

p = sub.Popen(('cat', '/proc/meminfo'), stdout=sub.PIPE)  #code untuk mengecek informasi memori pada Linux
keluaran = sub.check_output(('head', '-6'), stdin=p.stdout) #meminta hasil keluaran hanya sebanyak 6 informasi memori

root = Tk()        #memanggil program Tkinter 
text = Text(root)  #mendklarasikan text ke dalam Tkinter 
text.pack()        #membuat garis pinggir pada Tkinter 
text.insert(END, keluaran)  #memasukkan text berupa hasil pada code keluaran 
l = Label(root, text="Alvin Memory Usage")  #membuat judul Label
l.config(font =("Courier", 14))             #mengatur font judul Label
l.pack()                                    #menampilkan judul Label
root.mainloop()                             #menjalankan program Tkinter Widget GUI
