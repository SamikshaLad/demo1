import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.title("IRIS FLOWER DASHBOARD")
st.divider()
st.sidebar.header("Description")

st.sidebar.divider()
st.sidebar.markdown("The Iris Dataset contains four features (length and width of sepals and petals) of 150 samples of three species of Iris(Iris setosa Iris virginica and Iris versicolor).")
#st.sidebar.text("Just for reference, here are pictures of the three flowers species:")
df=pd.read_csv("iris.csv")
#st.table(df)
col1, col2 = st.columns(2)
with col1:
   
   class_data=df['species'].value_counts()
   st.subheader("Pie Chart of Species")
   fig,ax=plt.subplots()
   x=['Setosa','versicolor','virginica']
   ax.pie(class_data,labels=x)
   st.pyplot(fig)
with col2:
   class_data=df['species'].value_counts()
   st.subheader("Bar Chart of Species")
   fig,ax=plt.subplots()
   x=['Setosa','versicolor','virginica']
   ax.bar(class_data,labels=x)
   st.bar_chart(fig)
    

    
