import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import pickle
import html
import json
import zipfile
import os
import rarfile

st. set_page_config(
                   page_title='Flat Resale', 
                   initial_sidebar_state= 'expanded',
                   layout= 'wide'
                   )
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

        # Path to the RAR file and output directory
        rar_file_path = "flat_data/finalflat.rar"  # Replace with your RAR file path
        output_directory = "output_folder"

        # Extract the RAR file
        with rarfile.RarFile(rar_file_path) as rf:
             rf.extractall(output_directory)

        # List the first three files in the output directory
        files = os.listdir(output_directory)[:3]

        # Display the first three files
        st.write("First three extracted files:")
        for file in files:
            st.write(file)


elif selected == "Prediction":
    
  
    tab1,tab2 = st.tabs(["RESALE PRICE","EDA"])
    with tab1:
            country_values = [28.,  25.,  30.,  32.,  38.,  78.,  27.,  77., 113.,  79.,  26., 39.,  40.,  84.,  80., 107.,  89.]
            status_values = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
            item_type_values = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
            application_values = [10.0, 41.0, 28.0, 59.0, 15.0, 4.0, 38.0, 56.0, 42.0, 26.0, 27.0, 19.0, 20.0, 66.0, 29.0, 22.0, 40.0, 25.0, 67.0, 79.0, 3.0, 99.0,  2.0,  5.0, 39.0, 69.0, 70.0, 65.0, 58.0, 68.0]
            product_ref_values = [1670798778, 1668701718,     628377,     640665,     611993, 
                                  1668701376,  164141591, 1671863738, 1332077137,     640405,
                                  1693867550, 1665572374, 1282007633, 1668701698,     628117,
                                  1690738206,     628112,     640400, 1671876026,  164336407,
                                  164337175, 1668701725, 1665572032,     611728, 1721130331,
                                  1693867563,     611733, 1690738219, 1722207579,  929423819,
                                  1665584320, 1665584662, 1665584642]
      
            with st.form("my form 1"): 
            
                      col1,col2,col3 = st.columns([5,2,5])
                      with col1:
                                 st.write (" ")
                                 status =  st.selectbox("Status",status_values,key =1)
                                 item_type =  st.selectbox("Item Type",item_type_values, key =2)
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
  
    with tab2:
      
              with st.form("my form 2"): 
                     
                      col4,col5,col6 = st.columns([5,2,5])
                      with col4:
                                 st.write (" ")
                                 status =  st.selectbox("Status",status_values,key =6)
                                 item_type =  st.selectbox("Item Type",item_type_values, key =7)
                                 country =  st.selectbox("Country",country_values, key =8)
                                 application =  st.selectbox("Application",application_values, key =9)
                                 product_ref =  st.selectbox("Product Reference",product_ref_values, key =10)
                      with col6:
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
                                      predict_text ='''<h5 style='font_size: 4px; text-align: left; color: green;' > Status </h5'''
                                      st.markdown(predict_text, unsafe_allow_html=True)
