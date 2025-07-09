import streamlit as st
import pandas as pd
import joblib

st.title("HomeLens Kira Tahmin Sistemi")

# Seçenek listeleri
semtler = ['Bornova', 'Karşıyaka', 'Buca', 'Bayraklı', 'Konak', 'Balçova', 'Karabağlar']
oda_sayilari = ['1+1', '2+1', '3+1', '4+1']
isitma_tipleri = ['Doğalgaz Kombi', 'Merkezi Sistem', 'Soba', 'Klima']
site_durumlari = ['Evet', 'Hayır']
esya_durumlari = ['Evet', 'Hayır']
asansor_durumlari = ['Evet', 'Hayır']
balkon_durumlari = ['Evet', 'Hayır']
manzara_durumlari = ['Şehir', 'Deniz', 'Yok']

# Kullanıcıdan değerleri al
semt = st.selectbox("Semt Seçiniz", semtler)
metrekare = st.number_input("Metrekare Giriniz", min_value=20, max_value=300, value=100)
oda_sayisi = st.selectbox("Oda Sayısı", oda_sayilari)
isitma = st.selectbox("Isıtma Tipi", isitma_tipleri)
site_icinde = st.selectbox("Site Durumu", site_durumlari)
esyali = st.selectbox("Eşya Durumu", esya_durumlari)
asansor = st.selectbox("Asansör", asansor_durumlari)
balkon = st.selectbox("Balkon", balkon_durumlari)
manzara = st.selectbox("Manzara", manzara_durumlari)
bina_yasi = st.number_input("Bina Yaşı", min_value=0, max_value=100, value=10)
kat = st.number_input("Kat Sayısı", min_value=1, max_value=30, value=1)
aidat = st.number_input("Aidat (TL)", min_value=0, max_value=2000, value=100)

model_choice = st.selectbox("Model Seçiniz", ["Linear Regression", "Random Forest", "XGBoost"])

if st.button("Tahmin Et"):
    model_paths = {
        "Linear Regression": "linear_model.pkl",
        "Random Forest": "rf_model.pkl",
        "XGBoost": "xgb_model.pkl"
    }
    # Modeli yükle
    model = joblib.load(model_paths[model_choice])

    # Kullanıcı verilerini DataFrame olarak hazırla (Modelin beklediği sütun isimleri ile)
    input_df = pd.DataFrame([{
        "Semt": semt,
        "Metrekare": metrekare,
        "Oda_Sayisi": oda_sayisi,
        "Isitma": isitma,
        "Site_Icinde": site_icinde,
        "Esyali": esyali,
        "Asansor": asansor,
        "Balkon": balkon,
        "Manzara": manzara,
        "Bina_Yasi": bina_yasi,
        "Kat": kat,
        "Aidat": aidat
    }])

    # Tahmin yap
    prediction = model.predict(input_df)

    # Sonucu göster
    st.success(f"Tahmini Kira: {prediction[0]:.2f} TL")
