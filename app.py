import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import time
from sklearn import linear_model
df=[]
st.header("Regression")
upload = st.file_uploader("",type=['csv','xlsx'])
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>
            <html><body><p></p><body/></html>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
if upload is not None:


	print(upload)
	print("Hello")
	try:
		df = pd.read_csv(upload)
	except :
		
		df = pd.read_excel(upload)

if st.checkbox("Show/Hide Data"):
	st.write(df)
st.info("Please select values for analysis")

c1,c2 = st.columns(2)
if upload:
	
	df.dropna(inplace=True)
	with c1:
		x1 = st.multiselect("X",df.columns)
		x = df[x1]
        
	with c2:
		y1 = st.multiselect("Y",df.columns)
		y = df[y1]
	
	

if st.checkbox("Forecasting"):

	reg = linear_model.LinearRegression()
	reg.fit(x,y)
	y_pred =reg.predict(x)
	st.header("Coefficient")
	st.text(reg.coef_)
	st.header("Intercept")
	st.text(reg.intercept_)
if st.checkbox("Plot"):
	fig, ax = plt.subplots()
	plt.title("LinearRegression")
	ax.scatter(x,y)
	ax.scatter(x,y_pred)
	
	st.pyplot(fig)
# reg.coef_
# reg.intercept_

# from matplotlib_venn import venn2
# venn2(subsets = (5,8,5),set_labels =("boy","girl"))
# plt.show()
# st.pyplot()