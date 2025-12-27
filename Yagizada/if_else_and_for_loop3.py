can = 60
    
for i in range(10):
    can -= 1
    if can == 0:
        print("Oyun bitti")
    else:
        print(f"Kalan canınız: {can}")