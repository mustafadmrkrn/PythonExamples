import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import json
import os

# --- VERİTABANI (DEFTER) AYARLARI ---
# Notlarımızı bilgisayarda tutacağımız dosyanın adı
DOSYA_ADI = "notlar.json"
notlar_sozlugu = {}

# Eğer daha önceden oluşturulmuş bir not dosyamız varsa onu okuyup hafızaya alıyoruz
if os.path.exists(DOSYA_ADI):
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        notlar_sozlugu = json.load(dosya)

def dosyay_kaydet():
    # Hafızadaki notları gerçek dosyaya (deftere) yazma işlemi
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(notlar_sozlugu, dosya, ensure_ascii=False, indent=4)

# --- BUTONLARIN VE TAKVİMİN GÖREVLERİ (FONKSİYONLAR) ---

def tarih_secildi(event):
    """Takvimden yeni bir gün seçildiğinde çalışır."""
    secilen_tarih = tarih_kutusu.get()
    
    # Önce ekrandaki yazı kutusunu tamamen temizle (1. satır, 0. karakterden sonuna kadar)
    not_alani.delete("1.0", tk.END)
    
    # Eğer seçilen tarihte daha önceden yazılmış bir not varsa, onu ekrana getir
    if secilen_tarih in notlar_sozlugu:
        not_alani.insert(tk.END, notlar_sozlugu[secilen_tarih])

def kaydet():
    secilen_tarih = tarih_kutusu.get()
    yazilan_not = not_alani.get("1.0", tk.END).strip()
    
    if secilen_tarih in notlar_sozlugu:
        messagebox.showwarning("Uyarı", "Bu tarihte zaten not var! Güncellemek için 'Değiştir' butonuna basın.")
        return
        
    if yazilan_not == "":
        messagebox.showwarning("Uyarı", "Boş not kaydedilemez!")
        return
        
    # Notu sözlüğe ekle ve dosyaya kaydet
    notlar_sozlugu[secilen_tarih] = yazilan_not
    dosyay_kaydet()
    messagebox.showinfo("Başarılı", "Notunuz başarıyla kaydedildi!")

def degistir():
    secilen_tarih = tarih_kutusu.get()
    yazilan_not = not_alani.get("1.0", tk.END).strip()
    
    if secilen_tarih not in notlar_sozlugu:
        messagebox.showwarning("Uyarı", "Bu tarihte değiştirilecek bir not bulunamadı! Önce 'Kaydet' yapmalısınız.")
        return
        
    # Eski notun üzerine yeni notu yaz ve dosyayı güncelle
    notlar_sozlugu[secilen_tarih] = yazilan_not
    dosyay_kaydet()
    messagebox.showinfo("Başarılı", "Notunuz başarıyla değiştirildi!")

def sil():
    secilen_tarih = tarih_kutusu.get()
    
    if secilen_tarih in notlar_sozlugu:
        # Notu sözlükten sil
        del notlar_sozlugu[secilen_tarih]
        dosyay_kaydet()
        
        # Ekranı temizle
        not_alani.delete("1.0", tk.END)
        messagebox.showinfo("Başarılı", "Not silindi!")
    else:
        messagebox.showwarning("Uyarı", "Bu tarihte silinecek bir not yok.")


# --- ARAYÜZ (ODAYI VE EŞYALARI TASARLAMA) ---

pencere = tk.Tk()
pencere.title("Günlük Ajanda ve Not Uygulaması")
pencere.geometry("500x550")
pencere.config(bg="#f0f0f0") # Odanın duvar rengi (açık gri)

# 1. Eşya: Bilgi Etiketi
etiket = tk.Label(pencere, text="Bir Tarih Seçin ve Notunuzu Yazın", font=("Arial", 14, "bold"), bg="#f0f0f0")
etiket.pack(pady=15)

# 2. Eşya: Takvim (Tarih Kutusu)
tarih_kutusu = DateEntry(pencere, width=20, background='darkblue', foreground='white', borderwidth=2, font=("Arial", 12))
tarih_kutusu.pack(pady=5)
# Takvimden farklı bir güne tıklandığında 'tarih_secildi' görevini çalıştır
tarih_kutusu.bind("<<DateEntrySelected>>", tarih_secildi)

# 3. Eşya: Yazı (Not) Kutusu (Geniş bir Text alanı)
not_alani = tk.Text(pencere, font=("Arial", 12), width=45, height=15, wrap=tk.WORD)
not_alani.pack(pady=15)

# Butonları yan yana dizebilmek için odaya bir raf (Frame) alıyoruz
buton_rafi = tk.Frame(pencere, bg="#f0f0f0")
buton_rafi.pack(pady=10)

# 4. Eşyalar: Butonlar (Rafın içine diziyoruz)
btn_kaydet = tk.Button(buton_rafi, text="Kaydet", bg="#28a745", fg="white", font=("Arial", 11, "bold"), width=10, command=kaydet)
btn_kaydet.pack(side=tk.LEFT, padx=10)

btn_degistir = tk.Button(buton_rafi, text="Değiştir", bg="#ffc107", fg="black", font=("Arial", 11, "bold"), width=10, command=degistir)
btn_degistir.pack(side=tk.LEFT, padx=10)

btn_sil = tk.Button(buton_rafi, text="Sil", bg="#dc3545", fg="white", font=("Arial", 11, "bold"), width=10, command=sil)
btn_sil.pack(side=tk.LEFT, padx=10)

# Program açıldığında bugünün tarihine ait not varsa otomatik ekrana getir
tarih_secildi(None)

# Odayı dinlemeye başla
pencere.mainloop()