#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:22:50 2024

@author: diego
"""

import pandas as pd
import matplotlib.pyplot as plt

MJD = '60575'

# Leer el archivo de texto
with open('./logCs/' + MJD + '_cs1.txt', 'r') as file:
    lines = file.readlines()

# Inicializar listas para almacenar los datos
FMJD_list = []

Freq_Offset_list = []
Osc_control_list = []

rf_amp1_list = []
rf_amp2_list = []

zeeman_freq_list = []
c_field_curr_list = []

E_multiplier_list = []
Signal_Gain_list = []

CBT_Oven_list = []
CBT_Oven_Err_list = []

Osc_Oven_list = []
Ion_Pump_list = []

HW_Ionizer_list = []
Mass_spec_list = []

SAW_Tuning_list = []
DRO_Tuning_list = []

MHz_PLL_list = []
uP_Clock_PLL_list = []

plus_12_V_list = []
minus_12_V_list = []

plus_5_V_list = []
thermometer_list = []

tempe_list = []
hum_list = []
pres_list = []

TD12_list = []
TD13_list = []


# Recorrer las líneas y extraer los valores deseados
for i, line in enumerate(lines):
    # Buscar la línea que contiene MJD
    if line.startswith('MJD'):
        mjd_value = int(line[6:13])
        hour_value = int(line[-9:-7])
        FMJD_list.append(mjd_value + hour_value/24)
    
    if line.startswith('Freq Offset'):
        Freq_Offset_value = float(line[18:28])
        Freq_Offset_list.append(Freq_Offset_value)
        osc_control_value = "{:.2f}".format(float(line[46:52]))
        Osc_control_list.append(osc_control_value)
        
    if line.startswith('RF amplitude 1'):
        rf_amp1_value = "{:.1f}".format(float(line[17:23]))
        rf_amp2_value = "{:.1f}".format(float(line[46:52]))
        rf_amp1_list.append(rf_amp1_value)
        rf_amp2_list.append(rf_amp2_value)
    
    if line.startswith('Zeeman Freq'):
        zeeman_freq_value = int(line[17:23])
        c_field_curr_value = "{:.1f}".format(float(line[46:52]))
        zeeman_freq_list.append(zeeman_freq_value)
        c_field_curr_list.append(c_field_curr_value)

    if line.startswith('E-multiplier'):
        E_multiplier_value = int(line[17:23])
        Signal_Gain_value = float(line[46:52])
        E_multiplier_list.append(E_multiplier_value)
        Signal_Gain_list.append(Signal_Gain_value)

    if line.startswith('CBT Oven'):
        CBT_Oven_value = float(line[17:23])
        CBT_Oven_Err_value = float(line[46:52])
        CBT_Oven_list.append(CBT_Oven_value)
        CBT_Oven_Err_list.append(CBT_Oven_Err_value)

    if line.startswith('Osc. Oven'):
        Osc_Oven_value = float(line[17:23])
        Ion_Pump_value = float(line[46:52])
        Osc_Oven_list.append(Osc_Oven_value)
        Ion_Pump_list.append(Ion_Pump_value)

    if line.startswith('HW Ionizer'):
        HW_Ionizer_value = float(line[17:23])
        Mass_spec_value = float(line[46:52])
        HW_Ionizer_list.append(HW_Ionizer_value)
        Mass_spec_list.append(Mass_spec_value)

    if line.startswith('SAW Tuning'):
        SAW_Tuning_value = float(line[17:23])
        DRO_Tuning_value = float(line[46:52])
        SAW_Tuning_list.append(SAW_Tuning_value)
        DRO_Tuning_list.append(DRO_Tuning_value)

    if line.startswith('87MHz PLL'):
        MHz_PLL_value = float(line[17:23])
        uP_Clock_PLL_value = float(line[46:52])
        MHz_PLL_list.append(MHz_PLL_value)
        uP_Clock_PLL_list.append(uP_Clock_PLL_value)

    if line.startswith('+12V supply'):
        plus_12_V_value = float(line[17:23])
        minus_12_V_value = float(line[46:52])
        plus_12_V_list.append(plus_12_V_value)
        minus_12_V_list.append(minus_12_V_value)

    if line.startswith('+5V  supply'):
        plus_5_V_value = float(line[17:23])
        thermometer_value =  float(line[46:52])
        plus_5_V_list.append(plus_5_V_value)
        thermometer_list.append(thermometer_value)

# =============================================================================
# Temperatura, Presion y Humedad ambientes
# =============================================================================
 
destino = './logTPH/' + MJD + '_TPH.txt' 
   
file = open(destino, "r")
datos = file.read().split("\n")

for j in range(len(datos)-1):
    tempe_list.append(float(datos[j][3:8]))
    hum_list.append(float(datos[j][9:14]))
    pres_list.append(float(datos[j][15:24]))

# =============================================================================
# Diferencias de tiempo con otros relojes locales
# =============================================================================

destino12 = './logTD/TDI1-I2_' + MJD + '.txt' 
destino13 = './logTD/TDI1-I3_' + MJD + '.txt' 
   
file12 = open(destino12, "r")
file13 = open(destino13, "r")

datos12 = file12.read().split("\n")
datos13 = file13.read().split("\n")

for j in range(len(datos12)-1):
    TD12_list.append(float(datos12[j][-7:]))
    TD13_list.append(float(datos13[j][-7:]))

# Crear un DataFrame con los valores extraídos
df = pd.DataFrame({
    'FMJD': FMJD_list,
    'Freq Offset': Freq_Offset_list,
    'Osc. control (%)': Osc_control_list,
    'RF amplitude 1 (%)': rf_amp1_list,
    'RF amplitude 2 (%)': rf_amp2_list,
    'Zeeman Freq (Hz)': zeeman_freq_list,
    'C-field curr (mA)': c_field_curr_list,
    'E_multiplier (V)': E_multiplier_list,
    'Signal Gain (%)': Signal_Gain_list,
    'CBT Oven (V)': CBT_Oven_list,
    'CBT_Oven_Err (C)': CBT_Oven_Err_list,
    'Ion Pump (uA)': Ion_Pump_list,
    'Osc. Oven (V)': Osc_Oven_list,
    'HW Ionizer (V)': HW_Ionizer_list,
    'Mass spec (V)': Mass_spec_list,
    'SAW Tuning (V)': SAW_Tuning_list,
    'DRO Tuning (V)': DRO_Tuning_list,
    '87MHz PLL (V)':  MHz_PLL_list,
    'uP Clock PLL (V)': uP_Clock_PLL_list,
    '+12V Supply (V)': plus_12_V_list,
    '-12V Supply (V)': minus_12_V_list,
    '+5V  Supply (V)': plus_5_V_list,
    'Thermometer (C)': thermometer_list,
    'Temperatura amb (C)': tempe_list,
    'Humedad relativa': hum_list,
    'Presion atm': pres_list,
    'TD 1-2 (ns)': TD12_list,
    'TD 1-3 (ns)': TD13_list,
})

df.plot(x='FMJD', y='+5V  Supply (V)', kind='line')  # You can choose 'line', 'bar', etc.
plt.show()
