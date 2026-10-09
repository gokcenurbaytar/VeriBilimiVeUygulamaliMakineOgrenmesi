import pandas as pd

# Örnek bir satış veri seti oluşturuyoruz
veri_seti = pd.DataFrame({
    'Tarih': pd.date_range(start='2026-01-01', periods=6, freq='ME'),
    'Kategori': ['Elektronik', 'Giyim', 'Elektronik', 'Kozmetik', 'Giyim', 'Elektronik'],
    'Satis': [1200, 800, 1500, 400, 950, 2000]
})

# Tarih sütunundan 'Ay' ve 'Çeyrek' (Quarter) bilgilerini çekip yeni sütunlar ekliyoruz
veri_seti['Ay'] = veri_seti['Tarih'].dt.month
veri_seti['Ceyrek'] = veri_seti['Tarih'].dt.quarter

# Veri setinin yeni sütunlar eklenmiş güncel halini ekrana yazdırıyoruz
print(veri_seti)

# Kategorilere göre gruplama yaparak satışların toplamını, ortalamasını ve işlem sayısını hesaplıyoruz
kategori_ozeti = veri_seti.groupby('Kategori').agg(
    Toplam_Satis=('Satis', 'sum'),
    Ortalama_Satis=('Satis', 'mean'),
    Islem_Sayisi=('Satis', 'count')
).reset_index()

# Hesaplanan özet tabloyu görüntülüyoruz
print(kategori_ozeti)