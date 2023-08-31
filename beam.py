import streamlit as st
import pandas as pd
from pickle import load
import pickle
import numpy as np
import math
from PIL import Image
import os

st.header("Deflection of Cantilever Beam Edge Loading")

st.sidebar.header('User Input Parameters')

image = Image.open("beam1.png")
st.subheader('Dimensional Parameters')
st.image(image, caption='Figure 1: Cantilever beam with load at the edge')

def user_input_features():
    edge_load = st.sidebar.slider('P (N)', min_value=850, max_value=1150, step=20)
    span_length = st.sidebar.slider('L (mm)', min_value=850, max_value=1150, step=20)
    breadth = st.sidebar.slider('b (mm)', min_value=50, max_value=150, step=20)
    height = st.sidebar.slider('h (mm)', min_value=100, max_value=200, step=20)
    elastic_modulus_sel = st.sidebar.radio('E (GPa)', ('79000','110000','200000')) 
    if elastic_modulus_sel=='79000': elastic_modulus=79000
    elif elastic_modulus_sel=='110000': elastic_modulus=110000
    elif elastic_modulus_sel=='200000': elastic_modulus=200000

    yield_strength_sel = st.sidebar.radio('Fy (MPa)', ('235','355','440')) 
    if yield_strength_sel=='235': yield_strength=235
    elif yield_strength_sel=='355': yield_strength=355
    elif yield_strength_sel=='440': yield_strength=440

    data = {'P (N)': edge_load,
            'L (mm)': span_length,
            'b (mm)': breadth,
            'h (mm)': height,
            'E (GPa)': elastic_modulus,           
            'Fy (MPa)': yield_strength}
    features = pd.DataFrame(data, index=[0])
    return features


df = user_input_features()

P=df['P (N)'].values.item()
L=df['L (mm)'].values.item()
b=df['b (mm)'].values.item()
h=df['h (mm)'].values.item()
E=df['E (GPa)'].values.item()
Fy=df['Fy (MPa)'].values.item()

I = b*h**3/(12)
d = P*L**3/(3*E*I)

user_input={'P (N)': "{:.2f}".format(P),
            'L (mm)': "{:.2f}".format(L),
            'b (mm)': "{:.2f}".format(b),
            'h (mm)': "{:.2f}".format(h),
            'E (GPa)': "{:.2f}".format(E),
            'Fy (MPa)': "{:.2f}".format(Fy)}
user_input_df=pd.DataFrame(user_input, index=[0])
st.subheader('User Input Parameters')
st.write(user_input_df)

calculated_param={'I (mm^4)': "{:.2f}".format(I)}
calculated_param_df=pd.DataFrame(calculated_param, index=[0])
st.subheader('Calculated Beam Moment of Inertia')
st.write(calculated_param_df)

calculated_param={'d (mm)': "{:.2f}".format(d)}
calculated_param_df=pd.DataFrame(calculated_param, index=[0])
st.subheader('Calculated Beam maximum deflection')
st.write(calculated_param_df)

st.subheader('Nomenclature')
st.write('P is the beam load magnitude; L is the beam span length; b is the beam breadth; h is the beam height; E is the beam elastic modulus; Fy is the beam yield strength.')

st.subheader('Reference')
st.write('Merrill C.W. Lee, Rozetta M. Payne, Donald W. Kelly, Rodney S. Thomson b, Determination of robustness for a stiffened composite structure using stochastic analysis, Composite Structures 86 (2008) 78 -84, https://doi:10.1016/j.compstruct.2008.03.036')
st.markdown('[Pre-Test](https://forms.gle/wPvcgnZAC57MkCxN8)', unsafe_allow_html=True)