# Boş bir To-Do listesi oluşturma
to_do_list = []

# Kullanıcıdan alınan girdileri listeye ekleyen fonksiyon
def add_task(to_do_list):
    task = input("Yapılacak görevi girin: ")
    to_do_list.append(task)
    print("Görev başarıyla eklendi.")

# Listede bulunan görevleri gösteren fonksiyon
def show_tasks(to_do_list):
    print("Yapılacak Görevler: ")
    for task in to_do_list:
        print("- " + task)

# Listeden görev silen fonksiyon
def delete_task(to_do_list):
    task = input("Silmek istediğiniz görevi girin: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Görev başarıyla silindi.")
    else:
        print("Görev bulunamadı.")

# Ana döngü
while True:
    print("\nTo-Do List Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çıkış")
    choice = input("Seçiminiz (1/2/3/4): ")
    
    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_tasks(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")