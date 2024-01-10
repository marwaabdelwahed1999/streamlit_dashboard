import streamlit as st
import streamlit.components.v1 as comp
import plotly.express as px
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Bike Sales Dashboard",
    page_icon="images/bicycle.png",
    layout="wide",
)
# page background color 
st.markdown("""
                  <style>
                  .st-emotion-cache-z5fcl4 {
                  background-color: black;
                  width: 100%;
                  padding: 6rem 1rem 10rem;
                  min-width: auto;
                  max-width: initial;
                                        }
                  </style>
                  
                  
                  
                  """,unsafe_allow_html=True)



with open("style/index.html", "r") as html_file:
    html_content = html_file.read()
    
with open("style/index.css", "r") as css_index_file:
    css_index = css_index_file.read()
    
with open("style/style.css", "r") as css_style_file:
    css_style = css_style_file.read()


com.html(f"""
        <style>
        {css_index}
        {css_style}
        {html_content}
        
        
        </style>
        
                {html_content}

         
         """,height=2200,scrolling=False)

# end