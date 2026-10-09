import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Departmanlar ve bütçelerini içeren örnek bir veri seti oluşturuyoruz
veri = pd.DataFrame({
    "Departman": ["Pazarlama", "Satis", "IT", "IK", "Finans"],
    "Butce Milyon TL": [12.5, 18.2, 25.0, 5.4, 10.1]
})

# Plotly Express kullanarak veriyi görselleştirmek için bir çubuk grafiği (bar chart) hazırlıyoruz
grafik = px.bar(veri, x="Departman", y="Butce Milyon TL",
                title="Departmanlara Göre Bütçe Dağılımı",
                color="Departman", template="plotly_white")

# Dash web uygulamasını başlatıyoruz
uygulama = dash.Dash(__name__)

# Uygulamanın web arayüzünü (layout) HTML bileşenleriyle tasarlıyoruz
uygulama.layout = html.Div(children=[
    # Ana başlık (Ortalanmış)
    html.H1(children='Kurumsal İş Zekası (BI) Paneli', style={'textAlign': 'center'}),
    
    # Alt açıklama metni (Ortalanmış ve açık mavi renkli)
    html.Div(children='Stratejik karar alma süreçlerini destekleyen veriye dayalı içgörüler.',
             style={'textAlign': 'center', 'color': '#7FDBFF'}),
             
    # Hazırladığımız Plotly grafiğini web arayüzüne ekliyoruz
    dcc.Graph(id='butce-grafigi', figure=grafik)
])

# Uygulamayı yerel sunucuda (localhost) belirtilen portta (8050) çalıştırıyoruz
if __name__ == '__main__':
    uygulama.run(debug=False, port=8050)