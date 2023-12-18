from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.geometry("240x140")
pencere.title("Bahçeşehir")
def uyari():
    messagebox.showinfo("Başlık buraya yazılır", "Mesajı buraya yazınız")
    
btn = Button(pencere,text="Tıkla",command=uyari)
btn.pack()

pencere.mainloop()