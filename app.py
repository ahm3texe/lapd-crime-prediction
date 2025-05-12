import streamlit as st
import pandas as pd
import pickle

# Modeli yükle
model = pickle.load(open("rf_model.pkl", "rb"))

# Başlık
st.title("LAPD Suç Tahmin Uygulaması")
st.write("Suç detaylarını girin, ciddi mi (Part 1) yoksa hafif mi (Part 2) olduğunu tahmin edelim!")

# Kullanıcıdan input alma
time_occ = st.number_input("Suç Saati (0-1 arası, normalize; 0 = 00:00, 0.5 = 12:00, 1=23:59)", min_value=0.0, max_value=1.0, value=0.5)
vict_age = st.number_input("Mağdur Yaşı (0-1 arası, normalize; 0 = 1, 0.5 = 55, 1=110)", min_value=0.0, max_value=1.0, value=0.5)
lat = st.number_input("Enlem (0-1 arası, normalize)", min_value=0.0, max_value=1.0, value=0.5)
crm_cd = st.number_input("Suç Kodu (0-500 arası, kodlanmış)", min_value=0, max_value=500, value=100)
premis_cd = st.number_input("Olay Yeri Kodu (0-300 arası, kodlanmış)", min_value=0, max_value=300, value=100)

# Girdileri bir veri çerçevesine dönüştür
input_data = pd.DataFrame(
    [[crm_cd, premis_cd, time_occ, vict_age, lat]],
    columns=["Crm Cd", "Premis Cd", "TIME OCC", "Vict Age", "LAT"]
)

# Tahmin yap
if st.button("Tahmin Yap"):
    prediction = model.predict(input_data)
    result = "Ciddi Suç (Part 1)" if prediction[0] == 1 else "Hafif Suç (Part 2)"
    st.success(f"Tahmin Sonucu: **{result}**")
