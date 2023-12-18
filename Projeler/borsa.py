import pandas as pd
import matplotlib.pyplot as plt

def borsa_karsilastirma(gunluk_endeks, genel_endeks):
    # CSV dosyalarını okuyarak verileri alalım
    df_gunluk = pd.read_csv(gunluk_endeks)
    df_genel = pd.read_csv(genel_endeks)

    # Tarih sütununu indeks olarak ayarlayalım
    df_gunluk['Tarih'] = pd.to_datetime(df_gunluk['Tarih'])
    df_gunluk.set_index('Tarih', inplace=True)

    df_genel['Tarih'] = pd.to_datetime(df_genel['Tarih'])
    df_genel.set_index('Tarih', inplace=True)

    # İki veri kümesini birleştirelim ve boş değerleri çıkaralım
    df = pd.concat([df_gunluk['Kapanis'], df_genel['Kapanis']], axis=1, keys=['Günlük', 'Genel'])
    df.dropna(inplace=True)

    # Verileri çizdirelim
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Günlük'], label='Günlük Endeks')
    plt.plot(df.index, df['Genel'], label='Genel Endeks')
    plt.xlabel('Tarih')
    plt.ylabel('Endeks Değerleri')
    plt.title('Günlük ve Genel Endeks Karşılaştırması')
    plt.legend()
    plt.show()

# Örnek kullanım
borsa_karsilastirma('gunluk_endeks.csv', 'genel_endeks.csv')
