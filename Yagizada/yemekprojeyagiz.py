import tkinter as tk
from tkinter import messagebox
def hesapla():
    toplam_kalori = 0
    ozet_metni = "Seçilenler:\n"
    
    # Yemeklerin ve miktarların kontrolü
    for yemek, veri in yemekler.items():
        miktar = int(veri['miktar_kutusu'].get())
        if miktar > 0:
            kalori_degeri = miktar * veri['kalori']
            toplam_kalori += kalori_degeri
            ozet_metni += f"- {miktar} adet {yemek}: {kalori_degeri} kcal\n"
    
    if toplam_kalori > 0:
        ozet_metni += f"\nToplam: {toplam_kalori} kcal"
        messagebox.showinfo("Kalori Sonucu", ozet_metni)
    else:
        messagebox.showwarning("Uyarı", "Lütfen en az bir yemek miktarı seçin!")
# Ana Pencere Kurulumu
root = tk.Tk()
root.title("Yemek Kalori Hesaplayıcı")
root.geometry("400x450")
root.configure(padx=20, pady=20)
# Yemek verileri ve kalori değerleri (1 adet için)
yemek_listesi = {
    "Hamburger": 250,
    "Lahmacun": 220,
    "Tavuk Izgara": 180,
    "Pizza Dilimi": 285,
    "Patates Kızartması": 312
}
yemekler = {}
tk.Label(root, text="Yemek Listesi", font=("Arial", 14, "bold")).pack(pady=10)
# Arayüz Elemanlarını Oluşturma
for yemek, kalori in yemek_listesi.items():
    frame = tk.Frame(root)
    frame.pack(fill="x", pady=5)
    
    # Yemek Adı ve Kalori Bilgisi
    lbl = tk.Label(frame, text=f"{yemek} ({kalori} kcal)", width=20, anchor="w")
    lbl.pack(side="left")
    
    # Adet Seçme Kutusu (Spinbox)
    spin = tk.Spinbox(frame, from_=0, to=10, width=5)
    spin.pack(side="right")
    
    # Verileri sakla
    yemekler[yemek] = {'kalori': kalori, 'miktar_kutusu': spin}
# Hesapla Butonu
hesapla_btn = tk.Button(root, text="Toplam Kaloriyi Göster", command=hesapla, 
                       bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), pady=10)
hesapla_btn.pack(fill="x", pady=20)
root.mainloop()