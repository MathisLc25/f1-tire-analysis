import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from src.data_loader import get_session_data

st.set_page_config(page_title="F1 Tire Analysis", layout="wide")
st.title("Duel de Performance : Hamilton vs Verstappen (Silverstone 2024)")
st.write("Modélisation de la dégradation des gommes intermédiaires via régressions linéaire et polynomiale.")

with st.spinner("Chargement des données de télémétrie..."):
    session = get_session_data(2024, 'Silverstone', 'R')

def get_clean_driver_laps(driver_code):
    laps = session.laps.pick_driver(driver_code)
    return laps.loc[laps['IsAccurate'] == True].copy()

def get_trends(laps_df, degree=2):
    stint_data = laps_df.loc[laps_df['Compound'] == 'INTERMEDIATE']
    if len(stint_data) < 10: 
        return None, None, None, None
    
    X = stint_data['TyreLife'].values.reshape(-1, 1)
    y = stint_data['LapTime'].dt.total_seconds().values
    X_smooth = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    
    lin_model = LinearRegression().fit(X, y)
    y_lin = lin_model.predict(X_smooth)
    
    poly_model = make_pipeline(PolynomialFeatures(degree), LinearRegression()).fit(X, y)
    y_poly = poly_model.predict(X_smooth)
    
    lap_offset = stint_data['LapNumber'].min() - X.min()
    return X_smooth + lap_offset, y_lin, y_poly, stint_data

ham_laps = get_clean_driver_laps('HAM')
ver_laps = get_clean_driver_laps('VER')

fig, ax = plt.subplots(figsize=(15, 8))

X_h, y_lin_h, y_poly_h, d_h = get_trends(ham_laps, degree=2)
if d_h is not None:
    ax.scatter(d_h['LapNumber'], d_h['LapTime'].dt.total_seconds(), color='cyan', alpha=0.3, label='Points HAM')
    ax.plot(X_h, y_lin_h, color='cyan', linestyle='--', label='Hamilton (Linéaire)')
    ax.plot(X_h, y_poly_h, color='darkcyan', linewidth=3, label='Hamilton (Polynomial Deg2)')

X_v, y_lin_v, y_poly_v, d_v = get_trends(ver_laps, degree=3)
if d_v is not None:
    ax.scatter(d_v['LapNumber'], d_v['LapTime'].dt.total_seconds(), color='blue', alpha=0.3, label='Points VER')
    ax.plot(X_v, y_lin_v, color='blue', linestyle='--', label='Verstappen (Linéaire)')
    ax.plot(X_v, y_poly_v, color='darkblue', linewidth=3, label='Verstappen (Polynomial Deg3)')

ax.set_title('Duel de Performance : Hamilton vs Verstappen (Silverstone 2024)', fontsize=14)
ax.set_xlabel('Numéro du Tour', fontsize=12)
ax.set_ylabel('Temps au Tour (Secondes)', fontsize=12)
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)
fig.tight_layout()

st.pyplot(fig)