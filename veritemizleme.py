import pandas as pd
import numpy as np

ham_veri = pd.DataFrame({
    'Musteri_ID': [101, 102, 103, 104, 105],
    'Satis_Miktari': [250.5, np.nan, 150.0, 300.2, np.nan],
    'Geri_Bildirim_Skoru': [4.5, 3.0, np.nan, 4.8, 2.5]
})

temizlenmis_veri = ham_veri.dropna(subset=['Musteri_ID'])

temizlenmis_veri.loc[:, 'Satis_Miktari'] = temizlenmis_veri['Satis_Miktari'].fillna(
    temizlenmis_veri['Satis_Miktari'].mean()
)

temizlenmis_veri.loc[:, 'Geri_Bildirim_Skoru'] = temizlenmis_veri['Geri_Bildirim_Skoru'].fillna(
    temizlenmis_veri['Geri_Bildirim_Skoru'].median()
)

print(temizlenmis_veri)