import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import pickle
import html
import json
import os
import rarfile
import io
import csv
st. set_page_config(
                   page_title='Flat Resale', 
                   initial_sidebar_state= 'expanded',
                   layout= 'wide'
                   )


data = pd.read_csv('/app/finalflatshort.csv')
df = pd.DataFrame(data)

#def predict_fun():  
           

#streamlit part
title_text ='''<h1 style='font_size: 32px; text-align: center; color: blue;' > FLAT RESALE </h1'''
st.markdown(title_text, unsafe_allow_html=True)
#st.title(" FLAT RESALE ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

with st.sidebar:
  selected = option_menu('Main Menu', options=['Home', 'Prediction'], icons=['house','lightbulb'], default_index=1,orientation='vertical')

if selected == "Home":
        st.markdown(" ")
        st.markdown(" ")
        #img1 = Image.open("images/phonepe3.jpg")
        #st.image( img1,use_column_width=True,channels="RGB" )
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        # Example usage
  



elif selected == "Prediction":
    
  
    tab1= st.tabs(["RESALE PRICE"])
    with tab1:
             
      
            with st.form("my form 1"): 
            
                      col1,col2,col3 = st.columns([5,2,5])
                      with col1:
                                 st.write (" ")
                                 city_names = list(set(df["town"]))
                                 city_name =  st.selectbox("City Name",city_names,key =1)
                                 
                                 flat_type =  st.selectbox("Item Type",item_type_values, key =2)
                                 country =  st.selectbox("Country",country_values, key =3)
                                 application =  st.selectbox("Application",application_values, key =4)
                                 product_ref =  st.selectbox("Product Reference",product_ref_values, key =5)
                      with col3:
                                 #st.write(f'<h5 style="color:rgb(0, 153, 153, 0.4);">NOTE: Min & Max given for reference, y)
                                 quantity_tons = st.text_input("Enter Quantity Tons (Min:611728 & Max:1722207579)")
                                 thickness = st.text_input("Enter Thickness (Min:0.18 & Max:400)")
                                 width = st.text_input("Enter Width (Min:1 & Max:2990)")
                                 customer = st.text_input("Enter Customer ID (Min:12458 & Max:30408185)")
                                 submitted = st.form_submit_button(label = "RESALE PRICE")
                                 #if submitted:
                                 #st.write(f"Predicting the price for: ok ") #{brand} {model} ({year}), Mileage: {mileage} km.")
                                 st.markdown("""
                                           <style>
                                            div.stButton > button:first-child {
                                             background-color: #009999;
                                             color: white;
                                             width: 100%;
                                           }
                                           </sytle>
                                           """, unsafe_allow_html=True)   
                                  
                      if submitted:
                                      predict_text ='''<h5 style='font_size: 4px; text-align: left; color: green;' > Selling Price </h5'''
                                      st.markdown(predict_text, unsafe_allow_html=True)
  
    
                                  
                    
