import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from src.data_loader import get_session_data

session = get_session_data(2024, 'Silverstone', 'R')

def get_clean_driver_laps(driver_code):
    laps = session.laps.pick_driver(driver_code)
    return laps.loc[laps['IsAccurate'] == True].copy()

def get_trends(laps_df, degree=2):
    stint_data = laps_df.loc[laps_df['Compound'] == 'INTERMEDIATE']
    if len(stint_data) < 10: return None, None, None, None
    
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

plt.figure(figsize=(15, 8))

X_h, y_lin_h, y_poly_h, d_h = get_trends(ham_laps, degree=2)
if d_h is not None:
    plt.scatter(d_h['LapNumber'], d_h['LapTime'].dt.total_seconds(), color='cyan', alpha=0.2)
    plt.plot(X_h, y_lin_h, color='cyan', linestyle='--', label='Hamilton (Linéaire)')
    plt.plot(X_h, y_poly_h, color='darkcyan', linewidth=3, label='Hamilton (Polynomial Deg2)')

X_v, y_lin_v, y_poly_v, d_v = get_trends(ver_laps, degree=3)
if d_v is not None:
    plt.scatter(d_v['LapNumber'], d_v['LapTime'].dt.total_seconds(), color='blue', alpha=0.2)
    plt.plot(X_v, y_lin_v, color='blue', linestyle='--', label='Verstappen (Linéaire)')
    plt.plot(X_v, y_poly_v, color='darkblue', linewidth=3, label='Verstappen (Polynomial Deg3)')

plt.title('Duel de Performance : Hamilton vs Verstappen (Silverstone 2024)', fontsize=14)
plt.xlabel('Numéro du Tour', fontsize=12)
plt.ylabel('Temps au Tour (Secondes)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()